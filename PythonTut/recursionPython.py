import sys

sys.setrecursionlimit(1200)
print(sys.getrecursionlimit())

#global variable
i=0

def greet():
    global i #accessing a global variable and editing it
    i+=1
    print("Hello", i)
    greet()   #recurison


greet()


