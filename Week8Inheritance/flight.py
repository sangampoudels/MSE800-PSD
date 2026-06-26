#parent class

class Flight:
    """
    Parent class representing a general flight.
    """

    def __init__(self, flight_number, origin, destination, departure_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time

    def display_flight_info(self):
        print("\n----- Flight Information -----")
        print(f"Flight Number : {self.flight_number}")
        print(f"Origin        : {self.origin}")
        print(f"Destination   : {self.destination}")
        print(f"Departure Time: {self.departure_time}")

    def flight_status(self):
        print("Flight Status : On Time")