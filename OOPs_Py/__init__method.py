class Computer:

    # this is global
    def __init__(self,cpu,ram):
        print("int init")
        # self is com1 in first and com1 ko ram and cpu will be assigned to new values
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("i5, 16gb, 1TB")
        print("Config is ", self.cpu, self.ram)

# The moment we call class constructor Computer it calls __init__ method once for every

# We are actually passing three parameter
# Computer(com1, i5, 16) // behind the scenes
com1 = Computer('i5',16)
com2 = Computer('i7',8)

com1.config()
com2.config()