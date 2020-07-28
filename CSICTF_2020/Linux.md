# Linux

## AKA
```
Cows are following me everywhere I go. Help, I'm trapped!

nc chall.csivit.com 30611
```

We are stuck in a shell and some commands are disallowed:

```
$ nc chall.csivit.com 30611
user @ csictf: $ 
ls
 ________________________________________
/ Don't look at me, I'm just here to say \
\ moo.                                   /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
user @ csictf: $ 
echo test
test
```

Bash function is allowed, bingo !

```
user @ csictf: $ 
bash
ls
flag.txt
script.sh
start.sh
cat flag.txt
csictf{1_4m_cl4rk3_k3nt}
```

In fact some functions are just rewrites with aliases

In `start.sh` there is:
``` bash
#! /bin/sh

cd /ctf
/bin/bash script.sh  
```
And in `script.sh`:
``` bash
shopt -s expand_aliases
alias cat="cowsay Don\'t look at me, I\'m just here to say moo."
alias ls="cowsay Don\'t look at me, I\'m just here to say moo."
alias grep="cowsay Don\'t look at me, I\'m just here to say moo."
alias awk="cowsay Don\'t look at me, I\'m just here to say moo."
alias pwd="cowsay Don\'t look at me, I\'m just here to say moo."
alias cd="cowsay Don\'t look at me, I\'m just here to say moo."
alias head="cowsay Don\'t look at me, I\'m just here to say moo."
alias tail="cowsay Don\'t look at me, I\'m just here to say moo."
alias less="cowsay Don\'t look at me, I\'m just here to say moo."
alias more="cowsay Don\'t look at me, I\'m just here to say moo."
alias sed="cowsay Don\'t look at me, I\'m just here to say moo."
alias find="cowsay Don\'t look at me, I\'m just here to say moo."
alias awk="cowsay Don\'t look at me, I\'m just here to say moo."

while :
do
    echo "user @ csictf: $ "
    read input
    eval $input 2>/dev/null
done
```

The flag is: `csictf{1_4m_cl4rk3_k3nt}`

## find32
```
I should have really named my files better. I thought I've hidden the flag, now I can't find it myself. (Wrap your flag in csictf{})

ssh user1@chall.csivit.com -p 30630 Password is find32
```

On server, there is many files:

```
$ ls
02KG7GI3  3E7ZTAVL  5HQTP051  82R7NE45	A8DWWULS  CYNFLG1O  FUF4GEJ2  IUKF08Y4	KRNKFQTK  M6MO9M1W  OAVKKSIU  Q3VV2P04	T0ST0WFT  VOAZ2FLA  XM6M6XV3
02M95EZJ  3FSO4YLX  5OWRFEZT  84XR0NUK	A9ARPBTE  D01U0OA5  G18VV3XH  IW0M1T97	KRTDDSYK  M8XE7P73  OB0TZRYT  QBZ2NYYY	T5D06H6O  VQHX8Y2S  XVXM67UN
041Q5VQ6  3MPI6ZGG  5S7QF3H6  89JKXHMI	AK1L1RB0  DC953402  G20VWPOJ  IXLBEBRX	KTE9QN31  MAC4PGYS  OHGWT0IT  QDDZKQBI	THW3C7CC  VS2QLP5T  XZ5KZZPR
0K8HTQUI  3NI0KD8T  5ZCQW7TK  8AYM8OQ9	AK6PZX3H  DHI6XKWG  G4DRQMVC  IYLAWPCR	KUNZ9OP2  MDZE1NQC  OI290XGJ  QDZM9GU3	TIE17JV7  VS5RKUTC  Y0WAA0QK
0L51GUQ6  3O7SZPP5  66SLWGGM  8BHHDOCA	AL2HOE1I  DQZAE7MY  GBIA0FJJ  IYT9TNZ3	L25P2X6S  MIN0CJNB  OJTT5YOZ  QON3WELD	TNGM39LQ  VU7UXE91  Y2F5YYPT
0POE7NLS  3SF18NHO  6IGISUOK  8DCJBGN8	ATP6Z1LV  DVRULQ4L  GCCH7GUL  J634H910	L6RJI5MH  MITS1KT3  OLHQ2XMI  QV763DK6	TNNLXAMK  VUU3IP28  Y41T1L0P
0XC8TJL6  3WJNQHOI  6IS45I48  8O23G30S	AYHI7FZG  E2DCKTAW  GGK14ZEP  J9K0N1G3	L97LN1SA  MLNCZNJH  OM4BZRJ6  QXKDIR8P	TOD5ZOWV  VWXNPY8W  YB6CGUEN
10KS7XSL  3Y6ULSYJ  6JFHFM48  8Q8IDTC7	AZBQ6DI4  E2WWNK1U  GN72VYNY  JBNLA5LS	L9HIBPO9  MLRX5NHC  OO08I86R  QYBFIDQA	TP72DLYC  VYXH92ZI  YGAD81HL
17HSIYXQ  40HE4X61  6JJ8M6EQ  8SQP2JFV	AZF6YNNW  E3VMO1UV  GVAUVIPU  JCUBGZ0L	L9NCYUOA  MT0ZF01M  OPTKWTEN  QYKLAVOR	TQYI4JH2  W569XUGK  YI5ISTTI
1DB6A3RZ  41W0HO2L  6KPKMW7F  90ORMN66	BAL0FX4Y  EBGAB2T7  GVTHMJMC  JD8K3921	LA28D194  MVYJ08ZU  OTQLM9FR  QZBKI0LI	TY2N5W2V  W56UYZUK  YI9VPU71
1EBY9SNN  4DXWEUAK  6NZ8YTHN  931P2T2C	BDMSPZFU  EDL1IX5Y  H782K0GF  JDVT05Q1	LB4B6X6P  MWE4SJWL  OVB0C2DD  R3O1QJRE	TZ4TM4KC  W7N3EQ8A  YJ4H3LH9
1TE2UPR9  4E5VZT6C  6O893R7P  95NBR36B	BDYM2DL3  EJKM4P8J  H7PWE6D1  JL8V5YGI	LDMDGEL4  N56AGDMY  OXNCWNKP  R513RF7X	U1HE6HJU  W8XHJP69  YJPL7KY5
1VQPZIUO  4FMGJMPX  6TQAQ9JL  99KWRIDG	BH13PMF2  EMAPY1SV  HI1HXC9E  JM035B27	LF6NHZRK  N8O0W1UR  P7U25CJI  R75LDKZA	U1Z144SU  WFLCEXOU  YLTYQ7PT
1W6RAWEU  4LMTFZCM  6Y96J42D  9EO10QRH	BP1QOD2S  EMOTUDML  HJ7SLXWJ  JMXU733Y	LIVI4VP2  N9ZX32OP  P7ZSATBS  RHZ4QIGE	U4CT6S3M  WHYUOJS2  YZOFT123
21X763CW  4LYTO0ZG  71PCO4II  9KHTQSOG	BRKQC7KI  EPIGX1NO  HKX85U5A  JNTGVLSL	LKLQLQ8B  NDR9IE07  P8H2QJZE  RSA9B4XA	U9KXZUZT  WO7DKKIR  Z8TPG2SQ
24CHFLCM  4NE1DLAV  74EIPRM5  9KQEWTD4	BT4Q0KSC  EUXTE3IX  HL9OQ59W  JQJIA3QC	LKUM0ZLZ  NGT5TVLI  PBMIEOJ1  RXHHGT3D	UFF3VJES  WQYZVZ02  ZE0LYP1J
24UQMOA7  4O0KVR5P  784MLE5E  9KVDBM8O	BUIYBJW6  EXVHNHYF  HTFON23U  JSWT0A61	LP29J6MU  NJJ4FIMD  PF2KOY3A  RYRXFTD0	UFRWO7LV  WW5L7JNK  ZIIFJZRE
2FFS4207  4UOCNFI8  79VJFIU5  9LNZ0ETP	BW90182E  EYN874N3  HW9ZGUI0  JW5DHBI2	LQWDHMT1  NMMNMEDT  PJU5YNCE  S3CQF12S	UI3CYXEH  WXW4GEDU  ZKOYMDBL
2L9WVOQA  4VTQDZXG  7EA2V52Y  9MP89P4E	BZE1NCWY  F4K726ZE  HWR8ILW8  JYP14B13	LR9H9RJ4  NNGY3F51  PKEIXGTL  S50ORS2M	UK268DBR  X1SVRUTM  ZOM1L6RA
2MMNROKS  526KAB1Q  7IKIFVQC  9QNUXM4L	C1KDRW2G  F5FFWSP3  I0GJ1ZT2  K5HIYP7U	LS1E6E8N  NQ3BFZKH  PLE8FFL4  S9796BM8	UMVACDSG  X23268R9  ZUIZ3BRS
2X82259Q  5669QKVZ  7JKVQ1V4  9R6FWLZQ	C5L2LOAA  F9T58X71  I0HK3F0Q  K7H88QI2	M0ODDGTQ  NTIJFZDS  PM7NRHP0  SA13FEFE	UOKCOUPN  X44EBTIV  ZXWG1CJB
31H6U39X  5714I59N  7K2HS4Y8  9SMDHC89	C75ZYB8Q  FH0FGQU9  I3QH2SGS  K80WPMFB	M2D9A9GW  NWAG08DF  PMWQY71J  SGCS15D7	USP8NX9I  X4O9C3E9  ZYSF9F0A
32DJSRCD  5D8MSKXV  7O0E74NI  9TM8NR4D	C7LAWJCM  FI9WZ1NI  I7BE5SNQ  K8670JAD	M2W3FH21  NXH2E4FB  PN7VNWMY  SSNMEO7G	UTNI6PSD  X70F203P
36VMK9BG  5DNAUH8Z  7QQAKH41  9UGJX4Z2	C9EN38OZ  FJATAT6I  I7BYYSUH  KDT49C2O	M40WA6L0  O08K936H  PRIT98R2  ST1FTYFZ	V8A4PPEG  XA6HG1VW
3B2F652L  5DY1KZDZ  7UB67288  9X0BSFFX	CB7VL2AM  FMZXZWMD  IHGA1LHQ  KJ26BDR0	M45WG887  O20W8JF2  PUKTT71A  STYTHKQE	VCSYBT6V  XAGJI6C3
3C71HLAH  5E0OD9MJ  7UYWYDBZ  9YN7B5TM	CR8AY5W7  FOGK2TD9  INUIDPFZ  KOIIQDDB	M4PSP87C  O8C1K8CS  PX7XX8MV  SWD8ZKVQ	VFFKFKFP  XBJ59Z81
3CWSG1VM  5FOOLY10  80TD6MQ1  A202VRDJ	CVDGAH14  FPLW13DY  ISW6FLPB  KQFVQJ3J	M50MK22L  OA9OWQNN  PXR9X9H1  SXRZ25DU	VL8QUY6U  XESS84R7
```

We try to grep the flag:
```
$ grep -R csictf
MITS1KT3:UY2HW2WIYX3EB5E4BKRMS2YHBKT82MVPUISKZFNOWYXQUHMD33CJNPWIFDKOI7IPFBESU2HLNZ4EH6CJCNWYO6WM5E5RDI1Q89HQFIHR1EM4VFN451F0RD448XEA637K7YFLXQ9TKPINU9R4CUJE2GQD93K1A0P14WJGL9J8YQRQFEDA2NMD5IUXBQ2MPZFVPS665APY55DIXS48PQ40TUYMUPU30DQ2RABAZVSRX3RVOHH5SBDJAE0GN1J0MHQVFH69S0ASF76HKH6YQF51QSZD378VK5YOHR3G9KUYK3M5GXSK9W4JENVTI4MU2FZHMJ2R10YS9FNZ9PAS0BH198OYW8ENEJEF6816QJ8AJGNOEYS4MSL2CZ6O07LGMEVM12HVDNEUT9PA9NY23JDSF7AIMOG0BQ5CDVFNQGYCJGDGZO2YAP3JVIFYFGCJ2K58XXQZNL1D8NW8BESVKZC4UST3CMN1TVVFID30X7HNCPXTWHWLO0LGZURH50M444SPMA2IZR2SKM1EPTP2F1IMW0IQGJWE3T3J68883UEHDG2CC2YFZ2WQM45J0E3J1HX6NS2N69GOKZUT2JSYTN7YRZNTILR0LMTAPCZJMPXU6MH2A6PGVLAQXGWD6QDWE7PT6J0TAAYTJS8VLCQ1767F2OOWSX9RJRDL7P17XN0F7UCFUNYNI47G4YZAXP6FLKQC4WKZ09JLVTNBER63BQIWX75FA6POEZ014NF3S3RZHG2R9WXOHGBJI67XX83HYKDFKOORYPD1VMOZQ11PHX3E301U0C4Y74SSY9N1EC0JJQBDMAQ82NE2NQDDH4UG8P5A587B548S7LA7HZYB0FMJHLHY3VV5PITD722ZIY61B8O7OYBBZRXWV5VP6Z1EQACN6GD0OVFCE4K1SRGQPZR736995PS5NOLSCH3HXPY75VXUS74HJYMFK4U06F274ZURG5Q48W29989DER4XHDTX8V9OYQUKTIHI7ZFRWSXXASMXGDCNKHX6YPYAN9GWXEWC8FRS61UAVF8QIASIHT9M4443DP8N86OOAXWJUZX1R4TNYC7J7EZRQKV4S4OAHXGT1G86C4AKGGHT5R0QPSB2V92830R70RMRJ3GJO1SRKPOR2Q84JRW0B8AIT6HLZFFE1MEP9JJWXB55AU2W7AJGY5287QJUYG75MQ2MF0MOVC95F7Q7ECOG4U01QC3JCH7NDYVY4JNXTO42FWIMKKGI63OIIKIG31KTMJQOH0LMUGVOVKC3A8IA7BV505M1171C7TG5Q56QVUNV6TSEAOYUC49RP2GZ43FFN9M91M03LLF9FMZPQSAKEAQJGLEDB9D8K2A2BNR1TPQH7DDSY9I8ECZ86KLSB3P1WRPYO89A2H4IDPFKTOKCFGT1QPC7YVWQW1XRD5QCUOXC9OOHZ5KOGN1FVBG3ZYM3M8LMWCDBY4YUELUSAXL6YQB4JGJNGHPBONQSSTRQJTUGHDMHOVDNU8ZYZBLG7NR456SEXVKEJE4ZN61S8B40CG65YB8QCHHCSIDCUHY220PGRX620UI990D1MOPSBTZYTARLS1IBG7JOPYDG2PN041532CBHFQZ6L4YQ9PNJ7XGSTLO6U7H9C6PN2RQQK8AZVS7ABCMBSU37U7RWT515908D9FEA956ATLQWKNWO2E13EK23QRTK72BFTFAA18XBOVEA544IIYT8R1SNSZDHYSRB3ZXKB8UJC2TN5H7FOUGULPJTJNL4UA3VWM6IVHUKFV9VY9VGP9USC6TJVVQ7DKT62NFN9ODPK44GQU5XW2DYOYLJT3YIF0IX2LDO3IVHAQOLSVDTV0B2IT6OR31CFETD13F7EA1KXTW1TKZJ2A2EVTHPVAKQ63GB2NMS2SKVKV6TQG0SD96CCMVT68F642T548O8GIWHFN68QQ9DSC376X5GEGUR28I4NZUSA2VWSWRZZRLKS3TU8VHSQOY19HPWQYWMZPSY7KSR5TI10OYJIGE3VO26D803CVK40BLHNMIGGBKISLCLZOGV23GDTWN7LVMV59V3W5F77DAB1ZJYF71TID2OW1BEMM15CXP9U8FFOTW03BQWTV8HSBN1830FL6ADCB0Z6FVO3XQH6B812XZTP2398D6XTT5VQ3ZGVDVEX4EUPXJJN9IQ8VB8EH4ADQICAUCBO958M6XKI01ETKI7V6AIRY6KA99YY0NN3Z99HPVNCBN82COOWPV6M1LZR4Y35LV0YQWEHNP15K0S42MM2V0GVVPY2QKXLPVLL9SATV3XB173OPQX7O0KMWI30BIEWYUZREHMBCPU3081S1VPZPCWRTGVZ084X3CWKP0CN6SWZKJW7T4TVGRQ9EWKZE6N3S3HF3RY06CZ20FFO8NCNWHEATZ8LQW9DA6BT8D0ZRG74GGAN69S51HOGBXRICMRG0L5QGV0CAQE36RIYODDZFGAIYSUT0LSBXSVNN9EJWZCK6QVYJNTDIIAJZOMBBVU92487MVRSKCGGVA08I7Y1BQ6JP7HM5CO15DZ6MX11CDJ8OOXJT6VWYWAYPH5ZLA5M10DL7FEP61I75LDQLVPDQ5CSUPJ1LO8OM4FN34GXWORQDJMU2UE21X0Y2JQLR11BXAAIW49WNZKAQTV7SKOJN53L1QL0VP8DYX4ZVBKG6QIG87G9PWTGB0LQC0NLFBP1XSQB4SU5VAA8QHM60U2XK8GBY671I7BNCS8A1MUT22ZGGIUJYN9VTXLDR85BACN0YK6JWEQJEYDZ5CZHMQN5I0XX6T6UK9CRPOURQPP9I2VJ2H3VWIIGRU594UU58O2H45Q3HUXRFS4FXJVAX0OIRGO46O879763E3UWXCBTOKN8SNT71V2TTH1RGCEGOOVTQTBMB9VTVHLRNT7C44V37MUHCMKQBPNML8GAK7LU1U0DRFX9HX1JBOR4XKOX37ES9YRNYQIC0YXI99DU4X5ZMTXJSUW7IZ2GC77DSZYUZ8OLYGTZ5C70KWROCOCD7DZMTM2KDBY7B4VN93CANQM7VG1MA8ZS2Z1RU1558OPJ913JCZAPJYAV6JHIUQ4ZHV254OJIBTOM1VM0RWTTYAICCNQMW2SC21E5PYNTB2FC7ANC14ZHQO2WU8J2HZWZ0PLI6GD778FN63Z3XEOD9Q0RUVPKHAALDE4G0RVFOLXNG9II91K9H8W3E6GTS2KTNXYD46AX4KEUVTU4ERXQ6ZMF74L7BQO5H0AU1HJ9NFVINPUOWFIU6H659140G03G9I7PTZB21O4S0PJ8SJ96DMQOE6MRHDZYG19S1CVURD2J9FF9RG1CVBJRXC5UWRYN6Q7DKB95BJRO6WQX5PTB96NANLZK6NPD6TPNDGI14QZXWCXQI0FNK5E8514PJ08I789R6P6634MUN08HZPK92W3HTPMQL4GUP48OEQPW7AHUQLXAX6QMJXISRSAX2IR75LS816FTX92UPUT7KKZRLT2EY9RQPFXIIK8PL5XDMLVMX6CC9EE8Y7QA7LUO5PKUQ1P28IHL8LGBDTAZZO5Y80WD2LOZ3CPEO4A006LM8HYTZ6MTR4J7AKJTQ2HI76BZ4UOWOCL4SVM4BZFNSTHRUX7YT9B8D4HXSW8Y67OOGRZMNSOFX7WI99SN1RQQ8BOEWS655PTNEE8ERKV6VI6P1YSRNEJDZAGSHFLX4XNZ9FMK9ODW9BP3IRZH2QF6VUPPPJROS33X2M8G7N3HXP4IFBQOC07OOTQF2D2D4I81761RV3JTJG93WU88BJXEXLNIRFU9Q6G71M954K6SAA0S70Z2VQFCQBX0UHY5MY2SX32CH1O2YP0XB4Z8EGR3ZQHNZDXLDD618GT1A5F5DIQ7EAOU0BPXYV0VUZ2W30QHGVMLYWG9YIU9XE2JND6KOODIHBQNXWGRFY4ABO07KLP3J6N3WS1M50KCGEZ9FPQSHJBUZNT4QOM07TVZ43FRXXTPMPIWRKYSPJWU2BJL04KJ3ITZVTHBQM9J9OWVX8csictf{not_the_flag}{user2:AAE976A5232713355D58584CFE5A5}WOQS75G7TVPTTN3RBXGK96HGINKCRZ1Z8JP6N44KC02C9E8QWWTA2HW61CHPMKIZEZ6MYFR7N2WKVK93G5NBFEYYIGLUVXWK8NB3OZ06NLJVLRL6AXEXCYV6Z00CMPDPA7TU0G2CCRI5XNEEZQ79ZKC8B9WF0R79KX5X0EO0SVR8DLK7A5E4ZUO0A4ZYSP3DMENRTSIYRBP77ENRO94R3YWYGV154YX23Z6GY9V4U1ARL3PDFU6XO9RZOLJEJ1XXRR97HRV6TBSITPQ563V7GAAQSAPVY01KD8OSOQ1A78NJN0U4LRQN2ONQ0RTNO51W3227SH1BRGKC1SF9J8N72PMYIKMNJLE1XIH36AR3XU22NRTBTWOKEL9S1JT0THW0YF8MGC22RUERM34LLBI6B0EVMZKTE231NH9LTJBMKIABUXQ9CVZWTGIM2PFUNDFZVJSG14WO8W5FCJ1G6H1VXM1HP8Z92LY98JSYW2WDTHZVWF2AWZGTIY3OIOK0SEVIUOZT1Z41QS0C3W7FTRJEOZ3V3NDY517A48030C1362BNZHSZXYOF1CMANHQ408M9FF5R2Z9HC5BCDSKFLHAB3YFJ414WXCIOSPSY18323WYJL2FG0JHJA1ULW3M1KB4VXNWOV6MYU5YV88WJ8L03OO6738R50LI8XKHFR0TDVSFNEVRG95LBPMNUMRLP315YU6JMK4H5IF4B1P4N1J5YATTL6FFU9EMH99XUPEWXHH8TOZ4LBEFKGBS0LJMBRA6HULPB147O4DWNUALAOYY3VTXEUUT6CQL48PBB65AOU88UXDS5GHANP9A2XKF1MRRFTHJWLNEP3TMSK61ETIY82OS6GRYFQ5A6PXAVIWCSNT1H5CBBBDP9E2UOEVQBOOI2U27RQY4UU5QEY6GX75E72RO7RYESFMQR14LT1IS605XI4J5U7TYZN6NCIN2HH2WWUQ7DVWYPAGG3OZWHS3XE2LYT7N23WBN06S1RHR2I2A213US00MU6RDLCL194VL6221A6GS7XYFDSXPZQ458LVL1MCKTGV44OLC1LPLHTNRYKTXMDEM640I97STPIRPQ2OHCI3J6I6DL14FTJ1NWUV2U0V0GSW3TVUEUKXATKLU4DVFMPP1P8WLC1PSOM4ZMN6425OO27WSDU0QGWYRJDP90CCDIE2PFI212HBL7VSPQGA6L5V25JC6G3SHAD54GZYPB068DKLMQR5O6R950KV7VRATX628KS2SIS2QOF7RLF8GLGDA1HNL0UQ5FA7375ZR009M6NXQSS96JYJ7LU5T0K9S18MSMUC63O1200JCR8C9LPAGGAL3VTWKM1FEAH1KNJCUYKY61I7MTDSJG4KHKZD6ULTT4VAKH70S9QJL99YL9KKG7IEDHUNKE4TB7LH6NJW66LGU4EETSV3GOO82S2EJQ747UX1XNU5PVH1P98TUSI3D8VY4677VBHPYSBXVOKO1VYQ1DMGZ28W1ST70L7VJZ7EA2XZYNPHYK5G38AZ1JTLKADAFHIV69SGWGXDRD95SGC2TDSRC696QPSVLIC58SGBOUYWGXDK9OWL99T8H23KBSALFEHA0U275LJG86R6W3R2V2TRGUM3VAANU0ZRV87IPHT7YE47OXI4UIDTL16501WZA0TYYLHJ6QW1QNLJF1J9ABNG6FYUE6BPMRQSDGCKSYQZU2606NOVBN5527BOBBZYEN21UFSR78CKSDJ33FE8EOM48NLKY8NDGSBI6S98CJ0CP31S2C904DKSAHXW53LMG5MQQDGSPWUINDH6KE58HY0WWY2L5FF5SM7F91QAWUKCR89VN60GQDUDFQJA4BUH9IRC62LYT0U5GV9V3RCQ5JJXSF5UOP3SYFWM83AWXHU2YWO2AF7MTX72OXETJGI97BC3CLOF14Z4EEAB65QDFWEZNXUJR9ME3L636AJUDA5454C8J8O2YX3AS6DC9H9GL61CHAWODSP6VR0KKB5VF1KO7VXJ79DRATCORP792OU0WTN2R1QNSQ3Z11GD3QTWAC07V7WHDYZ5AQ46YQYO3G8VXMHBV0CHSUHGB7NHLR83ONUC5AL9C5ETLAW050TLRWI9Q7JLHI0DDJFXRUEAIBA6GKFZ7KLJEOMWDAEF17B1L48WVLBDXGHLMS11153WJ6VQDQUAGYSS5P7I2ZC9LOEP5CB705B3T6U6BF4PZ2HTILN4X0T08YRFYRNCCBTZ6KZUYGIRLBKCLY47O6G07PI59OY2IH3FSH3GIPNLSVPJWYLR9FPL0THPTQE362JJNW3VXVE0CPQ49GRV65I2H68KF2EN5VVOEKZY9F5X4FUFQ6M8CFLJEMYU3CZOTPV7I579OI2UPBE8VWDTLGXY06LAA5K969EBP2GVF9AXFEU6S86ZE3C9OTJS99NDGNRXX2C1M5J39DF145L5OW1NEDMGBCDVYA9C5RS54H0K3XGU1AKRI2VCCX5MI56BW6AGGSPMKSDH6D00OD49U0O3BOIF9Y5J95ATGBKUKWTKE7J7PW4LTONO5Y50DAAHGYSQAUPCP2GIKGOSPEM84K68PYA117FT54FDAB1251BK34OX92TVU8IVN8MRGC40BDQDAJ8Z0RJKPCM96FF1XF2XFAWDM9MTRVRPAZ0MFNKA8JRLM318U6IYYLV4D7ZV77AA2SSG1IJ296WE1D4ZB5E4BTNQHPKAU4K732ELAI2TZ7MXOWOIILLM21OVCH4F0F34X8HM06EKDNPJX1CKKGE4E2ZCQTH8XQLCPVYHGKWY350VX5SPKN8GJP9ENOAWT1TVTJURJMB3B20EZXIJP3JPK0K4Q4QX45HWCPS0S8FQ55W99R0868Y02LKHG1BI2BLG7DGXBVUP0IEO45JFI407Y40F4DUSEQZ5E0T3Y4HYMRAMN1E0AYV5ZUYU0W51APTDK6WT9QU8X845YK8VLTC7ZI1H8EAZBVLLRFWO5UL94Y85SV2PO5298725IT49NHOUUVEVW4LTL2Z0E4OC184QVKDW8MGWYWWTO7V2G4NFRCO22EYRPNF3OGD118E8SD3GGGB0UT0Q6WOGCTJWZXG5P8VBFEBL1T6HAJQKECOEXG82R84WBA8HAEXW4RW9RPQ5C1FU0KT78VTRSYHLPR9KZZ8HO28LWTU78A69TGHIV87YJJQFYM6MOL2QEVIHWTYQARVTUF6WDQQMC04S2LN66L6X99IIF5E2KD3THBAZLD9QBBTLWVY8TXDL81D1FBL0WMIHT0PIMZ5CSHP7EADOVRPLMPXGADUH6VMJTPTQ4P7F48QEJCY4S7EQS20E6N6L7UY1VI9LEWUDP3O5PAAKKFVTMT7Q40XGFEHSG01OMPX3JDVFV9U73Y6J7AKCTDEKOYEJ38NSAD5ULXJ1LYQ4FNO10QZVLK75NONJK8J0GPEH7DKGMIAW9I43JVUUF5OY3T7X4TMS789LQZDZHFCASPHSTASYM6RS3CTCYQYL3123IAZRDOR8PB6DXU2MTN8PMYKSGA6NRNXY5CW4YISFO7715OEID2XQYDW29L8EFXICBRO5TJ6YJ4KE47B09T2T3Y55FPO3L36SPT6G8TO39I7PUYPD4TA8QCEUTPQCPFBWH80FP6BVT78DWS5EIM9EKJ6EIL8J8NCOKTGGW0ND8M9LZK0Q92CBBRWWWS4E9XJNDM8BETVC1S27TI3CV1FQ28UYRW5WFTX0VHJ8Z9QCV7E8YPTK7DTEWLZ85C3NY1SKH9E6ZKBM6J7GEV3WFX75CXZ3IY76YJYF4MQ0V83739331MJ29KYRO3X76IU7T43RD7ZSARPRBZH76X35NN2GZNCXDU5126XX5XQXNZ7AVTL69GSCTT8ISRAMYET943NUJ5I7THFAMVH7TU3AT4NNEXD7IWFW844ARZLWQRCRAH020WL3MZMBQ2WY2XULOBWZ7AJESFAWJXOE6D7120GEZY2Z0WNMSKE1B6C5ZHOVWSU38CY9YTVJFQMIOWJ23ISYTD5YVE1GE0SXELQ6S7EUY5APOMCR5N6ZGLLOMA749VBCMHM7WDWFIS6KOC1BQQEZG70X46JQGQMEDE1TQ3HJ4LIY3OAVBB5Z8EQVWMRVC176RLKIG49TJTFRGTT8WL4DSM42D50I0R6764MRPUM65AXS5ZRITVVH8RR0KD75N537DO97HJYPFH84MEKJZ32UY4GUSFX7A9MQ20IY6ZWFD1JRHVY1EDWUQVU40Q54CGAWK07AYFAQTPA8RBFRDTNC8UF55IGHX2S63PYI6H2128K2EA65H84A10J8CRHMXLCGGZQG95VBTS3SG6ODQYLG0G42OF42LUOZABQ70NU5XDXRTORBPZIVL7CO5WXGE01JKXPLH0K2HN98GIQAGG9UMA8XO7XK8RBTODH1RMRJ5DEB82LF7VSS4LD9SL7QCHUJDKF13QYTEO3GGFZD2Y0IKGVIDFBWCLCB2WBIV94YHD1MWSZV4GBLEZ7AFC465FEC5S44BHEN3ATN7Z6GFKMMRTAH3BEE7LPMWEY8B6KZL4DTXUFF81G4SYVE9U8RL0Y3YRZ607VYR4QL1EUEP3S2X6RIZETDZ5ZSIK1SVIKS6YPNQYSAGZP4BEBJ63ITIC72IWLNNHYQ9WFD6R6CV2MBDDR74F5KF3TMCLOBIM44QGYB6465Y23O93DLTBJB0VNVDGLCSQ223CIYOJX3FRNMNEKR8MXKFLKCDGPVF129N3LNMJUVHYF7DOEJLG6NG1K123FNMV1NQECX3HHEXYVERK4F06IAC8RINFSG32MF1N8VYOASR9HAWN6ET11ARF0LL8H9PVV7EVGFCFEEHCYPEGTYVHWZMYFZUJXO7GI3ZTZ0VMI6KOQP8VB72EUBZA5WFJIOHTHIXQQTVJYT0ZVKWVTUK9Q8NA1RBN1C5BZHFZSW53PLO297M6UM8JHL9KEUN3MB3CMMJ2ADJAZTRK4K2OEMQEZN1NYKMLSJYYU3WXB8OO27TCTIKIQJQ8XI5M8OG73U4H6RQ92MCXD8XKFTAEY2CZW7DVU8B2QVD0MG70QV8QI21XR9HY0CYCL0XT4MH34KLENSMBNFFNOXP4DX7RJI7SMPKIRD0ONTR8Z3KQXD606TXNOEK0AB96ABTH4OO2CZ56IXUMWDWDRMX21QHCL3BEOADWGOJKU08D4WCRWZT88CZ8KC4J0L1T1ZEAHM0MREZ5ZU9WX7E9K7USHZMKNN6F6OQ92MU63ZGB78RH62HAF6T68NH2ZM4CLB0GE6TN3M78A745JTNDDEP8ZKUHXZ17F855AK8DRIE6AL8SEOX88MU1R7Y3SFLCX9P16UBZMR2TGIZRRGHGU64WPMMZRAOSD5QI0VE4MSVYJDYPK4JZAWSWOUQNCWMU0RLZ219PXRK0TYMPKYU3UOASQJYPHE7V1Y25TJ11DD9E7TLSHSF6XJEKID1AGL94OM9N4H4HI6OFZBL95POIAXFZ1K3P9BV9AS5761EQWH7BCHCIPA7D1GXJOFRTWI44F9MRTR2WJ2ZIABUZFCIARRGZDY06RQVSB5PITZL55TRO9P02ALLRWHYKPBARZ2PNN874U91VRKON96MRT0TF0T0UNR93F2EVXY1M5GV3V6O71UUXYGT0JRFKZI478QYSJKLF9YJ2F1WX65MWBG4BV6YJUCEB8T1KJ8BAGBI3ZYGV9BDRHHT0P3NHLMTB7MVWSU3QS7V4W57TQ7P2JONE4OBQ2LS5ZXA9GUMWSUN6ERSHUHKBVYBQMKP34UF83TSNTXOJEMKO5Q56ZL8AATQHO9WTBFCLEEEUJCAJH5KAAR0BDRN8Q43W09TAMVN8M7SHXVLOG4HQEUILN47C6PQP975JAUBA4HAWQ1PUJCB5WIUJ16AN0FRTVI58VA3QZQ448MZG8616FV6WJZ6GLU3LEIZ44GENU4UERNA70NAYVR1UEEB9Y9Z36L7MWWNBMCHFSGJYU0QX5E8RP4ALXWNBBWXKHYKSA66QT4J0RD6L8N
```

We can read `csictf{not_the_flag}{user2:AAE976A5232713355D58584CFE5A5}`

We reconnect with the user2 login and we get some other files:
```
$ ls
adgsfdgasf.d  fadf.x  janfjdkn.txt  notflag.txt  sadsas.tx
```

We try a grep with `_`, as most flags have one:
```
$ grep -R _
sadsas.tx:th15_15_unu5u41
```

The flag is `csictf{th15_15_unu5u41}`
