from flask import flash
from flask import redirect
from flaskblog import app
from flaskblog.models import User, Post
from flask import Flask, render_template, url_for
from flaskblog.forms import RegistrationForm, LoginForm

posts = [
        {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
    

]

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template("register.html",title="Register", form=form)

@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f"You have been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash(f"Log In unsuccessful, please check username and password", 'danger')
    return render_template("login.html",title="Register", form=form)
    