```console
$ gdb ./factchecker
gdb-peda$ b*main+1741
gdb-peda$ r
[SNIP]
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffd550 --> 0x7ffff7e233d0 --> 0x7ffff7d3b710 (<_ZNSt13basic_ostreamIwSt11char_traitsIwEED1Ev>:	endbr64)
0008| 0x7fffffffd558 --> 0x7ffff7e233f8 --> 0x7ffff7d3b750 (<_ZTv0_n24_NSt13basic_ostreamIwSt11char_traitsIwEED1Ev>:	endbr64)
0016| 0x7fffffffd560 --> 0x55555556aed0 ("picoCTF{wELF_d0N3_mate_fd65ee4e}")
0024| 0x7fffffffd568 --> 0x20 (' ')
0032| 0x7fffffffd570 --> 0x2e ('.')
0040| 0x7fffffffd578 --> 0x7ffff7e23398 --> 0x7ffff7d3b630 (<_ZTv0_n24_NSoD1Ev>:	endbr64)
0048| 0x7fffffffd580 --> 0x7fffffffd590 --> 0x7ffff7e20034 --> 0x200007fff 
0056| 0x7fffffffd588 --> 0x1 
[------------------------------------------------------------------------------]
[SNIP]
```

The flag is: `picoCTF{wELF_d0N3_mate_fd65ee4e}`