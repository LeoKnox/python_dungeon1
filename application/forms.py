from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class LoginForm(FlaskForm):
    login_id    =   IntegerField("Login Id", validators=[DataRequired()])
    login_name  =   StringField("Login Name", validators=[DataRequired()])
    remember_me =   BooleanField("Remember Me")
    submit      =   SubmitField("Login")