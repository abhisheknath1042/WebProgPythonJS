class A:
    def __init__(self):
        print("Inside a Base INIT")

    def feature1(self):
        print("Base Class in Inheritance")

class B(A):
    ## Super is used to access the INIT in Parent Class
    def __init__(self):
        super().__init__()

    def feature3(self):
        print("Single Level Inheritance")

    def feature4(self):
        print("Child Class")

class B1:
    def __init__(self):
        print("Inside a Child INIT")

    def feature1(self):
        print("Same feature in B1")

    def featureB1(self):
        print("Child Class")

class C(B):
	def feature5(self):
		print("Multilevel Inheritance")

class D(A,B1):
    ## Here since there are 2 parents Method Resolution Order is used (MRO)
    def __init__(self):
        super().__init__()

    def feature6(self):
        print("Multiple Inheritance")

    def feat(self):
        super().feature1()

#Types of Inheritance

# a1 = A()
#
# a1.feature1()
# a1.feature2()

#Single Level Inheritance
# b1 = B()
#
# b1.feature3()
# b1.feature1()

#Multi Level Inheritance
# c1 = C()
# c1.feature5()
# c1.feature1()

#Multiple Inheritance
# d1 = D()
# d1.feature6()
# d1.feature1()


#Constructors in Python using INIT
a1 = A()

## Super is used to access the INIT in Parent Class
a2 = B()

a3 = B1()

## Here since there are 2 parents Method Resolution Order is used (MRO)
a4 = D()

# Using super() for funciton overloading using MRO
a4.feat()