from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, FileField, SubmitField, BooleanField
from wtforms.validators import Required, Email, EqualTo, Length, Optional, URL

#
# SPACES SHOULD NOT BED ALLOWED IN USERNAMES
# UNDERSCORES AND HYPENS ARE OK
#


# login form
class LoginForm(Form):
    """ logging in """
    email = StringField(validators=[Email(), Required()])
    password = PasswordField(validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')



# register form
class RegisterForm(Form):
    """ Register a new account """
    username = StringField(validators=[Required(), Length(3,30)])
    email = StringField(validators=[Required(), Email()])
    password = PasswordField(validators=[Required(), Length(6, 28)])
    password2 = PasswordField('Confirm', validators=[Required(), EqualTo('password')])
    agree_to_terms = BooleanField(validators=[Required()])
    submit = SubmitField('Register')



# change email
class ChangeEmailForm(Form):
    """ Changing your email """
    email = StringField(validators=[Required(), Email()])
    submit = SubmitField('Send email')



# change password
class ChangePasswordForm(Form):
    """ Change password """
    current_password = PasswordField('Current Password', validators=[Required()])
    new_password = PasswordField('New Password', validators=[Required(), Length(6, 28)])
    new_password2 = PasswordField('Confirm', validators=[Required(), EqualTo('new_password')])
    submit = SubmitField('Change')



# reset password
class ResetPasswordForm(Form):
    """ Reset password """
    email = StringField(validators=[Required(), Email()])
    submit = SubmitField('Send email')
