# from threading import *
# from time import sleep
#
# class Hello(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hello ")
#             sleep(1)
#
# class Hi(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hi ")
#             sleep(1)
#
#
# t1 = Hello()
# t2 = Hi()
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# t1.join()
# t2.join()
#
# print("Bye")


#Different Example

from time import *
from threading import *

def square(numbers):
    print("Calculating Squares: ")
    for n in numbers:
        sleep(0.2)
        print('Square: ', n*n)

def cube(numbers):
    print("Calculating Cubes: ")
    for n in numbers:
        sleep(0.2)
        print('Cube: ', n*n*n)

arr = [2,3,4,5]

t=time()
t1 = Thread(target=square, args=(arr,))
t2 = Thread(target=cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Completed in: ", time() -t)

