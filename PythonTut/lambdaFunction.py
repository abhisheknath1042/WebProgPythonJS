from functools import reduce


#Anonymous Functions - Lambda Functions

# lamFunc = lambda a,b : a*b
#
# result = lamFunc(5,6)
# print(result)

#Using Lambda Functions

# def isEven(n):
#     return n%2==0
#instead of this function use a lambda function

nums = [3,6,34,45,64,2,43,88,12,69]

####

evens = list(filter(lambda n : n%2==0, nums))
print(evens)

####

doubles = list(map(lambda n : n*2, evens))
print(doubles)

####

sumLambda = reduce(lambda a,b : a+b, doubles)
print(sumLambda)