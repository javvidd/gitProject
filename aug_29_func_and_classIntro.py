#  functions continuation
# 29 aug -- 1h50min done


def full_name(first, last):
    """returns full name"""
    return f"{first.title()} {last.title()}"


full_name("tony", "marie")
name = full_name("john", "doe")
print(f"{name}, welcome to the class")


def add(a, b):
    return a + b


total = add(2, 4)
print(f"Total is {total}")


# def full_name_dict(first, last) will work perfectly fine
def full_name_dict(first: str, last: str) -> dict:  # this function will return dict data and with string as data type
    """returns dictionary with first and last name and string data type is must"""
    return {"first_name": first.title(), "last_name": last.title()}


student_1 = full_name_dict("anvar", "nosirov")
print(student_1)
print(student_1["first_name"], student_1["last_name"])

nums = [5, 55, 76, 1, -9, 0, 1, 456]
# for x in nums:
#     if x == 1:
#         print("found")
def find_num(x, y):
    for num in x:
        if num != y:
            pass
        else:
            print(f"yes we found {y}")
            break
find_num(nums, 1)

def desc_pizza(*toppings):
    print("we hav only cheese pizza: ")
    print(*toppings)
desc_pizza("pepperoni", "reqular", "bbq")

print("hello", 45, ["john, doe"])

