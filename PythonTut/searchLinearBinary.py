#####  Linear Search  #####

# def search(lst,n):
#     for i in lst:
#         if i==n:
#             return True
#
# linearList = [5,8,4,6,9,2]
#
# n = 9
#
# if search(linearList,n):
#     print("Found")
# else:
#     print("Not Found")

#######################################################################

#####  Binary Search  #####

pos = -1

def binarySearch(binaryList,f):
    l=0
    u=len(binaryList)-1

    while l<=u:
        mid = (l+u)//2

        if binaryList[mid] == f:
            globals()['pos'] = mid
            return True
        else:
            if binaryList[mid] < f:
                l=mid+1
            else:
                u=mid-1

    return False


binaryList = [2,5,8,33,45,78,98]
f = 21

if binarySearch(binaryList,f):
    print("Found at: ", pos+1)
else:
    print("Not Found")

