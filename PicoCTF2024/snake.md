```console
$ cat snake | head -n40 | grep -oP '(?<=\()\d+' | xargs echo
4 54 41 0 112 32 25 49 33 3 0 0 57 32 108 23 48 4 9 70 7 110 36 8 108 7 49 10 4 86 43 104 44 91 7 18 106 124 89 78
```

This xor `picoCTF{` equals `t_Jo3t_J`, so `t_Jo3` is the key (can also be found in the source code).

Then, xoring the decoded string with `t_Jo3` we got `picoCTF{N0t_sO_coNfus1ng_sn@ke_7f44f566}`.

<https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)XOR(%7B'option':'UTF8','string':'t_Jo3'%7D,'Standard',false)&input=NCA1NCA0MSAwIDExMiAzMiAyNSA0OSAzMyAzIDAgMCA1NyAzMiAxMDggMjMgNDggNCA5IDcwIDcgMTEwIDM2IDggMTA4IDcgNDkgMTAgNCA4NiA0MyAxMDQgNDQgOTEgNyAxOCAxMDYgMTI0IDg5IDc4>
