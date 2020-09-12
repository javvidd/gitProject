# classes - chapter 9
# class - general template, of certain real life objects
# class name always should be capital letter
# 30 aug classes 40min


class Dog():
    """this is general class about dog. """
    # attributes (properties)
    breed = ''
    name = ''

    # behaviour, methods
    def bark(self):
        print("wouf wouff!!")


class NewDog():
    """this is new class about dog with mandatory parameters."""

    def __init__(self, name, age):  # initiation/ constructor
        self.name = name
        self.age = age
        print("construction the dog class")

    # behaviour, methods
    def bark(self):
        print(f"{self.name} is barking like wouf wouff!!")

    def get_name(self):
        print(self.name)



# object is the instance (representation in specific case) of the class
dog1 = Dog()  # mydog is the object of the class/ obj instantiation from class
dog1.breed = "german shepard"
dog1.name = "Rex"
# dog1.bark()

dog2 = Dog()
dog2.name = "vova"
dog2.breed = "french bulldog"
# dog2.bark()

print("Name of dog1", dog1.name)
print("Breed of dog1", dog1.breed)
dog1.bark()

print("Name of dog2", dog2.name)
print("Breed of dog2", dog2.breed)
dog2.bark()

print("----------------")
dog3 = NewDog(age=4, name="capone")
dog3.bark()
dog3.get_name()
dog4 = NewDog("hatiko", 5)
dog4.bark()
dog4.get_name()

