from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField,SubmitField,SelectMultipleField
from wtforms.validators import InputRequired,Optional
from datetime import datetime,date
from flask_user import  current_user
from wtforms.widgets import ListWidget, CheckboxInput

class AssociationForm(FlaskForm):
    name=StringField("Association Name",validators=[InputRequired()])
    submit=SubmitField("Save")

class AssociationInputForm(FlaskForm):
    associations = SelectMultipleField(
        'Associations',
        validators=[Optional()],
        coerce=int,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput())
    submit=SubmitField("Save")