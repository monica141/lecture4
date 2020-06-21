#creating a class called flight
class Flight:

    #creating a method that is performed on individual flights
    #init method is built in python, which describes what happens when we want to create a flight
    #other arguments built as we want to store each flights information
    def _init_(self, origin, destination, duration):
        #self is out object and we are settign the propertu to self.origin
        self.origin = origin
        self.destination = destination
        self.duration = duration
