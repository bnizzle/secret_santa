from flask.ext.wtf import Form
from wtforms import BooleanField, StringField, validators, SubmitField
from wtforms.validators import DataRequired
from secret_santa import db

class SignUpForm(Form):
    eve_name = StringField('What is your eve characters name?', validators=[DataRequired()])
    email = StringField('The best email address to contact you on',validators=[DataRequired()])
    submit = SubmitField('Submit')

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(120),unique=True)
    email = db.Column(db.String(120),unique=True)