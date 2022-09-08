class Student(object):
    """docstring for Student"""

    def __init__(self, name, rno):
        self.name = name
        self.rno = rno
        self.lap = self.Laptop

    def show(self):
        print(self.name, self.rno)

    class Laptop(object):
        """docstring for Laptop"""

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Rooney', 10)
s2 = Student('Ronaldo', 7)

s1.show()

lap1 = Student.Laptop()

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))


