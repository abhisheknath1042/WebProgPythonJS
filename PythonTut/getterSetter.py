class students(object):
	"""docstring for students"""
	school = "Telusko"

	def __init__(self, m1, m2, m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		return (self.m1 + self.m2 + self.m3)/3

	def get_m1(self):
		return self.m1

	def set_m1(self,value):
		self.m1 = value

	@classmethod
	def getSchool(cls):
		return cls.school

	def info():
		print("This is a students class in abc module")

s1 = students(39,45,43)
s2 = students(21,38,49)


print(s1.avg())
print(students.getSchool())