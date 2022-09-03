def square(x):
  return x*x

for i in range(10):
  print(f"The square of {i} is {square(i)}")

class Point(object):
	"""docstring for Point"""
	def __init__(self, input1, input2):
		# super(Point, self).__init__()
		# self.arg = arg

		self.x=input1
		self.y=input2
		

p=Point(3,7)
print(p.x)
print(p.y)