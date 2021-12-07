# Steps to run the project
> virtualenv venv (Required once)
>pip install -r requirements.txt (Required once)

Start virtualenv on Command Prompt (Run Everytime)
>venv\Scripts\activate

Run project (Everytime)
Use new Terminal Activate venv
> python run.py

> Open flask shell (Required Once)
$ flask shell
>>>from app import db
>>>db.create_all()

This will create a database (sqlite.db) with 6 tables

> Making a User Admin (Required once)
A user should be Registered 
>flask shell
>>> from app.models import *
>>> user=User.query.filter(User.email=='anukeshkumar891997@gmail.com').first()
>>> user.roles.append(Role(name='Admin'))
>>> db.session.add(user)
>>> db.session.commit()

 # StudentAssociation
