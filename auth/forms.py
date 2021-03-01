from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo,ValidationError
from ..models import User
from wtforms import StringField,PasswordField,BooleanField,SubmitField

