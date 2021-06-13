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
    feedback = db.relationship('Feedback', backref ='feedback2')


    def __repr__(self):
        return f"User('{self.name}','{self.contact}')"

class Scrim1(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Scrim2(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique=True, nullable=False)
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


db.create_all()