class Stduent:

    def __init__(self,name,roll):
        self.nam = name
        self.rol = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.nam, self.rol)
        self.lap.show()

    
    class Laptop:

        def __init__(self):
            self.brand = 'lenovo'
            self.cpu = 'ryzen 7 5800h'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Stduent('saljesh',21)
s2 = Stduent('annika',3)

s1.show()
s2.show()

print(s1.lap.brand)

lap1 = Stduent.Laptop()
