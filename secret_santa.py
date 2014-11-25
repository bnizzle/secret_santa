from flask import Flask, render_template, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from models import *
from flask.ext.bootstrap import Bootstrap

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
        user_add = Users(user = name,email=form_email)
        if name == db.session.query(Users.user).filter(Users.user == name) or form_email == db.session.query(Users.email).filter(Users.email == form_email):
            db.session.add(user_add)
        else:
            flash('That username or email has already been submitted. Please try again')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, eve_name=eve_name, email=email)


if __name__ == '__main__':
    app.run(debug=True)
