from main import app
from flask import render_template, request
from main.forms import RegisterForm
from main.models import user
from main import db


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('Home.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    # form = RegisterForm()
    # print(form.validate_on_submit())
    # if form.validate_on_submit():
    #     print(form.username.data)
    #     user_to_create = user(username=form.username.data,
    #                           email=form.email_address.data,
    #                           password=form.password1.data)
    #     db.session.add(user_to_create)
    #     db.session.commit()
    return render_template('Register.html')

@app.route('/submitform', methods=['GET', 'POST'])
def submit_form():
    print(request.form['username'])
    return render_template('Register.html')





