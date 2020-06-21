import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://umyfbuekyusano:1c34505248203c1732612d039c5417d137b440cdf6e819ca78a57a366674e7c2@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d6ab5cg2452pfb"
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        #writing sql sintax in our pyhton code
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                   {"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.commit()

if __name__ == "__main__":
    main()
