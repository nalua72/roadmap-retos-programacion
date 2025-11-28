""" EJERCICIO """


# Decorador sin parametro

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("codigo antes de la funcion")
        func(*args, **kwargs)
        print("Codigo despues de la funcion")
    return wrapper

        
@my_decorator
def print_name(name):
    print(f"Hola mi nombre es {name}")


print_name("Jose")


# Decorador con parametro

def age_decorator(min_age):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) >= 2:
                age = args[1]
            elif "age" in kwargs:
                age = kwargs["age"]
            else:
                raise ValueError("No se ha proporcionado 'edad'")

            if age < min_age:
                name = args[0]
                print(f"{name} es menor de edad")
                return
            return func(*args, **kwargs)
        return wrapper
    return my_decorator

@age_decorator(18)
def driving_license(name, age):
    print(f"{name} puede sacarse el carnet de conducir")

driving_license("Jose", 23)
driving_license("Luis", 12)


""" EXTRA """

def func_counter_v1(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(f"La funcion {func.__name__} se ha llamado {count} veces")
        return func()
    return wrapper

def func_counter_v2(func):
    def wrapper():
        wrapper.count += 1
        print(f"La funcion {func.__name__} se ha llamado {wrapper.count} veces")
        return func()
    
    wrapper.count =0
    return wrapper

@func_counter_v1
def test_func1():
    ...

@func_counter_v2
def test_func2():
    ...

def main():
    
    for i in range(10):
        test_func1()

    for i in range(10):
        test_func2()


if __name__ == "__main__":
    main()