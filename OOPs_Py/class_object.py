"""
class may contain attributes => variables
behaviour => Methods(Function

"""

class Computer:

    def config(self):
        print("i5, 16gb, 1TB")

comp1 = Computer()
comp2 = Computer()

# calling functin of class and passing the object as parameter
Computer.config(comp1)
Computer.config(comp2)

# We can also do (method 2) 
# Behind the scene config will take com1(object) as parameter as above
comp1.config()
comp2.config()
