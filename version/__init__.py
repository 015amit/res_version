from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import re



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','postgres://qnqfgovaplwtuj:133018b4322b974d88cded3ac737f24afeb6ff8b1405469fdf296f07c15409de@ec2-3-214-136-47.compute-1.amazonaws.com:5432/dbabnsoq30me3f')
if app.config['SQLALCHEMY_DATABASE_URI'].startswith("postgres://"):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace("postgres://", "postgresql://", 1)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY','asdfhsdfgcvbnesdgh')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'your secret key'
  
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category =  'danger'

from version import routes