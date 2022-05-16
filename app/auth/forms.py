from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError



class RegistrationForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired(),EqualTo('password_confirm',message = 'passwords must match')])
    password_confirm = PasswordField('Confirm passwords',validators=[DataRequired()])
    submit = SubmitField('Sign up')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is already an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = StringField('password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')
