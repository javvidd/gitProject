# classes - chapter 9
# class name always should be capital letter


class Dog():
    """this is general class about dog. """
    # attributes (properties)
    breed = ''
    name = ''

    # behaviour, methods
    def bark(self):
        print("wouf wouff!!")

mydog = Dog()  # mydog is the object of the class

mydog.breed = "german shepard"
mydog.name = "Rex"