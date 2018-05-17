#SensorEd Workshop V0.1
#Author - Jacob Ulasevich
#Variable Introduction


"""
Variable are one of the most important features in programming.
In short, they allow you to store and manipulate data.
"""

"""
While there are many different type of variables in programming
languages, today we will be going over 4.
"""

#The following is an INTEGER variable.
a = 5
#The following is a DOUBLE variable.
b = 3.14
#The following is a STRING variable.
c = "Hello World"
#The following is a BOOLEAN variable.
d = False


print("Integer: " + str(a) + "\n"
      "Double: " + str(b) + "\n"
      "String: " + c + "\n"
      "Boolean: " + str(d))
#Press F5 to save and run your program.


"""
What do you think the differences between each variable is?
If you notice we had to put a str() around the number variables to
turn it into a string to it could be printed, this is called a function
and we will go in depth with that later.
"""

"""
Now that you know how variables work assign some variables of your own below
and make your own print statment to have the computer display them.
"""


"""
One final thing to note about variables.  You cannot add a string and an
integer/variable.  Lets see what happens when we try to add an integer and
a double.
"""


#Make x a double variable 
x = 7.11
#Make y an integer variable
y = 7
z = x + y
print("Result: " + str(z))


"""
What did you notice about the result?
"""

"""
Finally, lets add two strings together.
"""


#Assign stringOne a word or sentence
stringOne = "Natalie"
#Assigne stringTwo a word or sentence
stringTwo = " Union City"
print("Result: " + stringOne + stringTwo)

"""
Variables are the foundation of computer programming.  Without them
it would be very difficult to get the computer to understand what you
are trying to accomplish.  Be sure to keep an eye out as we manipulate
more variables throughout this workshop.
"""
c = 8
f = 10
print("Result: " + str(c) + str(f))
