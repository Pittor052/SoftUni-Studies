class Vehicle:
    def __init__(self, vehicle_type, model, price):
        self.price = price
        self.model = model
        self.type = vehicle_type
        self.owner = None

    def buy(self, money, owner):
        if money >= self.price and not self.owner:
            self.owner = owner
            result = f"Successfully bought a {self.type}. Change: {money - self.price :.2f}"
        elif money < self.price and not self.owner:
            result = f"Sorry, not enough money"
        else:
            result = "Car already sold"

        return result

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            result = f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            result = f"{self.model} {self.type} is on sale: {self.price}"
        return result


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)