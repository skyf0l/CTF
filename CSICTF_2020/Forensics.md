# Forensics

## Gradient sky
```
Gradient sky is a begginer level ctf challenge which is aimed towards rookies.

File: sky.jpg
```

```
$ strings sky.jpg
[...]
csictf{j0ker_w4snt_happy}
```

The flag is: `csictf{j0ker_w4snt_happy}`

## Archenemy
```
John likes Arch Linux. What is he hiding?

File: arched.png
```

We can exctract a file from `arched.png` with steghide and an empty passphrase:
```
$ steghide extract -sf arched.png 
Enter passphrase:
wrote extracted data to "flag.zip".
```

`flag.zip` is an archive protected by a password, we try to crack it:

```
$ zipCracker/zipcracker.py -f flag.zip -w /usr/share/wordlists/rockyou.txt 
    3638 / 14344394 |   0.00% -> masones1lndg456ce

Password cracked: kathmandu

Took 2.379971 seconds to crack the password. That is, 1529 attempts per second.
```

Then, file `meme.jpg` is extracted and we can read the flag on it.

The flag is: `csictf{1_h0pe_y0u_don't_s33_m3_here}`
