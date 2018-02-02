from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First Name', validators=[DataRequired("Enter First Name")])
    last_name = StringField('Last Name', validators=[DataRequired("Enter Last Name")])
    email = StringField('Email', validators=[DataRequired("Enter Email"), Email("Enter a Valid Email")])
    password = PasswordField('Password', validators=[DataRequired("Enter Password"), Length(min=5,message="Password must be > 5 characters")])
    submit = SubmitField('Sign Up')
