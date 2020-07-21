# Web

## Cascade
```
Welcome to csictf.

http://chall.csivit.com:30203
```

We are on a basic website, no `robots.txt`, but in `static/style.css` there is:
``` css
body {
    background-color: purple;
    text-align: center;
    display: flex;
    align-items: center;
    flex-direction: column;
}

h1, div, a {
    /* csictf{w3lc0me_t0_csictf} */
    color: white;
    font-size: 3rem;
}
```

The flag is: `csictf{w3lc0me_t0_csictf}`

## Oreo
```
My nephew is a fussy eater and is only willing to eat chocolate oreo. Any other flavour and he throws a tantrum.

http://chall.csivit.com:30243
```

On the website we still have the message `My nephew is a fussy eater and is only willing to eat chocolate oreo. Any other flavour and he throws a tantrum.`

We also have a cookie `flavour` with value `c3RyYXdiZXJyeQ==`

`c3RyYXdiZXJyeQ==` is `strawberry` in base64

We encode `chocolate` in base64 (`Y2hvY29sYXRl`), put it in value of the cookie `flavour` and refresh the page, the flag is show !

The flag is: `csictf{1ick_twi5t_dunk}`

## Warm Up
```
If you know, you know; otherwise you might waste a lot of time.

http://chall.csivit.com:30272
```

On website we have the source code of `index.php`:

``` php
 <?php

if (isset($_GET['hash'])) {
    if ($_GET['hash'] === "10932435112") {
        die('Not so easy mate.');
    }

    $hash = sha1($_GET['hash']);
    $target = sha1(10932435112);
    if($hash == $target) {
        include('flag.php');
        print $flag;
    } else {
        print "csictf{loser}";
    }
} else {
    show_source(__FILE__);
}

?>
```

Sha1 of `10932435112` is `0e07766915004133176347055865026311692244`

The comparaison `if($hash == $target)` is vulnerable because it is not a strict comparaison with `===`

Exemple:
```
'0x123' == '0x845' is true
'0x123' === '0x845' is false
```

We can find other magic hashes on internet: https://git.linuxtrack.net/Azgarech/PayloadsAllTheThings/blob/master/PHP%20juggling%20type/README.md

For exemple: sha1 of `aaroZmOk` is `0e66507019969427134894567494305185566735`

So `sha1('aaroZmOk') == sha1(10932435112)` is true

To get the flag we open the url `http://chall.csivit.com:30272/?hash=aaroZmOk`

The flag is: `csictf{typ3_juggl1ng_1n_php}`

## Mr Rami
```
"People who get violent get that way because they can’t communicate."

http://chall.csivit.com:30231
```

There is a `robots.txt` file:
```
# Hey there, you're not a robot, yet I see you sniffing through this file.
# SEO you later!
# Now get off my lawn.

Disallow: /fade/to/black
```

And on url `http://chall.csivit.com:30231/fade/to/black` we can read the flag... so easy...

The flag is `csictf{br0b0t_1s_pr3tty_c00l_1_th1nk}`

## Secure Portal
```
This is a super secure portal with a really unusual HTML file. Try to login.

http://chall.csivit.com:30281
```

There is a password input on website

The password cheacker seems be an obfuscated script in javascript:
``` javascript
var _0x575c=['\x32\x2d\x34','\x73\x75\x62\x73\x74\x72\x69\x6e\x67','\x34\x2d\x37','\x67\x65\x74\x49\x74\x65\x6d','\x64\x65\x6c\x65\x74\x65\x49\x74\x65\x6d','\x31\x32\x2d\x31\x34','\x30\x2d\x32','\x73\x65\x74\x49\x74\x65\x6d','\x39\x2d\x31\x32','\x5e\x37\x4d','\x75\x70\x64\x61\x74\x65\x49\x74\x65\x6d','\x62\x62\x3d','\x37\x2d\x39','\x31\x34\x2d\x31\x36','\x6c\x6f\x63\x61\x6c\x53\x74\x6f\x72\x61\x67\x65',];(function(_0x4f0aae,_0x575cf8){var _0x51eea2=function(_0x180eeb){while(--_0x180eeb){_0x4f0aae['push'](_0x4f0aae['shift']());}};_0x51eea2(++_0x575cf8);}(_0x575c,0x78));var _0x51ee=function(_0x4f0aae,_0x575cf8){_0x4f0aae=_0x4f0aae-0x0;var _0x51eea2=_0x575c[_0x4f0aae];return _0x51eea2;};function CheckPassword(_0x47df21){var _0x4bbdc3=[_0x51ee('0xe'),_0x51ee('0x3'),_0x51ee('0x7'),_0x51ee('0x4'),_0x51ee('0xa')];window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]]('9-12','BE*');window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x2'),_0x51ee('0xb'));window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x6'),'5W');window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]]('16',_0x51ee('0x9'));window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x5'),'pg');window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]]('7-9','+n');window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0xd'),'4t');window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x0'),'$F');if(window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0x8'))===_0x47df21[_0x51ee('0x1')](0x9,0xc)){if(window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0x2'))===_0x47df21['substring'](0x4,0x7)){if(window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0x6'))===_0x47df21[_0x51ee('0x1')](0x0,0x2)){if(window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]]('16')===_0x47df21[_0x51ee('0x1')](0x10)){if(window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0x5'))===_0x47df21[_0x51ee('0x1')](0xc,0xe)){if(window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0xc'))===_0x47df21[_0x51ee('0x1')](0x7,0x9)){if(window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0xd'))===_0x47df21[_0x51ee('0x1')](0xe,0x10)){if(window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0x0'))===_0x47df21[_0x51ee('0x1')](0x2,0x4))return!![];}}}}}}}return![];}
```

When we beautify the code we obtain:
``` javascript
var _0x575c = ['2-4', 'substring', '4-7', 'getItem', 'deleteItem', '12-14', '0-2', 'setItem', '9-12', '^7M', 'updateItem', 'bb=', '7-9', '14-16', 'localStorage', ];

(function(_0x4f0aae, _0x575cf8) {
    var _0x51eea2 = function(_0x180eeb) {
        while (--_0x180eeb) {
            _0x4f0aae['push'](_0x4f0aae['shift']());
        }
    };
    _0x51eea2(++_0x575cf8);
}(_0x575c, 0x78));
var _0x51ee = function(_0x4f0aae, _0x575cf8) {
    _0x4f0aae = _0x4f0aae - 0x0;
    var _0x51eea2 = _0x575c[_0x4f0aae];
    return _0x51eea2;
};

function CheckPassword(_0x47df21) {
    var _0x4bbdc3 = [_0x51ee('0xe'), _0x51ee('0x3'), _0x51ee('0x7'), _0x51ee('0x4'), _0x51ee('0xa')];
    window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]]('9-12', 'BE*');
    window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x2'), _0x51ee('0xb'));
    window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x6'), '5W');
    window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]]('16', _0x51ee('0x9'));
    window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x5'), 'pg');
    window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]]('7-9', '+n');
    window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0xd'), '4t');
    window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x0'), '$F');
    if (window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0x8')) === _0x47df21[_0x51ee('0x1')](0x9, 0xc)) {
        if (window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0x2')) === _0x47df21['substring'](0x4, 0x7)) {
            if (window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0x6')) === _0x47df21[_0x51ee('0x1')](0x0, 0x2)) {
                if (window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]]('16') === _0x47df21[_0x51ee('0x1')](0x10)) {
                    if (window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0x5')) === _0x47df21[_0x51ee('0x1')](0xc, 0xe)) {
                        if (window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0xc')) === _0x47df21[_0x51ee('0x1')](0x7, 0x9)) {
                            if (window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0xd')) === _0x47df21[_0x51ee('0x1')](0xe, 0x10)) {
                                if (window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]](_0x51ee('0x0')) === _0x47df21[_0x51ee('0x1')](0x2, 0x4)) return !![];
                            }
                        }
                    }
                }
            }
        }
    }
    return ![];
}
```

In `CheckPassword` function, there is an initialisation of part of the password in local storage and then a comparison between the local storage and the password enter by the user

In the console of a browser, we execute:
``` javascript
var _0x575c = ['2-4', 'substring', '4-7', 'getItem', 'deleteItem', '12-14', '0-2', 'setItem', '9-12', '^7M', 'updateItem', 'bb=', '7-9', '14-16', 'localStorage', ];

var _0x51ee = function(_0x4f0aae, _0x575cf8) {
    _0x4f0aae = _0x4f0aae - 0x0;
    var _0x51eea2 = _0x575c[_0x4f0aae];
    return _0x51eea2;
};

var _0x4bbdc3 = [_0x51ee('0xe'), _0x51ee('0x3'), _0x51ee('0x7'), _0x51ee('0x4'), _0x51ee('0xa')];
window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]]('9-12', 'BE*');
window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x2'), _0x51ee('0xb'));
window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x6'), '5W');
window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]]('16', _0x51ee('0x9'));
window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x5'), 'pg');
window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]]('7-9', '+n');
window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0xd'), '4t');
window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]](_0x51ee('0x0'), '$F');
```

After, we can read in local storage each part of the password:
```
0-2:"5W"
2-4:"$F"
4-7:"bb="
7-9:"+n"
9-12:"BE*"
12-14:"pg"
14-16:"4t"
16:"^7M"
```

The full password is `5W$Fbb=+nBE*pg4t^7M`

We enter this password and we can read the flag !

The flag is: `csictf{l3t_m3_c0nfus3_y0u}`
