# Chapter 3

## Familiar functions
100xp
Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist easier. You already know two such functions: print()and type(). You've also used the functions str(), int(), bool() and float() to switch between data type. These are built-in functions as well.
Calling a function is easy. To get the type of 3.0 and store the output as a new variable, result, you can use the following:
result = type(3.0)


The general recipe for calling functions is thus:
output = function_name(input)


### Instructions
- Use print() in combination with type() to print out the type of var1.
- Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
- Use int() to convert var2 to an integer. Store the output as out2.


## Help!
50xp
Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: help(). In IPython specifically, you can also use ? before the function name.
To get help on the max() function, for example, you can use one of these calls:
help(max)
?max


Use the Shell on the right to open up the documentation on complex(). Which of the following statements is true?


Answer three


## Multiple arguments
100xp
In the previous exercise, the square brackets around imag in the documentation showed us that the imag argument is optional. But Python also uses a different way to tell users about arguments being optional.
Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.
You'll see that sorted() takes three arguments: iterable, key and reverse.
key=None means that if you don't specify the key argument, it will be None. reverse=False means that if you don't specify the reverseargument, it will be False.
In this exercise, you'll only have to specify iterable and reverse, not key. The first input you pass to sorted() will obviously be matched to the iterable argument, but what about the second input? To tell Python you want to specify reverse without changing anything about key, you can use =:
sorted(___, reverse = ___)


Two lists have been created for you on the right. Can you paste them together and sort them in descending order?
### Instructions
- Use + to merge the contents of first and second into a new list: full.
- Call sorted() on full and specify the reverseargument to be True. Save the sorted list as full_sorted.
- Finish off by printing out full_sorted.

## String Methods
100xp
Strings come with a bunch of methods. Follow the instructions closely to discover some of them. If you want to discover them in more detail, you can always type help(str) in the IPython Shell.
A string room has already been created for you to experiment with.
### Instructions
- Use the upper() method on room and store the result in room_up. Use the dot notation.
- Print out room and room_up. Did both change?
- Print out the number of o's on the variable room by calling count() on room and passing the letter "o" as an input to the method. We're talking about the variable room, not the word "room"!
## List Methods
100xp
Strings are not the only Python types that have methods associated with them. Lists, floats, integers and booleans are also types that come packaged with a bunch of useful methods. In this exercise, you'll be experimenting with:
index(), to get the index of the first element of a list that matches its input and
count(), to get the number of times an element appears in a list.
You'll be working on the list with the area of different parts of a house: areas.
### Instructions
Use the index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
Call count() on areas to find out how many times 14.5 appears in the list. Again, simply print out this number.
## List Methods (2)
100xp
Most list methods will change the list they're called on. Examples are:
append(), that adds an element to the list it is called on,
remove(), that removes the first element of a list that matches the input, and
reverse(), that reverses the order of the elements in the list it is called on.
You'll be working on the list with the area of different parts of the house: areas.
### Instructions
- Use append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
-Print out areas
- Use the reverse() method to reverse the order of the elements in areas.
- Print out areas once more.

## Import package
100xp
As a data scientist, some notions of geometry never hurt. Let's refresh some of the basics.
For a fancy clustering algorithm, you want to find the circumference CC and area AA of a circle. When the radius of the circle is r, you can calculate CCand AA as:
C=2πrC=2πr
A=πr2A=πr2
To use the constant pi, you'll need the math package. A variable r is already coded in the script. Fill in the code to calculate C and A and see how the print() functions create some nice printouts.
### Instructions
- Import the math package. Now you can access the constant pi with math.pi.
- Calculate the circumference of the circle and store it in C.
- Calculate the area of the circle and store it in A.

## Selective import
100xp
General imports, like import math, make all functionality from the math package available to you. However, if you decide to only use a specific part of a package, you can always make your import more selective:
from math import pi


Let's say the Moon's orbit around planet Earth is a perfect circle, with a radius r (in km) that is defined in the script.
### Instructions
- Perform a selective import from the math package where you only import the radians function.
- Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. You can calculate this as r∗ϕr∗ϕ, where rr is the radius and ϕϕ is the angle in radians. To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
- Print out dist.

## Different ways of importing
50xp
There are several ways to import packages and modules into Python. Depending on the import call, you'll have to use different Python code.
Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this function as follows:
my_inv([[1,2], [3,4]])


Which import statement will you need in order to run the above code without an error?
Answer Four
