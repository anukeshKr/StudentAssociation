from flask.templating import render_template
from app import create_app,db,nav
from app.models import User,Role,UserRoles,Association,AssociationUsers
from app.forms import AssociationForm,AssociationInputForm
import datetime
from flask import Flask, request, render_template_string,flash
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_user import current_user, login_required, roles_required
from flask_nav.elements import Navbar, View,Separator,Subgroup,Link, Text


app=create_app()
@nav.navigation()
def mynavbar():
    if current_user.is_authenticated:
        if current_user.has_roles('Admin'):
            navbar=Navbar(
                'SAM ',
                View('Home', 'home_page'),
                Subgroup('Association',
                    View('List Association', 'list_Association'),
                    View('Add Association', 'add_Association')
                ),
                Subgroup('Membership',
                    View('List Membership', 'list_Membership')
                ),
                Subgroup(current_user.first_name+': Admin',
                    View('Edit User','user.edit_user_profile'),
                    View('Change Password','user.change_password'),
                    View('Logout','user.logout')
                )
            )
        else:
            navbar=Navbar(
                'SAM-Student',
                View('Home', 'home_page'),
                Subgroup('Association',
                    View('List Association', 'list_Association')
                ),
                Subgroup('Membership',
                    View('Update Membership', 'update_Membership')
                ),
                Subgroup(current_user.first_name,
                    View('Edit User','user.edit_user_profile'),
                    View('Change Password','user.change_password'),
                    View('Logout','user.logout')
                )
            )
    else:
        navbar=Navbar(
            'Student Association Membership',
            View('Home', 'home_page'),
            View('Login','user.login'),

        )
    return navbar

@app.route('/home')
def hello():
    return render_template('home.html')
# The Home page is accessible to anyone
@app.route('/')
def home_page():
    return render_template('home.html')

# The Members page is only accessible to authenticated users
@app.route('/members')
@login_required    # Use of @login_required decorator
def member_page():
    return render_template('home.html')

@app.route('/admin')
@roles_required('Admin')    # Use of @roles_required decorator user.roles.append(Role(name='Admin'))
def admin_page():
    return render_template('home.html')

@app.route('/addAssociation',methods = ['POST', 'GET'])
@roles_required('Admin') 
def add_Association():
    form=AssociationForm()
    if request.method == 'POST' and form.validate():
        assName=form.name.data
        if form.submit.data == True:
            association=Association(name=assName)
            db.session.add(association)
            db.session.commit()
            flash('Association Added','info')
            return render_template('home.html')
    return render_template('basic.html',form=form)

@app.route('/listAssociation')
@login_required
def list_Association():
    assocaitions=Association.query.all()
    return render_template('listAssocation.html',associations=assocaitions)

@app.route('/updateMembership',methods = ['POST', 'GET'])
@login_required
def update_Membership():
    #takes user_id as input gives list of associations @app.route(/some-form/, methods=['GET', 'POST'])
    form = AssociationInputForm()
    # Populate the multiselect field's data

    associations = Association.query.all()
    user=User.query.filter(User.email==current_user.email).first()
    form.associations.choices = [(a.id, a.name) for a in associations]#all associations
    form.associations.data=[(a.id) for a in user.associations] #associated with user
    print(form.associations.data)
    print(User.query.filter(User.email==current_user.email).first().associations)
    print(current_user.id,current_user.email)
    if form.validate_on_submit():
        print("Form Data",form.associations.data)
        print("requests",request.form.getlist('associations'))
        #find associations 
        associations=Association.query.filter(Association.id.in_(request.form.getlist('associations'))).all()
        print(associations)
        user.associations=associations
        db.session.add(user)
        db.session.commit()        
        flash('Membership Updated','info')
        return render_template('home.html')
    return render_template('basic.html', form=form)

@app.route('/listMembership',methods = ['POST', 'GET'])
@roles_required('Admin') 
def list_Membership():
    result=db.session.query(User.first_name, User.last_name, User.email, Association.name, AssociationUsers).filter(AssociationUsers.user_id == User.id).filter(AssociationUsers.association_id == Association.id).all()
    return render_template('listMembership.html',results=result)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)