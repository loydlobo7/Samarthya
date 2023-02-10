#creating a class for car and their basic details

class Car:
    def __init__(self, model, horsepower, color, details):
        self.model = model
        self.horsepower = horsepower
        self.color = color
        self.details = details
        
    def get_car_details(self):
        print("Model: ", self.model)
        print("Horsepower: ", self.horsepower)
        print("Color: ", self.color)
        print("Details: ", self.details)


my_car = Car("SUV", 250, "Red", "Luxury model with sunroof")


my_car.get_car_details()
