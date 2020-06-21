import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://umyfbuekyusano:1c34505248203c1732612d039c5417d137b440cdf6e819ca78a57a366674e7c2@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d6ab5cg2452pfb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    #select query with python
    flights = Flight.query.all()
    #loop through each flight
    for flight in flights:
        #and for each individual flight we print the following
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    with app.app_context():
        main()
