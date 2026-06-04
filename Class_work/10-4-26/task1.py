from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def salary(self):
#         pass

# class Raj(Employee):
#     def salary(self):
#         return 10000

# class Prem(Employee):
#     def salary(self):
#         return 15000


# obj = Raj()
# print(obj.salary())

# obj_1 = Prem()
# print(obj_1.salary())

class Vehicle(ABC):
    @abstractmethod
    def color(self):
        pass
    
    @abstractmethod
    def tyre(self):
        pass

class Bike(Vehicle):
    def color(self):
        return "black"
    
    def tyre(self):
        return 2

class Auto_rickshaw(Vehicle):
    def color(self):
        return "Yellow"
        
    
    def tyre(self):
        return 3

class Car(Vehicle):
    def color(self):
        return "White"
    
    def tyre(self):
        return 4

bike = Bike()
print(f"Color of Bike is {bike.color()} and having {bike.tyre()} tyre")

auto = Auto_rickshaw()
print(f"Color of Autorickshaw is {auto.color()} and having {auto.tyre()} tyre")

car = Car()
print(f"Color of Car is {car.color()} and having {car.tyre()} tyre")