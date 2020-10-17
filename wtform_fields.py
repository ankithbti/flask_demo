from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    """ Registration form """
    username = StringField('username_label', validators=[InputRequired(message="Username required"), Length(min=4,max=25, message="Username must be b/w 4 and 25")])
    password = PasswordField('password_label', validators=[InputRequired(message="Username required"), Length(min=4,max=25, message="Username must be b/w 4 and 25")])
    confirm_pswd = PasswordField('confirm_password_label', validators=[InputRequired(message="Username required"), EqualTo('password', message="Confirm password should match password")])
    submit_button = SubmitField('Register')
