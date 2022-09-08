class Student(object):
	"""docstring for Student"""
	def __init__(self, m1, m2):
		self.m1 = m1
		self.m2 = m2

	def __add__(self,other):
		add1 = self.m1 + other.m1
		add2 = self.m2 + other.m2
		s3 = Student(add1,add2)

		return s3

	def __gt__(self,other):
		r1 = self.m1 + other.m1
		r2 = self.m2 + other.m2
		if r1 > r2:
			return True
		else:
			return False

	def __str__(self):
		return "{} {}".format(self.m1, self.m2)


s1 = Student(47,82)
s2 = Student(34,93)

s3 = s1+s2

print(s3.m1)

if s1 > s2:
	print("First Place")
else:
	print("Second Place")


print(s1)
print(s2)