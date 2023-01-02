# simple-flash-app
 simple flask application

### starting the application

Method 1: (When __init__.py file is used)
```
gunicorn -w 2 simpleapp.app
```

Method 2: (When app.py file is used)
```
gunicorn -w 2 simpleapp.app:app
```

#! /bin/bash
apt update
apt -y install git
apt -y install python3-pip
git clone git@github.com:arif-b-khan/simple-flash-app.git

#! /bin/bash
apt update
apt -y install git
apt -y install python3-pip
git clone https://github.com/arif-b-khan/simple-flash-app.git /home/arif_bannehasan/app
cd /home/arif_bannehasan/app 
pip install -r requirements.txt
gunicorn --config gunicorn_config.py simpleapp.app:app

sudo bash -c 'python3 appinstall.py'

#! /bin/bash
git clone https://github.com/arif-b-khan/simple-flash-app.git /home/arif_bannehasan/app
cd /home/arif_bannehasan/app 
pip install -r requirements.txt
gunicorn --config gunicorn_config.py simpleapp.app:app