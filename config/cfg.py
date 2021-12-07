import os
from os.path import join,dirname,realpath
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(dirname(realpath(__name__)),'sqlite.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning
USER_APP_NAME = "Students' Association Registration App"      # Shown in and email templates and page footers
USER_ENABLE_EMAIL = True      # Disable email authentication
USER_ENABLE_USERNAME = False    # Enable username authentication
USER_EMAIL_SENDER_NAME=USER_APP_NAME
USER_EMAIL_SENDER_EMAIL= 'anukeshkumar891997@gmail.com'
USER_REQUIRE_RETYPE_PASSWORD = True
# Flask-Mail SMTP server settings
SECRET_KEY='abrakadabrasupersecretkey'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = 'anukeshkumar891997@gmail.com'
MAIL_PASSWORD = 'fteeqqtzvjrhmfyt' #should be in OS environment
MAIL_DEFAULT_SENDER = '"SAM" <noreply@sam.com>'
