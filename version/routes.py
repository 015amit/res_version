
from flask import render_template,session,jsonify,request
from flask.helpers import make_response
from version import app
import json

from .teams import data, senior, junior_head


@app.route('/')
def home():
    return render_template('home.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us")

@app.route('/events')
def events():
    return render_template('events.html', title="Events")

@app.route('/teams/<string:name>')
def teams(name):
    if senior[name] and junior_head[name]:
        return render_template('team.html', title="Team",name=name, team=data[name], senior =senior[name], junior= junior_head[name])
    elif senior[name]:
        return render_template('team.html', title="Team",name=name, team=data[name], senior =senior[name])    
    return render_template('team.html', title="Team",name=name, team=data[name])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404
