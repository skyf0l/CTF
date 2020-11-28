# Forensic

## Bwing (150 points)
```
Description:

Un expert forensic de DGA MI doit travailler sur un dump mémoire.
Au profit de l’activité missile, il doit retrouver des informations au sujet du plan d’une fusée.

Fichiers joints
dump.raw.gz 140.72MB
sha256: 966dabbf15c1d9b4b5f2896f17c322f6e38f60a433f8fd27f8f0596305eb838e
```

In archive, we have a memory dump named `dump.raw`

First of all, we need to identify the machine on which this dump was extracted:
```
$ strings dump.raw | grep BOOT_IMAGE
BOOT_IMAGE=/boot/vmlinuz-4.15.0-66-generic root=LABEL=cloudimg-rootfs ro console=tty1 console=ttyS0
BOOT_IMAGE=/boot/vmlinuz-4.15.0-66-generic root=LABEL=cloudimg-rootfs ro console=tty1 console=ttyS0
[...]
```

The dump come from a linux machine with kernel version `4.19.0-9-amd64`, next we need to identify which linux was installed:

```
$ strings dump.raw | grep "Linux version"
[...]
Linux version 4.15.0-66-generic (buildd@lgw01-amd64-044) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)) #75-Ubuntu SMP Tue Oct 1 05:24:09 UTC 2019 (Ubuntu 4.15.0-66.75-generic 4.15.18)
Linux version 4.15.0-66-generic (buildd@lgw01-amd64-044) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)) #75-Ubuntu SMP Tue Oct 1 05:24:09 UTC 2019 (Ubuntu 4.15.0-66.75-generic 4.15.18)
[...]
```

The distribution installed is `Ubuntu 18.04.1 amd64` with the kernel version `4.15.0-66-generic`

Now we need to install `Ubuntu 18.04.1 amd64` (http://old-releases.ubuntu.com/releases/18.04.1/) with the kernel version `4.15.0-66-generic`

After installing the iso on a virtual machine, we check if the kernel installed by default is the same as that of the dump:
```
$ uname -r
4.15.0-20-generic
```

The kernel isn't the same, so we need to install a new kernel:

```
$ sudo apt install linux-image-4.15.0-66-generic
$ sudo apt install linux-headers-4.15.0-66-generic
$ sudo reboot
...
$ uname -r
4.15.0-66-generic
```

Then, we make volatility profile:
```
$ sudo apt install build-essential git dwarfdump
$ git clone --depth=1 https://github.com/volatilityfoundation/volatility
$ cd volatility/tools/linux
$ make
$ sudo zip Ubuntu1804.zip module.dwarf /boot/System.map-4.15.0-66-generic
```

Before analyzing the dump with the application, the profile file [Ubuntu1804.zip](Forensic/Ubuntu1804.zip) must be put in the folder `volatility/plugins/overlays/linux` and check if the profile is well detected:

```
$ vol.py --info | grep Ubuntu
Volatility Foundation Volatility Framework 2.6.1
LinuxUbuntu1804x64    - A Profile for Linux Ubuntu1804 x64
```

After trying many things, we realize that there are flag.txt files:

```
$ vol.py -f dump.raw --profile=LinuxUbuntu1804x64 linux_enumerate_files | grep flag
Volatility Foundation Volatility Framework 2.6.1
0xffff95a89ac72260                     22114 /mnt/confidential/flag.txt
0xffff95a89bcf3c80                     11530 /sys/kernel/debug/block/loop7/hctx0/flags
0xffff95a89bceb560                     11498 /sys/kernel/debug/block/loop6/hctx0/flags
0xffff95a89bce6720                     11466 /sys/kernel/debug/block/loop5/hctx0/flags
0xffff95a89bce2980                     11434 /sys/kernel/debug/block/loop4/hctx0/flags
0xffff95a89bcdd7c0                     11402 /sys/kernel/debug/block/loop3/hctx0/flags
0xffff95a89bcd90a0                     11370 /sys/kernel/debug/block/loop2/hctx0/flags
0xffff95a89bcd2980                     11338 /sys/kernel/debug/block/loop1/hctx0/flags
0xffff95a89bcaf0a0                     11306 /sys/kernel/debug/block/loop0/hctx0/flags
0xffff95a89ac75560                         2 /vagrant/flag.txt
```

So we extract them:

```
$ vol.py -f dump.raw --profile=LinuxUbuntu1804x64 linux_find_file -i 0xffff95a89ac72260 -O flag1.txt
$ vol.py -f dump.raw --profile=LinuxUbuntu1804x64 linux_find_file -i 0xffff95a89ac75560 -O flag2.txt
```

And in the file `/mnt/confidential/flag.txt`, we find the flag:

```
$ cat flag1.txt
C0D3N4M34P011011
$ cat flag2.txt
```

The flag is: `C0D3N4M34P011011`
