def is_divisible(x, y):
    pass

def is_power(a, b):
    pass
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))

#Output:
#('is_power(10, 2) returns: ', None)
#('is_power(27, 3) returns: ', None)
#('is_power(1, 1) returns: ', None)
#('is_power(10, 1) returns: ', None)
#('is_power(3, 3) returns: ', None)


#Does the submission implement an is_power function that takes two arguments?
#Answer: Yes

#Does the is_power function call is_divisible?

#Aswer:
#If a == 1 this returns true because of base one. 
#If a is not 1 then this will look at b if b is one it will only return true is a is one.
#Alone this returns True for is_power(1, 1), but false for is_power(10, 1).

#Does the is_power function call itself recursively?
#Answer:Yes, Recursive functions take a while to get used to. It can help to add some print statements to the functions

#Does the is_power function include code for the base case of the two arguments being equal?
#Answer: Yes, which looks like this 
#def is_power(a, b):
    #if a == 1:
        #return True

    #if b == 1:
        #return a == 1
#Does the is_power function include code for the base case of the second argument being "1"?
#Answer:
#Yes

#Does the submission include correct output for the five test cases?
#Answer: Yes
#Here! ('is_power(10, 2) returns: ', None)
#('is_power(27, 3) returns: ', None)
#('is_power(1, 1) returns: ', None)
#('is_power(10, 1) returns: ', None)
#('is_power(3, 3) returns: ', None
