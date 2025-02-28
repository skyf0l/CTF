```console
$ gdb ./crackme100
gdb-peda$ b*main+0x1f4
gdb-peda$ r
Enter the secret password: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
[SNIP]
[-------------------------------------code-------------------------------------]
   0x40135d <main+487>:	lea    rax,[rbp-0xa0]
   0x401364 <main+494>:	mov    rsi,rcx
   0x401367 <main+497>:	mov    rdi,rax
=> 0x40136a <main+500>:	call   0x401060 <memcmp@plt>
   0x40136f <main+505>:	test   eax,eax
   0x401371 <main+507>:	jne    0x401389 <main+531>
   0x401373 <main+509>:	mov    esi,0x402029
   0x401378 <main+514>:	mov    edi,0x402040
Guessed arguments:
arg[0]: 0x7fffffffd700 ("addgdggjdggjgjjmdggjgjjmgjjmjmmpdggjgjjmgjjmjmmpgj")
arg[1]: 0x7fffffffd740 ("qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze")
arg[2]: 0x32 ('2')
arg[3]: 0x7fffffffd740 ("qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze")
[SNIP]
```

Password is `qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze`, encoded `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` is `addgdggjdggjgjjmdggjgjjmgjjmjmmpdggjgjjmgjjmjmmpgj`.

Seemed to be a simple substitution cipher, so I wrote a script to decode it.

```python
# file: gen_password.py
expected = "qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze"

# with aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
got = "addgdggjdggjgjjmdggjgjjmgjjmjmmpdggjgjjmgjjmjmmpgj"

password = ""
for (got_char, expected_char) in zip(got, expected):
    password += chr(ord('a') - ord(got_char) + ord(expected_char))

print(password)
```

```console
$ python crackme.py 
qe`jd\jlt\[^a\giibmkrYncqXnZ^f_kgmnZ]YeVm_\_g[`]t\
```

```console
$ ./crackme100 
Enter the secret password: qe`jd\jlt\[^a\giibmkrYncqXnZ^f_kgmnZ]YeVm_\_g[`]t\
SUCCESS! Here is your flag: picoCTF{sample_flag}
$ nc titan.picoctf.net 54373
Enter the secret password: qe`jd\jlt\[^a\giibmkrYncqXnZ^f_kgmnZ]YeVm_\_g[`]t\
SUCCESS! Here is your flag: picoCTF{s0lv3_angry_symb0ls_4699696e}
```