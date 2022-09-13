from time import *

#####  Bubble Sort  #####

def bubbleSort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp


nums = [5,4,7,3,1,5,9,2]
t=time()
bubbleSort(nums)

print("Sorted List using Bubble Sort is: ", nums, time()-t)

###################################################################

#####  Selection Sort  #####

def selectionSort(numList):
    for i in range(len(numList)-1):
        minPos=i
        for j in range(i, len(numList)):
            if numList[j] < numList[minPos]:
                minPos=j

        tempVar = numList[i]
        numList[i] = numList[minPos]
        numList[minPos] = tempVar


numList = [5,4,7,3,1,5,9,2]
t1=time()
selectionSort(numList)

print("Sorted List using Selection Sort is: ", numList, time()-t1)