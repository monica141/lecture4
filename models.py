from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#db.model is allowing to know that the flight class has some relation with SQLAlchemy
class Flight(db.Model):
    #the correspondance of the table name, in this class the table flight
    __tablename__ = "flights"
    #listing all the column name of the table flight
    id = db.Column(db.Integer, primary_key=True)
    #string value
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    #foreinkey referencing the id column of our flight table
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
