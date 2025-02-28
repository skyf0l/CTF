```console
$ upx -d -o packed packer
$ strings packed
[SNIP]
Enter the password to unlock this file:
You entered: %s
Password correct, please see flag: 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f39343130343638327d
Access denied
[SNIP]
$ basecracker -c 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f39343130343638327d
Recipe: hex
Result: picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_94104682}
```
