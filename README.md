# ORSO - Osint Reconnaissance Subdomain Obtainer - OSINT/Information Gathering Tool

ORSO (Osint Reconnaissance Subdomain Obtainer) is a OSINT tool to discover subdomains of a target.

It performs a passive scan mixed to web scraping in order to obtain the information.

# Screenshot

![](https://github.com/MrSaighnal/ORSO/blob/master/images/screen.png)

## Quick start

```
git clone https://github.com/MrSaighnal/ORSO
cd ORSO
python3 orso.py example.com
```
# Example

![](https://github.com/MrSaighnal/ORSO/blob/master/images/usage.gif)

# Requirements

```
apt install python3
pip install beautifulsoap4
pip install requests
```

## Why

ORSO is usefull for pentester and bug hunter, it provides a number of way to attack the target.

---

## FAQ

- **I find a lot of domains, but many of them are offline. Why?**
    - ORSO can reach out the history of a domain, an implementation to verify if a host is up will be available soon. I advice to check the obtained domains on archive.org, in order to get more information about your target.



## To do

- Implementing Search Engine gathering
- Check if discovered subdomaina are up
- Time machine function
- Finding new sources
- Removing email address

# DONATION

If you liked my work the best way to tell me thanks is to buy me a coffee.

**BTC `183omAyoCCFkHE7s7dzMJfJZHhR3f8JMam`**

## Support

Reach out to me.

- Website at <a href="http://mrsaigh@github.io" target="_blank">`mrsaighnal.github.io`</a>
- Email `mrsaigh[AT]protonmail[DOT]com`

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**

