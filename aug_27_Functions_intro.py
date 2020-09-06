import time

# def first_tst():
# #     """greets the usr"""
# #     print("welcome home lol")
# #
# # def first_tst1(name):
# #     """greeting the user with given name"""
# #     print(f"welcome home {name}")
#
# first_tst()
# first_tst1(input("please enter name: "))


def first_tst2(company, username=None):
    """greeting the user with given name"""
    if username is None:
        print(f"heyy welcome back to {company.upper()}!")
    else:
        print(f"{username.title()} welcome back to {company.upper()}!")


first_tst2("ge", "yooo")
first_tst2("pw")
