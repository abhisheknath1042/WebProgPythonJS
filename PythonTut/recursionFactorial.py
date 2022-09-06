
#implementing recursion to find factorial

def fact(n):
     if n==0:
         return 1
     else:
         return n*fact(n-1)



x = int(input("Enter a number: "))
result = fact(x)

print("Factorial of {} is {}".format(x,result))