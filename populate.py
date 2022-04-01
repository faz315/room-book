from website import db
from website.models import *

# add admin & users
user=User(id=1,username='Admin',fullname='Admin')
user.set_password('Admin12')
db.session.add(user)
user=User(id=2,username='apple',fullname='Apple')
user.set_password('Apple123')
db.session.add(user)
user=User(id=3,username='bob',fullname='Bob')
user.set_password('Bob546')
db.session.add(user)


# add rooms
room=Room(id=1,roomNumber='room1',projector=True, capacity=12)
db.session.add(room)
room=Room(id=2,roomNumber='room2',projector=True, capacity=8)
db.session.add(room)
room=Room(id=3,roomNumber='room3',projector=False, capacity=10)
db.session.add(room)
room=Room(id=4,roomNumber='room4',projector=True, capacity=20)
db.session.add(room)

# # add past bookings
# booking=Booking(id=9,title='past meeting',roomId=2,bookerId=2,date=datetime(2018,2,15),startTime=10,endTime=14,duration=4)
# db.session.add(booking)


# # add future bookings
# booking=Booking(id=15,title='future meeting1',roomId=2,bookerId=2,date=datetime(2018,3,15),startTime=11,endTime=14,duration=3)
# db.session.add(booking)

db.session.commit()