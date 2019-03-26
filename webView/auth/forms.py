from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
	username = StringField("Username")
	password = PasswordField("Password")
	submit = SubmitField("Login")


class SignupForm(FlaskForm):
	username = StringField("Your username")
	password = PasswordField("Your password")
	password_again = PasswordField("Your password again")
	email = EmailField("Your email")
	submit = SubmitField("Signup")
