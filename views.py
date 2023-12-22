from flask import Blueprint
from flask import render_template

views = Blueprint(__name__, 'views')

@views.route('/')
@views.route('/home')
def view():
    return(render_template('index.html'))

@views.route('/publications')
def dogs():
    return(f'TBD')