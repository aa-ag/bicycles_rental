from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from webapp import routes


"""

DIVVY CHALLENGE
Import the attached divvy_2013.csv file into a database.
Create a new column for trip_duration
Perform a migration that calculates and persists the trip duration for each trip.
Create a REST endpoint that accepts ‘starttime’ and ‘endtime’ parameters and returns the average duration for that time span in the response.
GET /avg-duration/?start=2013-11-01T12:00:00Z&end=2013-11-02T12:00:00Z
{
average_duration: 172.32
}


If you have time:
Update the endpoint to accept a  ‘from_station_id’ parameter that further filters the results by the stations that the trip started from.  Include the id and name of the station in the response.

"""