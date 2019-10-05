#define a function
def my_function_Assignment():
   print ("Hello eveyone in this class hope everyone is doing great! keep up the hard work")
   print ("Thanks to your teacher at university of the people for thier help and support")
   
my_function_Assignment()  # This is My Parameter

# Here is my Arguments

def square(x):
  	return x*x  # As you can see this is my Expression::
print(square(4)) # 

# I am also Declaring arguments here
def multiply(x,y=0):# This Multiple can also be passed an array.
#here i decleare value of this Argument multiply(x,y=0), i assign it value at function definition.

#PLEASE NOTE: 
#Arguments are declare in the function definition. While calling the function.
	print("value of x=",x) 
	print("value of y=",y)
    
	return x*y
  
print(multiply(y=2,x=4)) # Here i am passing arguments


# Example (3)
#Create a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.
 
x = 10
def test1():
	print(x)
	print(x+10)
	
	x+=10
	
test1()

#Result:
#python LocalVariable.py
#Traceback (most recent call last):
#  File "LocalVariable.py", line 10, in <module>
#    test1()
#  File "LocalVariable.py", line 4, in test1
#    print(x)
#UnboundLocalError: local variable 'x' referenced before assignment
#┌─[✗]─[zwanski@parrot]─[~/Documents/Uni]
#└──╼ $


#example5:
#Show what happens when a variable defined outside a function has the same name as a local variable inside a function.
# Explain what happens to the value of each variable as the program runs.

def Mohamed():
	Mohamed = "I am Computer Science Student at Uopeople"
	Print(mohamed)
	
Mohamed()
print(Mohamed)

#Output:
#Traceback (most recent call last):
# File "..\Playground\", line 5, in <module>
#    Mohamed()
#  File "..\Playground\", line 3, in Mohamed
#    Print(mohamed)
#NameError: name 'Print' is not defined

def my_assignment():
	print("I love computer science.")
	print("but at least i trying")
	print("python programming")
	
	for number in range(10):
		# use a if the number is multiple of 3, otherwise use b
		if (number % 3) ==0:
			message = message + a
			else:
				message = message + b
				print (message)
essage = ""
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)

