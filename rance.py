class ComputerBrand:
    def __init__(self, brand_name, model, price):
        self.__brand_name = brand_name  # Private attribute
        self.__model = model            # Private attribute
        self.__price = price            # Private attribute

    # Getter methods to access private attributes
    def get_brand_name(self):
        return self.__brand_name

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    # Setter methods to modify private attributes
    def set_brand_name(self, brand_name):
        if isinstance(brand_name, str):
            self.__brand_name = brand_name
        else:
            print("Invalid brand name. It should be a string.")

    def set_model(self, model):
        if isinstance(model, str):
            self.__model = model
        else:
            print("Invalid model name. It should be a string.")

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be a positive number.")

    # A method to display computer brand details
    def display_computer_info(self):
        print(f"Brand: {self.__brand_name}")
        print(f"Model: {self.__model}")
        print(f"Price: ${self.__price:.2f}")


# Creating a ComputerBrand object
computer = ComputerBrand("Apple", "MacBook Pro", 2500.00)

# Accessing computer brand details using getter methods
computer.display_computer_info()

# Modifying computer details using setter methods
computer.set_brand_name("Dell")
computer.set_model("XPS 15")
computer.set_price(2000.00)

# Displaying updated computer brand details
print("\nUpdated Computer Information:")
computer.display_computer_info()

# Trying to set invalid data (this will show an error message)
computer.set_price(-1000)  # Invalid price
computer.set_brand_name(123)  # Invalid brand name
