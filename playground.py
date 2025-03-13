def add(*args):
    # s=0
    # for n in args:
    #    s+=n
    return sum(args)

# my_range = range(1,5)
# print(*my_range)
# print(add(*my_range))

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

calculate(4, add=3, multiply=4)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")

my_car = Car(make="nissan")
print(my_car.model)