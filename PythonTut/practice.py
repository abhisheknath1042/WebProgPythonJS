class Flight(object):
	"""docstring for Flight"""
	def __init__(self, capacity):
		# super(Flight, self).__init__()
		# self.arg = arg
		self.capacity=capacity
		self.passengers=[]

	def add_passeger(self, name):
		if not self.open_seats():
			return False

		self.passengers.append(name)
		return True

	def open_seats(self):
		return self.capacity - len(self.passengers)

fly = Flight(3)		

people = ["Ron", "Roon", "Ruud"]	

for person in people:
	success = fly.add_passeger(person)
	if success:
		print(f"Added {person} to flight successfully")
	else:
		print(f"No available seats for {person}")