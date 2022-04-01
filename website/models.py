from datetime import datetime
from flask_login import UserMixin
from website import db

# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))

class User(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    username=db.Column(db.String(64), nullable=False,unique=True)
    fullname=db.Column(db.String(64),nullable=False)
    password=db.Column(db.String(64), nullable=False)
    bookings=db.relationship('Booking',backref='booker',lazy='dynamic')

class Room(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    roomNumber=db.Column(db.String(64), nullable=False)
    bookings=db.relationship('Booking',backref='room',lazy='dynamic')
    
class Booking(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    roomId=db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    bookerId=db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    date=db.Column(db.String(12),nullable=False)
    startTime=db.Column(db.String(5),nullable=False)
    endTime=db.Column(db.String(5),nullable=False)



