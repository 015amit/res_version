
from flask import render_template,session,jsonify,request,redirect,flash,url_for,send_file
from flask.helpers import make_response
from werkzeug.utils import redirect
from version import app,db
from version.models import Codathon, Event, Scrim1, Scrim2, User, Feedback, Scrim3, Mothra, Conundrum, Math_Pirate, Apprentissage, App_Replica, Maze_Runner, Genius, CTB, Code_Pazuru
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

@app.route('/magazines')
def magazine():
    return render_template('magazine.html', title="Magazines")

@app.route('/events')
def events():
    return render_template('events.html', title="Events", events=allevents['event'])

@app.route('/events/<int:id>')
def desc(id):
    if id in range(1,14):
        return render_template('desc.html', id=id, event=allevents['event'][id-4])
    else:
        return page_not_found(404)

@app.route('/events/<int:id>/registration', methods=['GET','POST'])
def registration(id):
    if request.method=='POST':
        user_id = request.form.get('scrim1id')
        if id == 1:
            user = Scrim1(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Scrim 1')
            return redirect(url_for('profile'))
        if id == 2:
            u1 = Scrim2.query.filter_by(user_id = user_id).first()
            if u1:
                flash('you have registered already for Scrim 2')
                return redirect(url_for('profile'))
            user = Scrim2(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Scrim 2')
            return redirect(url_for('profile'))
        if id == 3:
            user = Scrim3(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Workshop')
            return redirect(url_for('profile'))
        if id == 4:
            user = Mothra(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Mothra')
            return redirect(url_for('profile'))
        if id == 6:
            user = Codathon(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Codathon')
            return redirect(url_for('profile'))
        if id == 7:
            user = Conundrum(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Conundrum')
            return redirect(url_for('profile'))
        if id == 8:
            user = Math_Pirate(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Math 𝜋rate')
            return redirect(url_for('profile'))
        if id == 9:
            user = Apprentissage(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Apprentissage')
            return redirect(url_for('profile'))
        if id == 10:
            user = App_Replica(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for App Replica')
            return redirect(url_for('profile'))
        if id == 11:
            user = Maze_Runner(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Maze Runner')
            return redirect(url_for('profile'))
        if id == 12:
            user = Genius(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Genius')
            return redirect(url_for('profile'))
        if id == 13:
            user = CTB(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for CTB')
            return redirect(url_for('profile'))
        if id == 14:
            user = Code_Pazuru(user_id=user_id)
            db.session.add(user)
            db.session.commit()
            flash('you have registered for Code Pazuru')
            return redirect(url_for('profile'))
    return render_template('404.html')

@app.route('/registration', methods=['GET','POST'])
def register():
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
            return redirect(url_for('register'))
        if  contact1:
            flash('This Mobile Number has already been taken !')
            return redirect(url_for('register'))
        entry = User(name=name,email=email, gender=gender, contact=contact, roll=roll,
                year=year, hackid=hackid, iname=iname,address=address, city=city,
                state=state, pin=pin, pic_name=contact, pic_data=img.read())
        db.session.add(entry)
        db.session.commit()
        flash("You are registered successfully ")
        return redirect(url_for('login'))
    return render_template('register.html', title="Registration")

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
            em = user.email
            cont = user.contact
            gen = user.gender
            em = str(em).lower()
            gen = str(gen).lower()
            cont = str(cont).lower()
            check_pass = em[0:4]+cont[0:4]+gen[0:4]
            if check_pass==password:
                login_user(user)
                return redirect(url_for('profile'))
            flash('Incorrect Password')
            return redirect(url_for('login'))

        elif user is None:
            flash("you haven't registered in any event yet ")
            return redirect(url_for('login'))
              
        else:    
            flash("Incorrect email or password")
            return redirect(url_for('login'))

    return render_template('login.html', title="Log In")

@app.route('/dashboard', methods=['GET','POST'])
@login_required
def profile():
    registeredevent = []
    feedbackevent = []
    user = User.query.filter_by(id=current_user.id).first()
    events = Event.query.order_by(Event.id).all()
    closed_event = Event.query.filter_by(status = "closed").all()
    scrim1 = Scrim1.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(scrim1)
    scrim2 = Scrim2.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(scrim2)
    scrim3 = Scrim3.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(scrim3)
    mothra = Mothra.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(mothra)
    codathon = Codathon.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(codathon)
    conundrum = Conundrum.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(conundrum)
    math_Pirate = Math_Pirate.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(math_Pirate)
    apprentissage = Apprentissage.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(apprentissage)
    app_Replica = App_Replica.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(app_Replica)
    maze_Runner = Maze_Runner.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(maze_Runner)
    genius = Genius.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(genius)
    ctb = CTB.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(ctb)
    code_Pazuru = Code_Pazuru.query.filter_by(user_id=current_user.id).first()
    registeredevent.append(code_Pazuru)
    feeds = Feedback.query.filter_by(user_id=current_user.id).all()
    if feeds:
        for feed in feeds:
            event3 = Event.query.filter_by(id=feed.event_id).first()
            feedbackevent.append(event3)
    if request.method == 'POST':
        user.name=request.form.get('name')
        email=request.form.get('email')
        user.gender=request.form.get('gender')
        contact=request.form.get('contact')
        user.roll=request.form.get('roll')
        user.year=request.form.get('year')
        user.hackid=request.form.get('hackid')
        user.iname=request.form.get('iname')
        user.address = request.form.get('address')
        user.city=request.form.get('city')
        user.state=request.form.get('state')
        user.pin=request.form.get('pin')
 
        if email != user.email or contact != user.contact:
            email1 = User.query.filter_by(email=email).first()
            cont1 = User.query.filter_by(contact=contact).first()
            if email1 or cont1:
                flash('This email-id or contact is already taken!')
                return redirect(url_for('profile')) 

        user.email=email
        user.contact=contact

        db.session.commit()
        flash('your profile is updated successfully')
        return redirect(url_for('profile'))
    return render_template('profile.html', user=user,events=zip(events,registeredevent),events1=zip(events,registeredevent), title="Dashboard", pop=events, pop1=feedbackevent, pop2=registeredevent, closed_event = zip(closed_event, registeredevent))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', title="Internal Server Error"), 500






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
    


@app.route('/event/<int:id>/feedback', methods=['GET','POST'])
@login_required
def feedback(id):
    events = Event.query.filter_by(id=id).first_or_404()
    if events:
        if request.method=='POST':
            first = request.form.get('first')
            second = request.form.get('second')
            third = request.form.get('third')
            fourth = request.form.get('fourth')
            fifth = request.form.get('fifth')
            sixth = request.form.get('sixth')

            name = Event.query.filter_by(id=id).first()
            u1 = Feedback.query.filter_by(user_id=current_user.id, event_id=id).first()
            if u1:
                flash(f'your Feedback for {name.name} is already submitted.')
                return redirect(url_for('profile'))
            feedback = Feedback(event_id=id, user_id=current_user.id, overall=first, level=second, clarity=third, access=fourth, source=fifth, feed=sixth)
            db.session.add(feedback)
            db.session.commit()
            flash(f'Thank you for your Feedback for {name.name}')
            return redirect(url_for('profile'))

        return render_template('feedback.html',event=events, title="Feedback")  
      


@app.route('/amit_nikki_anshu', methods=['GET','POST'])
def adddata():
    if request.method == 'POST':
        name = request.form.get('name')
        status = request.form.get('status')

        data = Event(name = name, status = status)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('adddata'))
    return render_template('addevent.html')





