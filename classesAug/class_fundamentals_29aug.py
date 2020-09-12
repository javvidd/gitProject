# classes - chapter 9
# class - general template, of certain real life objects
# class name always should be capital letter


class Dog():
    """this is general class about dog. """
    # attributes (properties)
    breed = ''
    name = ''

    # behaviour, methods
    def bark(self):
        print("wouf wouff!!")

# object is the instance (representation in specific case) of the class
my_dog = Dog()  # mydog is the object of the class
my_dog.breed = "german shepard"
my_dog.name = "Rex"
my_dog.bark()

your_dog = Dog()
your_dog.name = "vova"
your_dog.breed = "french bulldog"
your_dog.bark()
