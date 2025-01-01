# from abc import ABC,abstractmethod
# class car(ABC):
#     def mileage(self):
#         print("The mileage is 30kmph")
# class Suzuki(ABC):
#     def mileage(self):
#         print("The mileage is 25kmph")
# class duster(ABC):
#     def mileage(self):
#         print("The mileage is 24kmph")
# s=Suzuki()
# s.mileage()

# d=duster()
# d.mileage()


# from abc import ABC,abstractmethod
# class polygon(ABC):
#     def sides(self):
#         pass
# class triangle(polygon):
#     def sides(self):
#         print("triangle has 3 side")
# class rectangle(polygon):
#     def sides(self):
#         print("rectangle has 4 side")
# class pentagon(polygon):
#     print("polygon has 5 side")
# t=triangle()
# t.sides()
# r=rectangle()
# r.sides()
# p=pentagon()
# p.sides()                                         

                            #  decorater

from abc import ABC,abstractmethod
class Animal(ABC):
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        return "Bark"
        
dog=dog()
print(dog.sound())    