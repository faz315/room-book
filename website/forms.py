from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, DateField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_login import current_user
from website.models import *
import datetime


class RoomChoiceIterable(object):
    def __iter__(self):
        rooms=Room.query.all()
        choices=[(room.id,room.roomNumber) for room in rooms] 
        for choice in choices:
            yield choice
            
class BookingForm(FlaskForm):
    rooms=SelectField('Choose room',coerce=int,choices=RoomChoiceIterable())
    date=DateField('Choose date', format="%m/%d/%Y",validators=[DataRequired()])
    startTime=SelectField('Choose starting time(in 24hr expression)',coerce=int,choices=[(i,i) for i in range(9,19)])
    duration=SelectField('Choose duration of the booking(in hours)',coerce=int,choices=[(i,i) for i in range(1,6)])
    submit=SubmitField('Book')

    def validate_date(self,date):
        if self.date.data<datetime.datetime.now().date():
            raise ValidationError('You can only book for day after today.')