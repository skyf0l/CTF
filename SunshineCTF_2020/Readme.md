# SunshineCTF 2020

sam, 07 nov. 2020, 14:00 UTC — lun, 09 nov. 2020, 14:00 UTC

# Web

## PasswordPandemonium
```
You're looking to book a flight to Florida with the totally-legit new budget airline, Oceanic Airlines!
All you need to do is create an account!
Should be pretty easy, right? ...right?
http://pandemonium.web.2020.sunshinectf.org

Author: Jeffrey D.
```

At the website, there is a basic create account form with an username and a password field

We try to create an account:

```
Username: azerty
Password: azerty
-> Error: Password is too short.

Password: azertyuiop
-> Error: Password must include more than two special characters.

Password: azertyuiop???
-> Error: Password must include a prime amount of numbers.

Password: 1azertyuiop???2
-> Error: Password must have equal amount of uppercase and lowercase characters.

Password: 1azertyAZERTY???2
-> Error: Password must include an emoji.

Password: 1azertyAZERTY???2🤬
-> Error: Password must be valid JavaScript that evaluates to True.

Password: 1//azertyAZERTY???2🤬
-> Error: Password's MD5 hash must start with a number.

Password: 1//azeRTY🤬🤬🤬🤬🤬YTReza//1
-> Flag: sun{Pal1ndr0m1c_EcMaScRiPt}
```

The flag is: `sun{Pal1ndr0m1c_EcMaScRiPt}`

# Reversing

## Hotel Door Puzzle

```
I thought I'd come down to Orlando on a vacation.
I thought I left work behind me!
What's at my hotel door when I show up?
A Silly reverse engineering puzzle to get into my hotel room!
I thought I was supposed to relax this weekend.
Instead of me doing it, I hired you to solve it for me.
Let me into my hotel room and you'll get some free internet points!

File: hotel_key_puzzle 
```

When we run program, it ask a password
We decompile program with ghidra and we see a check_flag function:
```c
int check_flag(char * flag)
{
  size_t size;
  int res;

  size = strlen(flag);
  if (size == 0x1d) {
    if (flag[0x13] == '6') {
      flag[6] = flag[6] + '\x03';
      if (flag[0x10] == 'n') {
        flag[0x14] = flag[0x14] + -8;
        flag[0x1a] = flag[0x1a] + -6;
        if (flag[0xd] == 'r') {
[...]
```

The function is so big: [check_flag_function.c](Reversing/check_flag_function.c)

We can write a python script to crack it:
```python3
#!/usr/bin/python3

import re
import sys

size = 0x1d
flag = ['_'] * size
mods = [0] * size

for line in open(sys.argv[1]):
    line = line.strip()

    if len(line) < 2 or line[:2] == '//':
        continue
    if line == 'res = 1;':
        # end on comparaisons
        break

    if line[:4] == 'if (':
        # extract pos and char from if line
        # if (flag[pos] == 'char') {
        match = re.search(r'\[([0-9a-fx]*)\].*\'(.)\'', line)
        pos = eval(match.group(1))
        char = match.group(2)
        flag[pos] = chr(ord(char) - mods[pos])

    elif line[:4] == 'flag':
        # extract pos and mod from if line
        # flag[pos] = flag[pos] + mod;
        match = re.search(r'flag\[([x0-9a-f]+)\]\s\+\s(.*);', line)
        pos = eval(match.group(1))
        mod = eval(match.group(2))
        if type(mod) == str:
            mod = ord(mod)
        mods[pos] += mod
    
    print(''.join(flag))
```

Run it:
```
$ python3 crack_check_flag.py check_flag_function.c | uniq
___________________6_________
________________n__6_________
_____________r__n__6_________
_____________r__n__6-________
_____________r_nn__6-________
__________p__r_nn__6-________
___{______p__r_nn__6-________
___{______p__r_nn__6-q_______
__n{______p__r_nn__6-q_______
s_n{______p__r_nn__6-q_______
s_n{___l__p__r_nn__6-q_______
s_n{___l__p__runn__6-q_______
s_n{___l__p_-runn__6-q_______
s_n{b__l__p_-runn__6-q_______
s_n{b_ll__p_-runn__6-q_______
s_n{b_ll__p_-runn_n6-q_______
s_n{b_ll__p_-runn_n6-qu______
s_n{b_ll__p_-runn_n6-qu1_____
sun{b_ll__p_-runn_n6-qu1_____
sun{b_ll__p_-runn_n6-qu1c____
sun{b_ll__p_-runn_n6-qu1c___}
sun{b_ll__p_-runn_n6-qu1c_l_}
sun{b_ll__p_-runn_n6-qu1c_ly}
sun{b_llh_p_-runn_n6-qu1c_ly}
sun{b_llh0p_-runn_n6-qu1c_ly}
sun{b3llh0p_-runn_n6-qu1c_ly}
sun{b3llh0p_-runn_n6-qu1ckly}
sun{b3llh0p_-runn1n6-qu1ckly}
sun{b3llh0p5-runn1n6-qu1ckly}
```

The flag is: `sun{b3llh0p5-runn1n6-qu1ckly}`
