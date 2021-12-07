import os
from os.path import join,dirname,realpath
from flask import Flask, config
from flask_user import UserManager, user_manager
from flask_user.forms import RegisterForm
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


db = SQLAlchemy()
mail=Mail()
bootstrap=Bootstrap()
csrf=CSRFProtect()
nav=Nav()
class CustomRegisterForm(RegisterForm):
    first_name = StringField(('First Name'), validators=[DataRequired()])
    last_name = StringField('Last name')


class CustomUserManager(UserManager):
    def customize(self, app):
        self.RegisterFormClass = CustomRegisterForm
def create_app():
    app=Flask(__name__)
    configuration=os.path.join(dirname(realpath(__name__)),'config','cfg.py')
    app.config.from_pyfile(configuration)
    db.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)
    nav.init_app(app)

    from app.models import User
    user_manager=CustomUserManager(app,db,User)

    return app
    