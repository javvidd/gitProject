# 30 aug car class starts at 41min
# 30 aug done
# 30 aug classes - 1h.40min at 1h.35min explains exercises in chapter 9


class Car():
    """this is class to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = "white"
        self.odometer_reading = 0  # in miles

    # getter(return some info) and setter(assign new val)
    def get_description(self):
        msg = f"your car:\n\tmanufacturer: {self.make}\n\tmodel: {self.model}\n\tyear: {self.year}\n\tcolor: {self.color}"
        return msg

    def set_color(self, new_color):
        print(f"changing the color {self.color} to {new_color}")
        self.color = new_color  # this line sets the new val

    def read_odometer(self):
        """gets the odometer value of the car"""
        msg = f"Car has {self.odometer_reading} miles on it."
        return msg

    def set_odometer(self, new_miles):
        """sets the odometer value with if logic"""
        if new_miles >= self.odometer_reading:
            print(f"Setting odometer from {self.odometer_reading} to {new_miles} miles.")
            self.odometer_reading = new_miles  # sets the new val
        else:
            print(f"you can not roll back the odo from {self.odometer_reading} to {new_miles}")

    def increment_odo(self, miles):
        """incrementing miles to odometer_reading"""
        # self.odometer_reading = self.odometer_reading + miles
        if miles > 0:
            self.odometer_reading += miles
            print(f"incremented by additional {miles} miles")
        else:
            print(f"{miles} is a negative value, u cant roll back your odometer")


class ElectricCar(Car):  # inheriting Car class
    """ElectricCar inherits all features of Car() class"""

    def __init__(self, make, model, year): # it called signature also
        """child class constructor, can OVERRIDE the parent class constructor"""
        super().__init__(make, model, year)  # calls the constructor of parent class
        self.battery_size = 100
        # self.make = make
        # self.model = model

    def get_description(self):  # overriding the parent method
        msg = f"your car:\n\tmanufacturer: {self.make}\n\tmodel: {self.model}\n\tyear: {self.year}\n\tcolor: {self.color}\n\tBattery size: {self.battery_size}"
        return msg

    def tst_method(self):
        print(self.get_description())  # current class get_description()/ with battery size
        print(super().get_description())  # parent class get_description()

