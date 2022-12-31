# simple-flash-app
 simple flask application

### starting the application

Method 1: (When __init__.py file is used)
```
gunicorn -w 2 simpleapp.app:app
```

Method 2: (When app.py file is used)
```
gunicorn -w 2 simpleapp.app:app
```
