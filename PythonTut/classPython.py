class Computer(object):
    """docstring for Computer"""

    def __init__(self, cpu, ram):
        self.cpu1 = cpu
        self.ram1 = ram

    def config(self):
        print("Config is ", self.cpu1, self.ram1)



comp1 = Computer('i5',16)
comp2 = Computer('Ryzen 3', 8)

# Two ways of calling member function
comp1.config()
# Computer.config(comp1)
comp2.config()