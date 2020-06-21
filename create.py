import os

from flask import Flask, render_template, request
#here we are importing everything from models file
from models import *

app = Flask(__name__)
#teling flaskalquemy on what database to use
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://umyfbuekyusano:1c34505248203c1732612d039c5417d137b440cdf6e819ca78a57a366674e7c2@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d6ab5cg2452pfb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#tying the database with the flask application
db.init_app(app)

def main():
    #creating tables based on our models file
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        main()
