# I-Spy-P
[![Built On](https://img.shields.io/badge/python-3.7-brightgreen)](https://img.shields.io/badge/python-3.7-brightgreen) [![Last Commit](https://img.shields.io/github/last-commit/byhay1/python_challenge)](https://img.shields.io/github/last-commit/byhay1/python_challenge) [![Version](https://img.shields.io/badge/Version-1.0-blue)](https://img.shields.io/badge/Version-1.0-blue)[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<!-- [![logo](https://raw.githubusercontent.com/byhay1/python_challenge/master/images/I-Spy-P.png](https://raw.githubusercontent.com/byhay1/python_challenge/master/images/I-Spy-P.png) -->


> Application for identifying IPs in a txt file and getting more information from the IP (Or any IP)

> Have txt filled with IPs? Want to see if target IP/your IP is in the txt? Want more details on IP? Use I-Spy-P




***Pretty Darn Fast***

<VIDEO HERE>

- What made the challenge "challenging" was using native python solely for all of the code. No 3rd-party Modules/Packages!
- However, even without BeautifulSoup, Selenium, and even Pandas, the code ran well.



---

## Table of Contents 

- [Installation](#installation)
- [Features](#features)
- [Usage-Help](#usage-help)
- [Tests](#tests)
- [Future](#future)
- [Support](#support)



---

## Example (Optional)

```javascript
// code away!

let generateProject = project => {
  let code = [];
  for (let js = 0; js < project.length; js++) {
    code.push(js);
  }
};
```

---

## Installation

- Python 3.X installed
- Terminal or IDE capable of running .py scripts

### Setup

> update and install python

```shell
$ cd /usr/src
$ sudo wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgzs
```

> extract the package

```shell
$ sudo tar xzf Python-3.7.4.tgz
```

> compile python

```shell
$ cd Python-3.7.4
$ sudo ./configure --enable-optimizations
$ sudo make altinstall
```

---

## Features
- Ability to parse through text to find and extract IPs. Code can be easily modified to export all IPs found in document into another .txt file or .csv. 
- Search target IP against geoIP and RDAP apis to extract additional information about the target IP
---
## Usage-Help 

[![helpme](https://raw.githubusercontent.com/byhay1/python_challenge/master/images/Help.png](https://raw.githubusercontent.com/byhay1/python_challenge/master/images/Help.png) 

---
## Tests

- Sample txt file and IPs within the .txt are in the test folder
- Utilized both <a href="http://api.db-ip.com/v2/free/" target="_blank">DB-IP API</a> and 
<a href="https://www.rdap.net/ip/" target="_blank">RDAP API</a> to get information on IP easier.

---


## Future

- Creating a docker image so others can use
- Better UI
- Better formatting

---

## Support

Reach out to me to help support the app!

- Github, just create commits
- Other social networks coming soon 

---

## Donations

BTC - Add Later
LTC - Add Later
ETH - Add Later
