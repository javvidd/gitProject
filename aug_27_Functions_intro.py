# functions
# 2h


def greet():
    print("welcome to the class")
    print("__________")


def greet_usr(x):
    """greets the user with given name"""
    print(f"welcome to {x} community")
    print("__________")


def greet_usr1(company, username):
    """greets the user with given name"""
    print(f"Hi {username.title()} welcome to {company.upper()} community ")
    print("_________")


# compName is an optional(keyword) and default val is google
def greet_usr2(username, company_name="google"):
    """greets the user with given name and keyword argument compName=google"""
    print(f"Hi {username.title()} welcome to {company_name.upper()} community ")
    print("__________")


# compName argument is an optional arg and with no default val NONE
def greet_usr3(username, company_name=None):
    """greets the user with given name and keyword argument no default value"""
    if company_name is None:
        print(f"Hi {username.title()} welcome to yur NewHome")
    else:
        print(f"Hi {username.title()} welcome to {company_name.upper()} community ")
    print("__________")


comp = "levelDown"
greet()
greet_usr("levelUp")  # calling function to be executed
greet_usr(comp)
greet_usr1("lgbt", "tony") # giving values by position
greet_usr1(username="tony", company="lgbt")  # defining values by name
greet_usr2("tony")  # function use default value which is google
greet_usr3("polya", "fb")  # without second arg "fb" first condition will return
greet_usr3("ali")

# Package - directory with __init__.py empty file
# Module - ...py file (python file)
