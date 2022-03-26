# constructor is responsible to allocates memeory to object

class Computer:
    
    def __init__(self):
        self.name = 'saljesh'
        self.age = 21

    def update(self):
        self.age = 23
    
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()


# Comparing age of c1 and c2 object 
# we cant do if c1 == c2  we need own function i.e compare

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

c1.name = 'aney'

c1.update() # by default in prarametes its c1 or whatever is in front before .update()

print(c1.age)
print(c2.name)


