

from domestic_flight import DomesticFlight

def main():

    flight1 = DomesticFlight(
        "NZ101",
        "Auckland",
        "Wellington",
        "10:30 AM",
        23
    )

    print("===== Air New Zealand Domestic Flight System =====")

    # Inherited methods
    flight1.display_flight_info()
    flight1.flight_status()

    # Child class method
    flight1.display_baggage_info()

if __name__ == "__main__":
    main()