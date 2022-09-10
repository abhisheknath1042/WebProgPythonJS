##### Threads Without Class #####

# from threading import *
#
# def new():
#     for i in range(6):
#         print("Child Executing...", current_thread().getName())
#
#
# t1 = Thread(target=new)
#
# print(current_thread().getName())
#
# t1.start()
# t1.join()
#
# print("Bye", current_thread().getName())


#####################################################

### By Extending Thread Class ###

# from threading import *
#
# class A(Thread):
#     def run(self):
#         for x in range(6):
#             print("Child = ", current_thread().getName())
#
#
# obj = A()
# obj.start()
# obj.join()
#
# print("Control Returned to: ", current_thread().getName())


########################################################

### Without Extending Thread Class ###

from threading import *

class ex:
    def B(self):
        lst = [2,1,'w', 9,4,'xyz']
        for x in lst:
            print("Child Printing: ",x)

myObj = ex()

t1 = Thread(target=myObj.B)
t1.start()
t1.join()

print("Done.")


#############################################################

##### Time Comparision #####

from time import *
from threading import *

def func(n):
    for i in n:
        print(i%2)

def func1(n):
    for i in n:
        print(i%3)


n = [2,4,5,9]

s=time()

func(n)
func1(n)

print(time()-s)