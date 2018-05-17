#SensorEd Workshop V0.1
#Author - Jacob Ulasevich
#Function Introduction

"""
Functions allow you to write bits of code that will only be used when
you call the function, if you don't call the function it won't be ran!

Think of a programming function just like a math function.  There's inputs
(called parametere) and an output which is given in a raturn statement.
"""


def printHelloWorld():
    print("Hello World")
    
#Call the function simply by typing the name
printHelloWorld()


"""
This basic function just executes the code inside it's body, lets move
on to something a little more complicated.
"""

'''
def sumNumbers(x, y):
    result = x + y
    return result
'''
"""
This function has paramters x and y.  We are assuming they are numbers we
can later add togwther.  We add them together in the body of the function
and return the variable labeled result.
"""

'''
variableOne = input("Enter a number: ")
variableTwo = input("Enter another number: ")

sumOfVariables = sumNumbers(variable0ne, variableTwo)
print("Result: " + str(sumOfVariables))
'''


"""
There can be any number of paramteres you want and they all don't
have to be the same variable type.
"""

''''
def printMultipleTimes(counter,countUpTo,word):
    while(counter < countUpTo):
        print(word)
        counter += 1
        

printMultipleTimes(0,10,"Hello")
'''


def printName(month,day,name):
    while(month < day):
        print(name)
        month += 2

printName(7,11, "Natalie")




"""
The possibilites of functionare endless!  Make your own function below and
run your code to see what you can make.
"""
