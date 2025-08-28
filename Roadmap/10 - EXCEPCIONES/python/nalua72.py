try:
    print(10/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division performed successfully.")
finally:
    print("Execution completed.")

try:
    print(10/1)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division performed successfully.")
finally:
    print("Execution completed.")

try:
    list1 = [1, 2, 3]
    print(list1[5])
except IndexError:
    print("Index out of range!")
else:
    print("Index in range")
finally:
    print("Execution completed.")

try:
    list1 = [1, 2, 3]
    print(list1[2])
except IndexError:
    print("Index out of range!")
else:
    print("Index in range")
finally:
    print("Execution completed.")


""" EXTRA EXERCISE"""

class NegativeNumber(Exception):
    pass


def check_parameter(param):
    if not isinstance(param, int):
        raise TypeError("Parameter must be an integer")
    elif param < 0:
        raise NegativeNumber("Negative number not allowed")
    else:
        return "Valid parameter"

def main():
    try:
        print(check_parameter(-10))
    except TypeError as te:
        print(te)
    except NegativeNumber as ne:
        print(ne)

    try:
        print(check_parameter("string"))
    except TypeError as te:
        print(te)
    except NegativeNumber as ne:
        print(ne)

    try:
        print(check_parameter(10))
    except TypeError as te:
        print(te)
    except NegativeNumber as ne:
        print(ne)
        
if __name__ == "__main__":
    main()
