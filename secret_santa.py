from flask import Flask, render_template, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func, select
from flask_mail import Mail, Message
from models import *
from flask.ext.bootstrap import Bootstrap
import random

app = Flask(__name__)


app.config.from_object('config')


db = SQLAlchemy(app)
mail = Mail(app)
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET', 'POST'])
def index():
    eve_name = None
    email = None
    form = SignUpForm()
    if form.validate_on_submit():
        name = form.eve_name.data
        form_email = form.email.data
        user_add = Users(user=name,email=form_email)
        # checks for existing username/email and returns error
        if db.session.query(Users).filter(Users.user == name).first() is None:
            if db.session.query(Users).filter(Users.email == form_email).first() is None:
                db.session.add(user_add)
            else: flash('That email has already been submitted. Please try again')
        else:
            flash('That username has already been submitted. Please try again')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, eve_name=eve_name, email=email)


if __name__ == '__main__':
    app.run(debug=True)
