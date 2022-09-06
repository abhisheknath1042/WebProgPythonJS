# def announce(f):
# 	def wrapper():
# 		print("About to run the function F")
# 		f()
# 		print("Done with the function")
# 	return wrapper

# @announce
# def hello():
# 	print("Hello, World!")

# hello()

def div(a,b):
    print(a/b)

def smart_Div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner


div= smart_Div(div)
div(2,4)
