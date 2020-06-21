import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://umyfbuekyusano:1c34505248203c1732612d039c5417d137b440cdf6e819ca78a57a366674e7c2@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d6ab5cg2452pfb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("flights.csv")
    #opennign csv file
    reader = csv.reader(f)
    #lopping over every line in the csv file
    for origin, destination, duration in reader:
        #inserting into the db with python code
        flight = Flight(origin=origin, destination=destination, duration=duration)
        #adding the info to the db
        db.session.add(flight)
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
        #commiting
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        main()
