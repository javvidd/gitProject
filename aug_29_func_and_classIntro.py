#  functions continuation
# 29 aug -- 30min done


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


def full_name_dict(first: str, last: str) -> dict:  # this function will return dict data
    """returns dictionary with first and last name"""
    return {"first_name": first.title(), "last_name": last.title()}


student_1 = full_name_dict("anvar", "nosirov")
print(student_1)
print(student_1["first_name"], student_1["last_name"])
