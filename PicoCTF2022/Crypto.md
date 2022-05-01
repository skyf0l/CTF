# Crypto

- [basic-mod1](Crypto.md#basic-mod1)
- [basic-mod2](Crypto.md#basic-mod2)
- [credstuff](Crypto.md#credstuff)

# basic-mod1

```
Author: Will Hong
Description

We found this weird message being passed around on the servers, we think we have a working decrpytion scheme.
Download the message here.
Take each number mod 37 and map it to the following character set:
0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.

Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
```

The downloaded file content is:

```
128 63 242 87 151 147 50 369 239 248 205 346 299 73 335 189 105 293 37 214 333 137
```

Following the steps above, we can decrypt the message with the following python code:

```python3
#!/usr/bin/env python3

ENC = "128 63 242 87 151 147 50 369 239 248 205 346 299 73 335 189 105 293 37 214 333 137"

CHAR_SET = "abcdefghijklmnopqrstuvwxyz0123456789_"

plaintext = ""
for token in ENC.split():
    value = int(token) % 37
    plaintext += CHAR_SET[value]

print(f"picoCTF{{{plaintext}}}")
```

After running the code above, we get the following result:

```console
$ python3 solve.py
picoCTF{r0und_n_r0und_ce58a3a0}
```

The flag is: `picoCTF{r0und_n_r0und_ce58a3a0}`

# basic-mod2

```
Author: Will Hong
Description

A new modular challenge! Download the message here.
Take each number mod 41 and find the modular inverse for the result.
Then map to the following character set:
1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.

Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
```

The downloaded file content is:

```
186 249 356 395 303 337 190 393 146 174 446 127 385 400 420 226 76 294 144 90 291 445 137
```

Following the steps above, we can decrypt the message with the following python code:

```python3
#!/usr/bin/env python3

ENC = "186 249 356 395 303 337 190 393 146 174 446 127 385 400 420 226 76 294 144 90 291 445 137"

CHAR_SET = ".abcdefghijklmnopqrstuvwxyz0123456789_"

plaintext = ""
for token in ENC.split():
    value = int(token) % 41
    modinv = pow(value, -1, 41)
    plaintext += CHAR_SET[modinv]

print(f"picoCTF{{{plaintext}}}")
```

After running the code above, we get the following result:

```console
$ python3 solve.py
picoCTF{1nv3r53ly_h4rd_b7fb947c}
```

The flag is: `picoCTF{1nv3r53ly_h4rd_b7fb947c}`

# credstuff

```
Author: Will Hong / LT 'syreal' Jones
Description

We found a leak of a blackmarket website's login credentials.
Can you find the password of the user cultiris and successfully decrypt it?
Download the leak here.

The first user in usernames.txt corresponds to the first password in passwords.txt.
The second user corresponds to the second password, and so on.
```

Files are [usernames.txt](Crypto/credstuff/usernames.txt):

```
engineerrissoles
icebunt
fruitfultry
celebritypentathlon
--SNIP--
```

And [passwords.txt](Crypto/credstuff/passwords.txt):

```
CMPTmLrgfYCexGzJu6TbdGwZa
GK73YKE2XD2TEnvJeHRBdfpt2
UukmEk5NCPGUSfs5tGWPK26gG
kaL36YJtvZMdbTdLuQRx84t85
--SNIP--
```

First we need to find offset of the username `cultiris`:

```bash
$ grep -n cultiris usernames.txt
378:cultiris
```

Then, we can find the password of the user `cultiris` at line 378:

```bash
$ sed -n '378p' passwords.txt
cvpbPGS{P7e1S_54I35_71Z3}
```

The password seems to be encrypted using ROT13, let's try to decode it:

```bash
$ echo "cvpbPGS{P7e1S_54I35_71Z3}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
picoCTF{C7r1F_54V35_71M3}
```

The flag is: `picoCTF{C7r1F_54V35_71M3}`

# morse-code

```
Author: Will Hong
Description

Morse code is well known. Can you decrypt this?
Download the file here.

Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.
```

The file [morse_chal.wav](Crypto/morse-code/morse_chal.wav) is a audio with many `beeep`s. It looks like morse code as mentioned in the challenge description.

```console
$ file morse_chal.wav
morse_chal.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
```

With the following website, we can upload the audio file and decode it [audio-decoder-adaptive](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) with parameters auto guessed:

- WPM: 12
- Farnsworth WPM: 12
- Frequency (Hz): 188

Then, we obtain the following result: `WH47 H47H 90D W20U9H7`

After wrapping the result in expected format, we get the following flag: `picoCTF{wh47_h47h_90d_w20u9h7}`

# rail-fence

```
Author: Will Hong
Description

A type of transposition cipher is the rail fence cipher, which is described here.
Here is one such cipher encrypted using the rail fence with 4 rails.
Can you decrypt it?
Download the message here.

Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.
```

The documentation redirects to [Wikipedia Rail fence cipher](https://en.wikipedia.org/wiki/Rail_fence_cipher)

The downloaded file content is:

```
Ta _7N6DDEhlg:W3D_H3C31N__883ef sHR053F38N43D1B i33___ND
```

Thanks to the [rail-fence-decoder](https://www.boxentriq.com/code-breaking/rail-fence-cipher) website, we can decode the message with the key `4`:

Then we get the following result:

```
The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D81DB8E3
```

The flag is: `picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D81DB8E3}`

# substitution0

```
Author: Will Hong
Description

A message has come in but it seems to be all scrambled.
Luckily it seems to have the key at the beginning.
Can you crack this substitution cipher?
Download the message here.
```

The downloaded file content is:

```
IADNMLPFYEJSWBZVXUHKGROCQT

Fmumgvzb Smpuibn iuzhm, oykf i puirm ibn hkikmsq iyu, ibn auzgpfk wm kfm ammksm
luzw i psihh dihm yb ofydf yk oih mbdszhmn. Yk oih i amigkylgs hdiuiaimgh, ibn, ik
kfik kywm, gbjbzob kz bikguisyhkh—zl dzguhm i pumik vuytm yb i hdymbkylyd vzybk
zl rymo. Kfmum omum koz uzgbn asidj hvzkh bmiu zbm mckumwykq zl kfm aidj, ibn i
szbp zbm bmiu kfm zkfmu. Kfm hdismh omum mcdmmnybpsq fiun ibn pszhhq, oykf iss kfm
ivvmiuibdm zl agubyhfmn pzsn. Kfm omypfk zl kfm ybhmdk oih rmuq umwiujiasm, ibn,
kijybp iss kfybph ybkz dzbhynmuikyzb, Y dzgsn fiunsq asiwm Egvykmu lzu fyh zvybyzb
umhvmdkybp yk.

Kfm lsip yh: vydzDKL{5GA5717G710B_3R0SG710B_A1N36772}
```

The first line seems to be the key: `IADNMLPFYEJSWBZVXUHKGROCQT`

Let's try to decode the message:

```console
$ tr 'IADNMLPFYEJSWBZVXUHKGROCQTiadnmlpfyejswbzvxuhkgrocqt' 'A-Za-z' < message.txt
ABCDEFGHIJKLMNOPQRSTUVWXYZ

Hereupon Legrand arose, with a grave and stately air, and brought me the beetle
from a glass case in which it was enclosed. It was a beautiful scarabaeus, and, at
that time, unknown to naturalists—of course a great prize in a scientific point
of view. There were two round black spots near one extremity of the back, and a
long one near the other. The scales were exceedingly hard and glossy, with all the
appearance of burnished gold. The weight of the insect was very remarkable, and,
taking all things into consideration, I could hardly blame Jupiter for his opinion
respecting it.

The flag is: picoCTF{5UB5717U710N_3V0LU710N_B1D36772}
```

# substitution1

```
Author: Will Hong
Description

A second message has come in the mail, and it seems almost identical to the first one.
Maybe the same thing will work again.
Download the message here.
```

The downloaded file content is:

```
GQEy (yxrjq erj gzpqfjc qxc euzi) zjc z qbpc re grwpfqcj ycgfjlqb grwpcqlqlro. Groqcyqzoqy zjc pjcycoqct vlqx z ycq re gxzuucoicy vxlgx qcyq qxclj gjczqlalqb, qcgxolgzu (zot irriuloi) ynluuy, zot pjrmucw-yrualoi zmlulqb. Gxzuucoicy fyfzuub gracj z ofwmcj re gzqcirjlcy, zot vxco yruact, czgx blcuty z yqjloi (gzuuct z euzi) vxlgx ly yfmwlqqct qr zo rouloc ygrjloi ycjalgc. GQEy zjc z ijczq vzb qr uczjo z vltc zjjzb re grwpfqcj ycgfjlqb ynluuy lo z yzec, ucizu coaljrowcoq, zot zjc xryqct zot puzbct mb wzob ycgfjlqb ijrfpy zjrfot qxc vrjut erj efo zot pjzgqlgc. Erj qxly pjrmucw, qxc euzi ly: plgrGQE{EJ3SF3OGB_4774GN5_4J3_G001_C5M0GGTM}
```

We don't know the key, but we can guess some letters by guessing plaintexts. Also, we lowercase all text to process upper and lowercase chars in same time. For example `qxc euzi ly: plgrgqe` seems to be `the flag is: picoctf`:

```console
$ cat message.txt | tr '[A-Z]' '[a-z]' | tr 'qxc euzi ly: plgrgqe' 'the flag is: picoctf'
ctfs (shojt foj captfje the flag) aje a tbpe of cowpftej secfjitb cowpetitioo. cootestaots aje pjeseotet vith a set of challeoges vhich test theij cjeatiaitb, techoical (aot googliog) snills, aot pjomlew-solaiog amilitb. challeoges fsfallb coaej a ofwmej of categojies, aot vheo solaet, each bielts a stjiog (callet a flag) vhich is sfmwittet to ao oolioe scojiog sejaice. ctfs aje a gjeat vab to leajo a vite ajjab of cowpftej secfjitb snills io a safe, legal eoaijooweot, aot aje hostet aot plabet mb waob secfjitb gjofps ajofot the vojlt foj ffo aot pjactice. foj this pjomlew, the flag is: picoctf{fj3sf3ocb_4774cn5_4j3_c001_e5m0cctm}
```

Then, we can guess the start of sentence: `CTFs (shojt foj captfje the flag)` seems to be `CTFs (short for capture the flag)`

Let's add it to out key:

```console:
$ cat message.txt | tr '[A-Z]' '[a-z]' | tr 'qxc euzi ly plgrgqe gqey (yxrjq erj gzpqfjc qxc euzi)' 'the flag is picoctf ctfs (short for capture the flag)'
ctfs (short for capture the flag) are a tbpe of cowputer securitb cowpetitioo. cootestaots are preseotet vith a set of challeoges vhich test their creatiaitb, techoical (aot googliog) snills, aot promlew-solaiog amilitb. challeoges usuallb coaer a ouwmer of categories, aot vheo solaet, each bielts a striog (callet a flag) vhich is sumwittet to ao oolioe scoriog seraice. ctfs are a great vab to learo a vite arrab of cowputer securitb snills io a safe, legal eoairooweot, aot are hostet aot plabet mb waob securitb groups arouot the vorlt for fuo aot practice. for this promlew, the flag is: picoctf{fr3su3ocb_4774cn5_4r3_c001_e5m0cctm}
```

By using the same method, we can guess the rest of the sentence: `are a tbpe of cowputer securitb cowpetitioo` seems to be `are a type of computer security competition`

And use it as new key:

```console
$ cat message.txt | tr '[A-Z]' '[a-z]' | tr 'qxc euzi ly plgrgqe gqey (yxrjq erj gzpqfjc qxc euzi) zjc z qbpc re grwpfqcj ycgfjlqb grwpcqlqlro' 'the flag is picoctf ctfs (short for capture the flag) are a type of computer security competition'
ctfs (short for capture the flag) are a type of computer security competition. contestants are presentet vith a set of challenges vhich test their creatiaity, technical (ant googling) snills, ant promlem-solaing amility. challenges usually coaer a nummer of categories, ant vhen solaet, each yielts a string (callet a flag) vhich is summittet to an online scoring seraice. ctfs are a great vay to learn a vite array of computer security snills in a safe, legal enaironment, ant are hostet ant playet my many security groups arount the vorlt for fun ant practice. for this promlem, the flag is: picoctf{fr3su3ncy_4774cn5_4r3_c001_e5m0cctm}
```

Missing letters are: `adhkmnstv` and there seems to be respectively `v???bk?dw`

Final round is:

```console
$ cat message.txt | tr '[A-Z]' '[a-z]' | tr 'qxc euzi ly plgrgqe gqey (yxrjq erj gzpqfjc qxc euzi) zjc z qbpc re grwpfqcj ycgfjlqb grwpcqlqlro adhkmnstv' 'the flag is picoctf ctfs (short for capture the flag) are a type of computer security competition v???bk?dw'
ctfs (short for capture the flag) are a type of computer security competition. contestants are presented with a set of challenges which test their creativity, technical (and googling) skills, and problem-solving ability. challenges usually cover a number of categories, and when solved, each yields a string (called a flag) which is submitted to an online scoring service. ctfs are a great way to learn a wide array of computer security skills in a safe, legal environment, and are hosted and played by many security groups around the world for fun and practice. for this problem, the flag is: picoctf{fr3?u3ncy_4774ck5_4r3_c001_e5b0ccdb}
```

After case conversion, the flag is: `picoCTF{FR3?U3NCY_4774CK5_4R3_C001_E5B0CCDB}`

A char in flag still not decoded but it really looks like a flag: `frequency_attacks_are_cool_esboccdb`

The flag is: `picoCTF{FR3QU3NCY_4774CK5_4R3_C001_E5B0CCDB`

# substitution2

```
Author: Will Hong
Description

It seems that another encrypted message has been intercepted.
The encryptor seems to have learned their lesson though and now there isn't any punctuation!
Can you still crack the cipher?
Download the message here.
```

The downloaded file content is:

```
jdiaiirmtjtipiaeknjdiabikkitjewkmtdizdmldtxdnnkxnqscjiatixcamjgxnqsijmjmnhtmhxkczmhlxgwiasejamnjehzctxgwiaxdekkihlijditixnqsijmjmnhtonxctsamqeamkgnhtgtjiqtezqmhmtjaejmnhochzeqihjektbdmxdeaipiagctiockehzqeavijewkitvmkktdnbipiabiwikmipijdisansiascasntinoedmldtxdnnkxnqscjiatixcamjgxnqsijmjmnhmthnjnhkgjnjiexdpekcewkitvmkktwcjektnjnlijtjczihjtmhjiaitjizmhehzirxmjizewncjxnqscjiatxmihxizioihtmpixnqsijmjmnhteainojihkewnamncteooematehzxnqiznbhjnachhmhlxdixvkmtjtehzirixcjmhlxnhomltxamsjtnooihtinhjdinjdiadehzmtdiepmkgonxctiznhirsknaejmnhehzmqsanpmtejmnhehznojihdetikiqihjtnoskegbiwikmipiexnqsijmjmnhjncxdmhlnhjdinooihtmpiikiqihjtnoxnqscjiatixcamjgmtjdiaionaiewijjiapidmxkionajixdipehlikmtqjntjczihjtmheqiamxehdmldtxdnnktocajdiabiwikmipijdejehchziatjehzmhlnonooihtmpijixdhmfcitmtittihjmekonaqnchjmhlehiooixjmpizioihtiehzjdejjdijnnktehzxnhomlcaejmnhonxctihxnchjiaizmhzioihtmpixnqsijmjmnhtznithnjkieztjczihjtjnvhnbjdimaihiqgetiooixjmpikgetjiexdmhljdiqjnexjmpikgjdmhvkmviehejjexviasmxnxjomtehnooihtmpikgnamihjizdmldtxdnnkxnqscjiatixcamjgxnqsijmjmnhjdejtiivtjnlihiaejimhjiaitjmhxnqscjiatxmihxieqnhldmldtxdnnkiatjiexdmhljdiqihncldewncjxnqscjiatixcamjgjnsmfcijdimaxcamntmjgqnjmpejmhljdiqjnirsknainhjdimanbhehzihewkmhljdiqjnwijjiazioihzjdimaqexdmhitjdiokelmtsmxnXJO{H6A4Q_4H41G515_15_73Z10C5_6XO50W5X}
```

It looks like the previous challenge: [substitution1](Crypto.md#substitution1) but spaces are missing.

Here, we are going to cheat by using an automated cracker for substitution cipher: [Monoalphabetic Substitution](https://www.dcode.fr/monoalphabetic-substitution)

The tool automatically detects the key and decrypts the message.

The flag is: `picoCTF{N6R4M_4N41Y515_15_73D10U5_6CF50B5C}`

# transposition-trial

```
Author: Will Hong
Description

Our data got corrupted on the way here.
Luckily, nothing got replaced, but every block of 3 got scrambled around!
The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message here.
```

The downloaded file content is:

```
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_VE1A1D3D}B
```

The stack of messages seems to be: `The flag is picoCTF{`

The first block of 3 chars is rotated by 1 char to the right and it seems to be the same for next blocks:

```
heT/fl /g a/...
231/231/234/...
The/ fl/ag /...
```

The following script will process the same algorithm to recover the flag:

```python3
#!/usr/bin/env python3

CIPHER = 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_VE1A1D3D}B'

plaintext = ''
for i in range(0, len(CIPHER), 3):
    chunk = CIPHER[i:i+3]
    chunk = chunk[2] + chunk[:2]
    plaintext += chunk

print(plaintext)
```

After running the code above, we get the following result:

```console
$ python3 solve.py
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_AE131DBD}
```

The flag is: `picoCTF{7R4N5P051N6_15_3XP3N51V3_AE131DBD}`

# Vigenere

```
Author: Mubarak Mikail
Description

Can you decrypt this message? Decrypt this message using this key "CYLAB".
```

The downloaded file content is:

```
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_d0db78b8}
```

The following script will decrypt the message with Vigenere algorithm and key `CYLAB`:

```python3
#!/usr/bin/env python3

import string

CIPHER = 'rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_d0db78b8}'
KEY = 'CYLAB'


def vigenere_decode(cipher: str, key: str) -> str:
    plain = ''
    i = 0
    for c in cipher:
        key_index = i % len(key)
        key_value = ord(key[i % len(key)]) - ord('A')
        if c in string.ascii_lowercase:
            plain += chr((ord(c) - ord('a') - key_value) % 26 + ord('a'))
            i += 1
        elif c in string.ascii_uppercase:
            plain += chr((ord(c) - ord('A') - key_value) % 26 + ord('A'))
            i += 1
        else:
            plain += c

    return plain


plaintext = vigenere_decode(CIPHER, KEY)
print(plaintext)
```

After running the code above, we get the following result:

```console
$ python solve.py
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_b0fq78b8}
```

The flag is: `picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_b0fq78b8}`

# diffie-hellman

```
Author: Will Hong
Description

Alice and Bob wanted to exchange information secretly.
The two of them agreed to use the Diffie-Hellman key exchange algorithm, using p = 13 and g = 5.
They both chose numbers secretly where Alice chose 7 and Bob chose 3.
Then, Alice sent Bob some encoded text (with both letters and digits) using the generated key as
the shift amount for a Caesar cipher over the alphabet and the decimal digits.
Can you figure out the contents of the message? Download the message here.

Wrap your decrypted message in the picoCTF flag format like: picoCTF{decrypted_message}
```

The downloaded file content is:

```
H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_DI9D987F
```

According to the algorithm [Diffie–Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange), the following script will decrypt the message:

```python3
#!/usr/bin/env python3

import string

CIPHER = 'H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_DI9D987F'
ALPHABET = string.ascii_uppercase + string.digits

# public primes
P = 13
G = 5

# private key
ALICE_PRIVATE = 7
BOB_PRIVATE = 3

# public keys
ALICE_PUBLIC = pow(G, ALICE_PRIVATE, P)
BOB_PUBLIC = pow(G, BOB_PRIVATE, P)

# shared secret
S = pow(BOB_PUBLIC, ALICE_PRIVATE, P)
assert(S == pow(ALICE_PUBLIC, BOB_PRIVATE, P))
print(f"Shared secret: {S}")


def decrypt_ceasar(ciphertext: str, alphabet: str, key: int) -> str:
    plaintext = ""
    for c in ciphertext:
        if c in alphabet:
            plaintext += alphabet[(alphabet.index(c) - key) % len(alphabet)]
        else:
            plaintext += c
    return plaintext


plaintext = decrypt_ceasar(CIPHER, ALPHABET,  S)
print(f"Flag: picoCTF{{{plaintext}}}")
```

After running the code above, we get the following result:

```
$ python3 solve.py
Shared secret: 5
Flag: picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_8D48432A}
```

The flag is: `picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_8D48432A}`

# Sum-O-Primes

```
Author: Joshua Inscoe
Description

We have so much faith in RSA we give you not just the product of the primes, but their sum as well!

    gen.py
    output.txt
```

We have a [gen.py](Crypto/Sum-O-Primes/gen.py) which generates a RSA key pair, encodes the flag, and writes `n` modulus, `x = p + q` and `c` ciphertext to [output.txt}(Crypto/Sum-O-Primes/output.txt) file.

Thanks to this aswer, we can understand the [Relation between factors and their sum on RSA](https://crypto.stackexchange.com/a/87309)

Then, we can follow the documentation to crack the key and decrypt the flag:

```python3
#!/usr/bin/env python3

from binascii import unhexlify
from math import isqrt

# known values
x = 0x1603fc8d929cb31edf62bcce2d06794f3efd095accb163e6f2b78941bd8c646d746369636a582aaac77c16a9486881a9e3db26d742e48c4adcc417ef98f310a0c5433ab077dd872530c3c3c77fe0c080d84154bfdb4c920df9617e986999104d9284516c7babc80dc53718d59032aefdf41b9be53957dea3f00a386b2666d446e
n = 0x75302ba292dc4bf47ffd690b8edc70ef1fcca5e148b2b9c1b60227788afcfe77a0097929ed3789fe51ac66f678c558244890a09ae4af3e7d098fd366a1c859edabbff1c9e164d5354968798107ae8518fcaab3743de58a141ffd26c1e16cb09fed1f6b0d68536ec7fba744ed120fea8c3a7ac1ebfa55d664d2f321fb44e814650147a9031f3bfa8f69d87393c7d88976d28d147398a355020bcb8e5613f0b29028b77db710e163ca1019fd3c3a065465ea457adec45243c385d12d3a1de3178f6ca05964be92e8b5bc24d420956de96ccc9ce39e70705660eb6b2f4e675aac7d6d7ba45c84223fc5819b37aa85beff1382f1c2c3b97603150f30c17f7e674441
c = 0x562888c70ce9a5c5ed9a0be1b6196f854ba2efcdb6dd0f79319ee9e1142659f90a6bae67481eb0f635f445d3c9889da84639beb84ff7159dcf4d3a389873dc90163270d80dbb9503cbc32992cb592069ba5b3eb2bbe410a3121d658f18e100f7bd878a25c27ab8c6c15b690fce1ca43288163c544bfce344bcd089a5f4733acc7dc4b6160718e3c627e81a58f650281413bb5bf7bad5c15b00c5a2ef7dbe7a44cce85ed5b1becd5273a26453cb84d327aa04ad8783f46d22d61b96c501515913ca88937475603437067ce9dc10d68efc3da282cd64acaf8f1368c1c09800cb51f70f784bd0f94e067af541ae8d20ab7bfc5569e1213ccdf69d8a81c4746e90c1
e = 65537

# calculate delta
delta = isqrt(x ** 2 - 4 * n)
assert(delta ** 2 == x ** 2 - 4 * n)

# calculate p and q
p = (x + delta) // 2
q = (x - delta) // 2
assert(p * q == n)
assert(p + q == x)

# calculate d
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

# decrypt c
m = pow(c, d, n)
plaintext = unhexlify(hex(m)[2:]).decode()
print(plaintext)
```

After running the code above, we get the following result:

```console
$ python solve_sum.py
picoCTF{674b189f}
```

The flag is: `picoCTF{674b189f}`
