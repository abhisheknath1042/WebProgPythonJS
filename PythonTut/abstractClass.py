from abc import ABC, abstractmethod

class Computer(ABC):
	#Abstract Method
	@abstractmethod
	def process(self):
		pass

class Laptop(Computer):
    def process(self):
        print("It is running")

class Whiteboard(Computer):
    def write(self):
        print("It is writing")

class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()

# com = Computer()
com1 = Laptop()
com2 = Whiteboard()
# com1.process()

prog1 = Programmer()
prog1.work(com1)

prog1.work(com2)
