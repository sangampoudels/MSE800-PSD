# child class

# Import parent class
from flight import Flight

class DomesticFlight(Flight):
    """
    Child class inheriting from Flight.
    """

    def __init__(self, flight_number, origin, destination,
                 departure_time, baggage_allowance):

        # Call parent constructor
        super().__init__(
            flight_number,
            origin,
            destination,
            departure_time
        )

        # Additional attribute
        self.baggage_allowance = baggage_allowance

    def display_baggage_info(self):
        print(f"Baggage Allowance : {self.baggage_allowance} kg")