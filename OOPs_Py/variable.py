# Namespace is an area where you create and store object/variable

class Car:
    #if we define variable inside class it becomes class variables

    wheels = 4

    #if we define variable inside __init__ it becomes instance variables
    def __init__(self):
        self.mileage = 10
        self.company = "BMW"

c1 = Car()
c2 = Car()

c1.mileage = 9

Car.wheels = 12

# We can use either object name or class name for class variables
print(c1.company, c1.mileage ,c1.wheels)
print(c2.company, c2.mileage, Car.wheels)