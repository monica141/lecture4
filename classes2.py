class Flight:

    #creating a new class with the innit method
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    #printing the information of the flight
    #we take self to know the object we are operating with
    def print_info(self):
        #self refers to the object we are trying to prin information for and the object is the object we take
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")


def main():
    #printing the flight information
    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f1.print_info()

    f2 = Flight(origin="Tokyo", destination="Shanghai", duration=185)
    f2.print_info()


if __name__ == "__main__":
    main()
