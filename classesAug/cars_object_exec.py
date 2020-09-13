from gitProject.classesAug.car_class_30aug import Car, ElectricCar
from gitProject.classesAug.car_class_30aug import *

car1 = Car("toyota", "highlander", "2020")
print(car1.get_description())
car1.set_color("Red")
print(car1.get_description())
print(car1.read_odometer())

car1.odometer_reading = 1000
print(car1.read_odometer())
print(car1.odometer_reading)

# car1.odometer_reading = 800  # not good practice
car1.set_odometer(120)
print(car1.read_odometer())  # we can put logic in the method
print(car1.odometer_reading)

car1.set_odometer(1500)
print(car1.read_odometer())

print("--------")
car1.increment_odo(279)
print(car1.read_odometer())

ecar1 = ElectricCar("tesla", "model y", "2020")
ecar1.set_color("blue")
print(ecar1.get_description())
print("-------------------")
ecar1.tst_method()

# oop object oriented programming
# class, object, method
# inheritance, (single & multiple classes)
# constructor (__init__())
# self. keyword calls something from current, super() method calls from parent
# overriding(due to inheritance) - rewriting the parent attributes or methods in child class
# python does not allow overloading/ check java method to overload (using same name with different parameters)
# parent can not have child class method
