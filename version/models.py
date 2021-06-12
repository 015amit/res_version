from version import db


class User(db.Model):
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


    def __repr__(self):
        return f"User('{self.name}','{self.contact}')"

class Scrim2(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

db.create_all()