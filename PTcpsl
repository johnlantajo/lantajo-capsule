class PlaneTicket:
    def __init__(self, passenger_name, flight_number, ticket_price):
        self.__passenger_name = passenger_name  
        self.__flight_number = flight_number    
        self.__ticket_price = ticket_price     

   
    def get_passenger_name(self):
        return self.__passenger_name

    def get_flight_number(self):
        return self.__flight_number

    def get_ticket_price(self):
        return self.__ticket_price

   
    def set_passenger_name(self, name):
        if isinstance(name, str):
            self.__passenger_name = name
        else:
            print("Invalid name. It should be a string.")

    def set_flight_number(self, flight_number):
        if isinstance(flight_number, str):
            self.__flight_number = flight_number
        else:
            print("Invalid flight number. It should be a string.")

    def set_ticket_price(self, price):
        if price > 0:
            self.__ticket_price = price
        else:
            print("Ticket price must be a positive number.")

   
    def display_ticket_info(self):
        print(f"Passenger Name: {self.__passenger_name}")
        print(f"Flight Number: {self.__flight_number}")
        print(f"Ticket Price: ${self.__ticket_price:.2f}")



ticket = PlaneTicket("Alice Johnson", "AA123", 300.00)


ticket.display_ticket_info()


ticket.set_passenger_name("Bob Smith")
ticket.set_flight_number("BA456")
ticket.set_ticket_price(350.00)


print("\nUpdated Ticket Information:")
ticket.display_ticket_info()

ticket.set_t
