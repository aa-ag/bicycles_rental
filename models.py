from webapp import app, db
from datetime import datetime

class Trip(db.Model):
    trip_id = db.Column(db.Integer, primary_key = True)
    starttime = db.Column(db.DateTime, nullable = True, default="")
    stoptime = db.Column(db.DateTime, nullable = True, default="")
    bikeid = db.Column(db.Integer, nullable = True, default="") 
    from_station_id = db.Column(db.Integer, nullable = True, default="")
    to_station_id = db.Column(db.Integer, nullable = True, default="")
    to_station_name = db.Column(db.String(150), nullable = True, default="")
    usertype = db.Column(db.String(100), nullable = True, default="Customer")
    gender = db.Column(db.String(30), nullable = True, default="")
    birthday = db.Column(db.String(12), nullable = True, default="")
    trip_duration = db.Column(db.Integer, nullable=True, default="")
    
    def __init__(self, trip_id, starttime, stoptime, bikeid, from_station_id, to_station_id, to_station_name, usertype, gender, birthday, trip_duration):
        self.trip_id = trip_id
        self.starttime = starttime
        self.stoptime = stoptime
        self.bikeid = bikeid
        self.from_station_id = from_station_id
        self.to_station_id = to_station_id
        self.to_station_name = to_station_name
        self.usertype = usertype
        self.gender = gender
        self.birthday = birthday
        self.trip_duration = trip_id