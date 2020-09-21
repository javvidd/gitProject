# summary of python
# next is Selenium package
# sep-03 1h.20min python summary files, exceptions
# import abc
#
# students = ["akmal", "lenur", "said"]
# cars = {"car1": "corolla", "car2": "optima"}
#
# print(len(students))  # len is polymorphism here since it has been used for different purposes
# print(len(cars))
# print(students, cars)
#
#
# class Shape(metaclass=abc.ABCMeta):
#     classmethod
#
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width


# using with open() as random_name: saves memory
# using just open will keep using memory and if opened file is big it will overflow the stack
with open("data/inputData.txt") as saved_in_memory_as:
    # # option 1 using for loop
    # counter = 1
    # for line in saved_in_memory_as:
    #     print("Line: " ,counter, line)
    #     counter +=1

    # # option 2 printing saved data
    contents = saved_in_memory_as.read()  # it will read line by line
    print(contents)

print(contents)
print("reading a inputData.txt file completed")
print("now printing line by line: ")

# writing to the file
filename = "data/inputData.txt"
with open(filename, "w") as file_object:  # w rewrites whole file
    file_object.write("i said do u wanna fight?")

with open(filename, "a") as new_obj:  # a appends new line
    new_obj.write("\ni said do u wanna catch this hand?")
