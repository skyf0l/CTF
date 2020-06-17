# Web

## Agent 95
```
They've given you a number, and taken away your name~

Connect here:
http://jh2i.com:50000
```

On website, it writes:
```
You don't look like our agent!
We will only give our flag to our Agent 95! He is still running an old version of Windows...
```

Agent 95 ? Maybe its window 95 user-agent ?

On https://en.wikipedia.org/wiki/User_agent we can see that the user-agent or Window95 is `Microsoft Internet Explorer/4.0b1 (Windows 95)`

We access to the website with this user-agent and we can read the flag:
```
$ curl -h "^Cft Internet Explorer/4.0b1 (Windows 95ows 95)" http://jh2i.com:50000/
[tom.rorato@linux Downloads]$ curl -H "User-Agent:Microsoft Internet Explorer/4.0b1 (Windows 95) " http://jh2i.com:50000/
flag{user_agents_undercover}
[...]
```

The flag is: `flag{user_agents_undercover}`

## Localghost
```
BooOooOooOOoo! This spooOoOooky client-side cooOoOode sure is scary! What spoOoOoOoky secrets does he have in stooOoOoOore??

Connect here:
http://jh2i.com:50003

Note, this flag is not in the usual format.
```

On website, the flag is stored on local storage, we can access to it in firefox with `inspect element`, go in `Storage` menu and in `Local Storage` 

The flag is: `JCTF{spoooooky_ghosts_in_storage}`
