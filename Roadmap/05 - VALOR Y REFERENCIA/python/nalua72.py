#Variables by value. Inmutable variables (int, float, string)
a = 1
b = a
print(f"a: {a}, b: {b}")
b += 2
print(f"a: {a}, b: {b}")

#Variables by reference. Mutable variables (list, tuple, set)
list_a = [10, 20]
list_b = list_a
print(f"list_a: {list_a}, list_b: {list_b}")
list_b.append(40)
print(f"list_a: {list_a}, list_b: {list_b}")

#Function with parameter as value

def func_value(x: int):
    x += 1
    print(f"x: {x}") 

a = 10
print(f"a before: {a}")
func_value(a)
print(f"a after: {a}")

#Function with parameter as reference
def func_reference(x_list: list):
    x_list.append(40)
    print(f"x_list: {x_list}")

a_list: list = [10, 20]
print(f"a_list before: {a_list}")
func_reference(a_list)
print(f"a_list after: {a_list}")



""" EXTRA """

def value_func(x: int, y: int) -> tuple:

    x, y = y, x

    return x, y

def reference_func(x: list, y: list) -> tuple:

    x, y = y, x

    return x, y


def main ():

    a: int = 4
    b: int = 5

    c, d = value_func(a, b)

    print(f"var1: {a}, var2: {b}, var3: {c}, var4: {d}")

    list1: list = [1,2,3]
    list2: list = [4,5,6]

    list3, list4 = reference_func(list1, list2)

    print(f"list1: {list1}, list2: {list2}, list3: {list3}, list4: {list4}")



if __name__ == "__main__":
    main()  