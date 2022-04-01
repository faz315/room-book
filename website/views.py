import json
from tracemalloc import start
from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import *
from . import db
from website.forms import *
from sqlalchemy import *

views = Blueprint('views', __name__)

# routes for the website
# home page
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

# route for create booking
@views.route('/createbooking', methods=['GET', 'POST'])
@login_required
def createBooking():
    if request.method == 'POST':
        # get data from the fields
        roomNumber = request.form.get('drop_roomNumber')
        date = request.form.get('date')
        startTime = request.form.get('startTime')
        endTime = request.form.get('endTime')
        user= current_user.id
        
        # compare if the similar booking exists with the booking that is trying to be made
        sameRoom = Booking.query.filter_by(roomId= roomNumber).first()
        sameDate = Booking.query.filter_by(date= date).first()
        sameTime = Booking.query.filter_by(startTime= startTime).first()
        
        if roomNumber == null:
            flash('Please choose a room', category='alert')
        elif  sameRoom == roomNumber and sameDate == date and sameTime == startTime:
            flash('This booking is unavailable please try a different time/date/room', category='alert')
        else:    
            new_Book= Booking(roomId=roomNumber, date = date,bookerId= user, startTime = startTime, endTime= endTime )
            db.session.add(new_Book)
            db.session.commit()

        flash('Booking Added!', category='success')
        
    room = Room.query.all()
    return render_template("createbooking.html", user = current_user, room = room)


@views.route('/addroom', methods=['GET', 'POST'])
@login_required
def addRoom():
    
    if current_user.username == 'Admin':
        room = Room.query.all()
        
        if request.method == 'POST':
            roomN = request.form.get('roomNumber')
            
            if roomN.isdigit() == False:
                flash('Please only enter a number !', category='error')
                
            else:
                new_room = Room(roomNumber=roomN)
                db.session.add(new_room)
                db.session.commit()
                flash('room added!', category='success')

                
    else:    
        flash('You are not authorised to view that page!', category='error')
        return redirect(url_for('views.home'))
    
    return render_template("addroom.html", user = current_user, room = room)


@views.route('/existingbooking', methods=['GET'])
def existingBooking():
    

    bookings = Booking.query.all()
    room = Room.query.all()


    return render_template("existingbooking.html",user = current_user,room = room, booking= bookings)


@views.route('/delete-room', methods=['POST'])
def delete_room():
    room = json.loads(request.data)
    roomId = room['id']
    room = Room.query.get(roomId)
    if room:
        db.session.delete(room)
        db.session.commit()

    return jsonify({})

@views.route('/delete-booking', methods=['POST'])
def delete_booking():
    booking = json.loads(request.data)
    bookingId = booking['id']
    booking = Booking.query.get(bookingId)
    if booking:
        db.session.delete(booking)
        db.session.commit()

    return jsonify({})
