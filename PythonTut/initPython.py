class Computer:
    def __init__(self):
        self.age = 34
        self.name = "Rooney"

    def update(self):
        self.age =30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age =37
c2 = Computer()

c1.name = "Ronaldo"
c1.age = 37

if c1.compare(c2):
    print("They are same!")
else:
    print("They are different")

c1.update()

print(c1.name)
print(c2.name)