# Forensics

## Microsooft
```
We have to use Microsoft Word at the office!? Oof...

Download the file below.
Files: microsooft.docx
```
We extract files in `microsooft.docx` and we see if flag is write in plaintext:
```
$ grep -R flag
src/oof.txt: [...] flag{oof_is_right_why_gfxdata_though} [...]
```

The flag is: `flag{oof_is_right_why_gfxdata_though}`

## Volatile
```
What was the flag again? I don't remember...

Download the file below.

Note, this flag is not in the usual format.

Large File Hosted with Google Drive
Files: memdump.raw
```

`memdump.raw` is a memory dump, we will use volatility (https://github.com/volatilityfoundation/volatility) to analyse it

First af all, we get the profile of the memory dump:
```
vol -f memdump.raw imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/tom.rorato/Downloads/memdump.raw)
                      PAE type : PAE
                           DTB : 0x185000L
                          KDBG : 0x8276fc28L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0x82770c00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2020-04-20 21:16:55 UTC+0000
     Image local date and time : 2020-04-20 14:16:55 -0700
```
We will use the profile: `Win7SP1x86_23418`

We don't know where to get the flag, so we try everything

And we finally fing the flag in console history:
```
vol -f memdump.raw --profile Win7SP1x86_23418 consoles
Volatility Foundation Volatility Framework 2.6.1
**************************************************
ConsoleProcess: conhost.exe Pid: 3468
Console: 0xc781c0 CommandHistorySize: 50
HistoryBufferCount: 1 HistoryBufferMax: 4
OriginalTitle: %SystemRoot%\system32\cmd.exe
Title: C:\Windows\system32\cmd.exe
AttachedProcess: cmd.exe Pid: 3460 Handle: 0x5c
----
CommandHistory: 0x2f0448 Application: cmd.exe Flags: Allocated, Reset
CommandCount: 1 LastAdded: 0 LastDisplayed: 0
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x5c
Cmd #0 at 0x2f4680: echo JCTF{nice_volatility_tricks_bro}
----
Screen 0x2d62d8 X:80 Y:300
Dump:
Microsoft Windows [Version 6.1.7601]                                            
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.                 
                                                                                
C:\Users\JCTF>echo JCTF{nice_volatility_tricks_bro}                             
JCTF{nice_volatility_tricks_bro}                                                
                                                                                
C:\Users\JCTF>                      
```

The flag is: `JCTF{nice_volatility_tricks_bro}`

## Cow Pie
```
Ew. Some cow left this for us. It's gross... but something doesn't seem right...

Download the file below.
Files: manure
```
`manure` is a `QEMU QCOW2 Image`

But before all, we try to see if flag is write in plaintext:
```
$ strings manure
[...]
flag{this_flag_says_mooo_what_say_you}
[...]
```

The flag is: `flag{this_flag_says_mooo_what_say_you}`
