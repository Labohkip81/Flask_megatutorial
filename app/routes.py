from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm






@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have successfully logged in; Welcome{}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


#Defines the route for home page for this application.
@app.route('/')
@app.route('/index')


def index():
    user = {'username': 'Laban'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!',
            'greeting': 'Hey there thanks for the information'
        },

         {
            'author': {'username': 'Laban'},
            'body': 'Its another log here',
            'greeting': 'Hey there thanks much'
        },
     
        {   
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!',
            'greeting': 'Woow, can\'t resist this'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)