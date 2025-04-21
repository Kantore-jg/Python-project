# def add(*args):
#     somme = 0
#     for n in args:
#         somme+=n
#     return somme
#
# print(add(2,3,4,5))

# def calculate(n,**kwargs):
#     # for key,value in kwargs.items():
#     #     # print(key)
#     #     # print(value)
#     n+=kwargs["add"]
#     n*=kwargs["multiply"]
#     print(n)
#
# calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kwargs):
        self.color = kwargs.get("color")
        self.model = kwargs.get("model")
        self.price = kwargs.get("price")

my_car = Car(color="black",model="GT-R",price=1000000)
print(my_car.price)
