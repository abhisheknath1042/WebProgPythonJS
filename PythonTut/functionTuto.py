# def person(name,age=18):
#     print(name)
#     print(age)
#
# person("Ron", 37)

#Variable Length Argument
# def sum(a,*b):
#     c=a
#     for i in b:
#         c=c+i
#     print(c)
#
# sum(2,5,29,10)

#Keyworded Variable Length Arguments
# def person(name, **data):
#     print(name)
#
#     for i,j in data.items():
#         print(i,j)
#
#
# person("Rooney", age=35, city="Manchester", jerseyNo=10)


#Global and Local Values
a=10
b=9
c=3

def something():
    a=9
    x=globals()['a']

    print("Previous Value of A:" , x)
    print("In Func", a)
    globals()['a']=15

something()

print("Outside Func ",a)