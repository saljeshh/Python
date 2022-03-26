# Instance method  -> works with object (static)
# class method
# static method


class Student:

    school = 'Tech'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    # Accessors
    def get_m1(self):
        return self.m1

    # Mutators
    def set_m1(self, value):
        self.m1 = value

    # In class method in paranthesis we need to write cls only not any other insted of self i.e in object 
    # decorators
    @classmethod
    def getSchool(cls):
        return cls.school

    # this is static method nth in paranthesis
    @staticmethod
    def info():
        print("This is student class... in abc module")

std1 = Student(32,45,56)
std2 = Student(44,78,90)


print(std1.avg())
print(std2.avg())

#printing values
print(std1.m1)

print(Student.getSchool())

Student.info()
