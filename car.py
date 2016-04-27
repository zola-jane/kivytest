# CP1404 Car class example


class Car:
    def __init__(self, fuel=0):
        """ initialise a Car instance
        fuel: float, one unit of fuel drives one kilometre """
        self.name = str(self)
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel
        or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        """ returns a formatted string """
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)
