from enum import unique
from version import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    
    return User.query.get(id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True)
    gender = db.Column(db.String(50), nullable = False)
    contact = db.Column(db.String(50), nullable = False, unique = True)
    roll = db.Column(db.String(50), nullable = False)
    year = db.Column(db.String(50), nullable = False)
    hackid = db.Column(db.String(50), nullable = False)
    iname = db.Column(db.String(50), nullable = False)
    address = db.Column(db.String(100), nullable = False)
    city = db.Column(db.String(50), nullable = False)
    state = db.Column(db.String(50), nullable = False)
    pin = db.Column(db.String(20), nullable = False)
    pic_name = db.Column(db.String(200))
    pic_data = db.Column(db.LargeBinary)
    scrim1 = db.relationship('Scrim1', backref ='event1')
    scrim2 = db.relationship('Scrim2', backref ='event2')
    scrim3 = db.relationship('Scrim3', backref ='event3')
    feedback = db.relationship('Feedback', backref ='feedback2')


    def __repr__(self):
        return f"User('{self.name}','{self.contact}')"

class Scrim1(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Scrim2(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Scrim3(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Mothra(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Codathon(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Conundrum(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Math_Pirate(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Apprentissage(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class App_Replica(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Maze_Runner(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Genius(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class CTB(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Code_Pazuru(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.String, unique=False, default="open")
    feedback = db.relationship('Feedback', backref ='feedback1',cascade="all,delete")

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    overall = db.Column(db.Integer)
    level = db.Column(db.Integer)
    clarity = db.Column(db.Integer)
    access = db.Column(db.Integer)
    source = db.Column(db.String)
    feed = db.Column(db.String, nullable=True)


class Feed1(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    mothra = db.Column(db.Integer)
    codathon = db.Column(db.Integer)
    math_pirate = db.Column(db.Integer)
    app_replica = db.Column(db.Integer)
    apprentissage = db.Column(db.Integer)
    conundrum = db.Column(db.Integer)
    maze_runner = db.Column(db.Integer)
    ctb = db.Column(db.Integer)
    genius = db.Column(db.Integer)
    code_pazuru = db.Column(db.Integer)
    scrim1 = db.Column(db.Integer)
    scrim2 = db.Column(db.Integer)
    experience = db.Column(db.String, nullable=True)
    suggestion = db.Column(db.String, nullable=True)
    overall = db.Column(db.String, nullable=True)

db.create_all()