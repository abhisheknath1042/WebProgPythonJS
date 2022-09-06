# import array as arr
#
# arr.array()

#from array import *
#import numpy as np
from numpy import *

#############################################################################################################

# vals = array('i',[3,7,23,52])
# newArr = array(vals.typecode, (a*a for a in vals))
# #vals.reverse()
#
# for i in range(len(vals)):
#     print(vals[i])
#
# for e in newArr:
#     print(e)

# print(vals)
#
# print(vals.buffer_info())

#############################################################################################################

# arr = array('i', [])
# n = int(input("Enter length of Array: "))
#
# for i in range(n):
#     x=int(input("Enter the next element: "))
#     arr.append(x)
#
# print(arr)
#
# k=0
# val = int(input("Enter the value for search: "))
# for e in arr:
#     if e==val:
#         print("Match Found")
#         print(k)
#         break
#     k+=1
#
# print("Using func")
# print(arr.index(val))

#############################################################################################################

##Different ways to import array

# array()
# linspace()
# logspace()
# arange()
# zeros()


# arr = linspace(0,15,16)
# print(arr)
#
# arr1 = arange(1,15,2)
# print(arr1)
#
# arr2 = logspace(1,40,5)
# print('%.2f' %arr2[0])
#
# arrZ = zeros(6,int)
# print(arrZ)
#
# arrOne = ones(7,int)
# print(arrOne)
#
#
#############################################################################################################


#adding two arrays
# arr3 = arr2 + arr1
#
# #inbuilt-functions of the array
# print(max(arr2))
# print(sum(arr2))
# print(sin(arr2))


#############################################################################################################

#Copying an Array

arr1 = array([1,2,3,4,5])
arr2 = array([11,22,33,44,55])



arrA = arr1  #aliasing -  copies values and stores in 1 memory block
arrS = arr1.view()  #shallow copy - copies value but in different memory
arrD = arr1.copy()  #deep copy - completely overwrites the second arr


print(arrA)
print(arrS)
print(arrD)




























