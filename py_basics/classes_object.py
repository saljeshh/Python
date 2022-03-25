# class Myclass:
#     x = 5

# p1 = Myclass()
# print(p1.x)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# name = input("Enter your name")
# age = int(input("Enter your age"))

# p2 = Person(name,age)
# print(p2.name)
# print(p2.age)

# del p2.age

from inheritance import Student

class School(Student):
    pass

p1 = School()
print(p1.name)
