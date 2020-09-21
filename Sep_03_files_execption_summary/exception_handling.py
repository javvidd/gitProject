# exception (errors) handling
# 03-Sep - Done


def division(a, b):
    try:
        print(a/b)
    except ZeroDivisionError as zerodv:
        print(f"u cant divide by ZERO - err: {zerodv}")
    except (TypeError, NameError) as errmsg:
        print(f"check yur input - err: {errmsg}")
        # raise errmsg  # will show regular error message
    finally:  # will always be executed in either try or except block
        print("finally block is executed")

division(45, 15)
division(45, 10)
division(45, 0)
division(100, "a")
division(100, 2)

filename = "dat/inputData.txt"
try:
    with open(filename) as input_data:
        contents = input_data.read()  # it will read line by line
        print(contents)
except FileNotFoundError as noFile:
    print(f"filename compromised - {noFile}")
