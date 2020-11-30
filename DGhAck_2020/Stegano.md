# Stegano

## Time for something different (150 points)

```
Description:

Le serveur récoltant les candidatures à nos offres d’emploi en cyberdéfense a été attaqué.
Nous avons enregistré un fichier trace au format PCAP. Aidez-nous à comprendre ce qu’il s’est passé ?

Fichiers joints:
data.pcap 1.53kB
sha256: b34fc04418320941838c268e36b84ce9ccc5abdf7088c773a577367e0fe49012
```

All trames are exactly same except the time between them:
```
$ tshark -r data.pcap
    1   0.000000 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
    2   0.703011 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
    3   1.465858 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
    4   2.119027 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
    5   2.831841 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
    6   4.065128 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
    7   5.228682 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
    8   5.711408 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
    9   6.193885 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   10   7.346273 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   11   8.429533 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   12   9.542633 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   13  10.415249 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   14  11.528470 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   15  12.671630 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   16  13.834918 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   17  14.317492 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   18  14.800088 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   19  15.482997 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   20  15.995057 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   21  17.178110 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   22  17.670983 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   23  18.783221 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   24  19.956524 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   25  20.318264 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
   26  21.571729 192.168.0.14 → 192.168.0.254 ICMP 42 Echo (ping) request  id=0x0000, seq=0/0, ttl=64
```

May be, the message is hidden by the time between each request, we can try it:
```
$ tshark -r data.pcap -Tfields -e frame.time_delta
0.000000000
0.703011000
0.762847000
0.653169000
0.712814000
1.233287000
1.163554000
0.482726000
0.482477000
1.152388000
1.083260000
1.113100000
0.872616000
1.113221000
1.143160000
1.163288000
0.482574000
0.482596000
0.682909000
0.512060000
1.183053000
0.492873000
1.112238000
1.173303000
0.361740000
1.253465000
```

We select only the first 3 digits of each value:

```
070 076 065 071 123 116 048 048 115 108 111 087 111 114 116 048 048 068 051 118 049 111 117 036 125
```

And we decode it from decimal with [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)&input=MDcwIDA3NiAwNjUgMDcxIDEyMyAxMTYgMDQ4IDA0OCAxMTUgMTA4IDExMSAwODcgMTExIDExNCAxMTYgMDQ4IDA0OCAwNjggMDUxIDExOCAwNDkgMTExIDExNyAwMzYgMTI1)

The flag is: `FLAG{t00sloWort00D3v1ou$}`
