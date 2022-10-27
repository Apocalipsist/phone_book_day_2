from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

 
class Contact(FlaskForm):
    first = StringField('First Name', validators=[DataRequired()])
    last = StringField('Last name', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    home = StringField('Address', validators=[DataRequired()])
    submit = SubmitField()