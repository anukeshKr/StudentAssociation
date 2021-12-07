from app import db
from flask_user import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    # User fields
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # Relationships
    roles = db.relationship('Role', secondary='user_roles')
    associations= db.relationship('Association',secondary='association_membership')

    def has_roles(self, *args):
        return set(args).issubset({role.name for role in self.roles})

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

#Define the Association table
class Association(db.Model):
    __tablename__='associations'
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

#Define the Association Membership table
class AssociationUsers(db.Model):
    __tablename__='association_membership'
    id= db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    association_id = db.Column(db.Integer(), db.ForeignKey('associations.id', ondelete='CASCADE'))