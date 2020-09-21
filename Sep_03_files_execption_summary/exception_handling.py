# exception handling
# 03 sep 1h.40min


def division(a, b):
    try:
        print(a/b)
    except ZeroDivisionError as zerodv:
        print(f"u cant divide by ZERO - err: {zerodv}")
    except (TypeError, NameError) as errmsg:
        print(f"check yur input - err: {errmsg}")
    finally:  # will always be executed in either try or except block
        print("finally block is executed")

division(45, 15)
division(45, 10)
division(45, 0)
division(100, "a")
division(100, 2)
