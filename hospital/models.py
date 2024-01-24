from . import db 
from . import app 
from datetime import datetime
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

    def __repr__(self):
        return f"Test{'{self.name}', '{self.email}'}"

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    usertype=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))

    def __repr__(self):
        return f"User{'{self.username}','{self.usertype}', '{self.email}', '{self.password}'}"

class Patients(db.Model):
    pid=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    name=db.Column(db.String(50))
    gender=db.Column(db.String(50))
    slot=db.Column(db.String(50))
    disease=db.Column(db.String(50))
    time=db.Column(db.String(50),nullable=False)
    date=db.Column(db.String(50),nullable=False)
    dept=db.Column(db.String(50))
    number=db.Column(db.String(50))
    def __repr__(self):
        return f"Patients{ '{self.email}', '{self.name}', '{self.gender}', '{self.slot}', '{self.disease}', '{self.time}','{self.date}', '{self.dept}', '{self.number}'}"

class Doctors(db.Model,UserMixin):
    did=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    doctorname=db.Column(db.String(50))
    dept=db.Column(db.String(50))
    def __repr__(self):
        return f"Doctors{'{self.email}','{self.doctorname}', '{self.dept}'}"
    

class Trigr(db.Model):
    tid=db.Column(db.Integer,primary_key=True)
    pid=db.Column(db.Integer)
    email=db.Column(db.String(50))
    name=db.Column(db.String(50))
    action=db.Column(db.String(50))
    timestamp=db.Column(db.String(50))
    def __repr__(self):
        return f"Trigr{'{self.pid}','{self.email}', '{self.name}', '{self.action}', '{self.timestamp}'}"

with app.app_context():
    db.create_all()