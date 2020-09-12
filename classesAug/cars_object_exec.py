from gitProject.classesAug.car_class_30aug import Car

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

car1.increment_odo(279)
print(car1.read_odometer())