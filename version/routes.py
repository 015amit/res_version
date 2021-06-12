
from flask import render_template,session,jsonify,request,redirect,flash,url_for,send_file
from flask.helpers import make_response
from werkzeug.utils import redirect
from version import app,db
from version.models import User
from flask_login import login_user, current_user,login_required, logout_user
import json
from io import BytesIO
import codecs

from .teams import data, senior, junior_head
from .events import allevents


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
    return render_template('events.html', title="Events", events=allevents['event'])

@app.route('/events/<int:id>')
def desc(id):
    return render_template('desc.html', id=id, event=allevents['event'][id-1])

@app.route('/events/<int:id>/registration', methods=['GET','POST'])
def register(id):
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        gender=request.form.get('gender')
        contact=request.form.get('contact')
        roll=request.form.get('roll')
        year=request.form.get('year')
        hackid=request.form.get('hackid')
        iname=request.form.get('iname')
        address = request.form.get('address')
        city=request.form.get('city')
        state=request.form.get('state')
        pin=request.form.get('pin')
        img = request.files['Image']
        email1 = User.query.filter_by(email=email).first()
        contact1 = User.query.filter_by(contact=contact).first()
        if email1:
            flash('This email has already been taken !')
            return redirect(url_for('register',id=id))
        if  contact1:
            flash('This Mobile Number has already been taken !')
            return redirect(url_for('register',id=id))
        entry = User(name=name,email=email, gender=gender, contact=contact, roll=roll,
                year=year, hackid=hackid, iname=iname,address=address, city=city,
                state=state, pin=pin, pic_name=contact, pic_data=img.read())
        db.session.add(entry)
        db.session.commit()
        flash("You are registered successfully ")
        return redirect(url_for('desc',id=id))
    return render_template('register.html', title="Registration", id=id )

@app.route('/teams/<string:name>')
def teams(name):
    if senior[name] and junior_head[name]:
        return render_template('team.html', title="Teams",name=name, team=data[name], senior =senior[name], junior= junior_head[name])
    elif senior[name]:
        return render_template('team.html', title="Teams",name=name, team=data[name], senior =senior[name])    
    return render_template('team.html', title="Teams",name=name, team=data[name])


@app.route('/login', methods=['GET','POST'])
def login():
  
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            login_user(user)
            return redirect(url_for('home'))

        elif user is None:
            flash("you haven't registered in any event yet ")
            return redirect(url_for('events'))
              
        else:    
            flash("Incorrect email or password")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    user = User.query.filter_by(id=11).first()
    if request.method == 'POST':
        user.name=request.form.get('name')
        user.email=request.form.get('email')
        user.gender=request.form.get('gender')
        user.contact=request.form.get('contact')
        user.roll=request.form.get('roll')
        user.year=request.form.get('year')
        user.hackid=request.form.get('hackid')
        user.iname=request.form.get('iname')
        user.address = request.form.get('address')
        user.city=request.form.get('city')
        user.state=request.form.get('state')
        user.pin=request.form.get('pin')

        db.session.commit()
        flash('your profile is updated successfully')
        return redirect(url_for('profile'))
    return render_template('profile.html', user=user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', title="Internal Server Error"), 500


@app.route('/account')
def account():
    return render_template('account.html', title="Account")


@app.route('/show/<int:id>')
def getimg(id):
    user = User.query.filter_by(id=id).first()
    header_byte = codecs.encode(user.pic_data[0:3], "hex")
    header_byte = str(header_byte).lower()
    header_byte = header_byte[2:8]
    # return header_byte
    # header_byte = user.pic_data[0:3].encode("hex").lower()

    if header_byte == '255044':
        get = send_file(BytesIO(user.pic_data), attachment_filename='flask.pdf')
    elif header_byte == '89504e':
        get = send_file(BytesIO(user.pic_data), attachment_filename='flask.png')
    elif header_byte == 'ffd8ff':
        get = send_file(BytesIO(user.pic_data), attachment_filename='flask.jpg')
    else:
        return "binary file"
    return get
    