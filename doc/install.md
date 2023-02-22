# Install

安装步骤

```sh
$ sudo apt-get install python3 python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools node-less libjpeg-dev gdebi -y
$ sudo apt-get install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev -y

$ git clone https://github.com/telesoho/coreodoo.git
$ cd coreodoo
$ python3 -m venv venv
$ source venv/bin/activate
```

```sh
(venv)$ pip install setuptools wheel phonenumbers
(venv)$ pip install -r requirements.txt
(venv)$ pip install -r requirements-dev.txt
(venv)$ pre-commit install
```
