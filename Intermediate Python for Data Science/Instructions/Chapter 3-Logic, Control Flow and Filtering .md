# Logic, Control Flow and Filtering
## Equality
100xp
To check if two Python values, or variables, are equal you can use ==. To check for inequality, you need !=. As a refresher, have a look at the following examples that all result in True. Feel free to try them out in the IPython Shell.
2 == (1 + 1)
"intermediate" != "python"
True != False
"Python" != "python"


When you write these comparisons in a script, you will need to wrap a print() function around them to see the output.
### Instructions
In the editor on the right, write code to see if True equals False.
Write Python code to check if -5 * 15 is not equal to 75.
Ask Python whether the strings "pyscript" and "PyScript" are equal.
What happens if you compare booleans and integers? Write code to see if True and 1 are equal.

##  Greater and less than
100xp
In the video, Filip also talked about the less than and greater than signs, <and > in Python. You can combine them with an equals sign: <= and >=. Pay attention: <= is valid syntax, but =< is not.
All Python expressions in the following code chunk evaluate to True:
3 < 4
3 <= 4
"alpha" <= "beta"


Remember that for string comparison, Python determines the relationship based on alphabetical order.
### Instructions
Write Python expressions, wrapped in a print() function, to check whether:
x is greater than or equal to -10. x has already been defined for you.
"test" is less than or equal to y. y has already been defined for you.
True is greater than False.
## Compare arrays
100xp
Out of the box, you can also use comparison operators with Numpy arrays.
Remember areas, the list of area measurements for different rooms in your house from the previous course? This time there's two Numpy arrays: my_house and your_house. They both contain the areas for the kitchen, living room, bedroom and bathroom in the same order, so you can compare them.
### Instructions
Using comparison operators, generate boolean arrays that answer the following questions:
Which areas in my_house are greater than or equal to 18?
You can also compare two Numpy arrays element-wise. Which areas in my_house are smaller than the ones in your_house?
Make sure to wrap both commands in a print() statement, so that you can inspect the output.
##  and, or, not (1)
100xp
A boolean is either 1 or 0, True or False. With boolean operators such as and, or and not, you can combine these booleans to perform more advanced queries on your data.
In the sample code on the right, two variables are defined: my_kitchen and your_kitchen, representing areas.
### Instructions
Write Python expressions, wrapped in a print() function, to check whether:
my_kitchen is bigger than 10 and smaller than 18.
my_kitchen is smaller than 14 or bigger than 17.
double the area of my_kitchen is smaller than triple the area of your_kitchen.
## Boolean operators with Numpy


 Before, the operational operators like < and >= worked with Numpy arrays out of the box. Unfortunately, this is not true for the boolean operators and, or, and not.
To use these operators with Numpy, you will need np.logical_and(), np.logical_or() and np.logical_not(). Here's an example on the my_house and your_house arrays from before to give you an idea:
logical_and(your_house > 13, 
            your_house < 15)


### Instructions
Generate boolean arrays that answer the following questions:
Which areas in my_house are greater than 18.5 or smaller than 10?
Which areas are smaller than 11 in both my_houseand your_house? Make sure to wrap both commands in print() statement, so that you can inspect the output.
## if
100xp
It's time to take a closer look around in your house.
Two variables are defined in the sample code: room, a string that tells you which room of the house we're looking at, and area, the area of that room.
### Instructions
Examine the if statement that prints out "Looking around in the kitchen." if room equals "kit".
Write another if statement that prints out "big place!" if areais greater than 15.

## Add else
100xp
On the right, the if construct for room has been extended with an else statement so that "looking around elsewhere." is printed if the condition room = "kit" evaluates to False.
Can you do a similar thing to add more functionality to the if construct for area?
### Instructions
Add an else statement to the second control structure so that "pretty small." is printed out if area > 15 evaluates to False.


## Customize further: elif
100xp
It's also possible to have a look around in the bedroom. The sample code contains an elif part that checks if room equals "bed". In that case, "looking around in the bedroom." is printed out.
It's up to you now! Make a similar addition to the second control structure to further customize the messages for different values of area.
### Instructions
Add an elif to the second control structure such that "medium size, nice!" is printed out if area is greater than 10.

## Driving right (1)
100xp
Remember that cars dataset, containing the cars per 1000 people (cars_per_cap) and whether people drive right (drives_right) for different countries (country)? The code that imports this data in CSV format into Python as a DataFrame is available on the right.
In the video, you saw a step-by-step approach to filter observations from a DataFrame based on boolean arrays. Let's start simple and try to find all observations in cars where drives_right is True.
drives_right is a boolean column, so you'll have to extract it as a Series and then use this boolean Series to select observations from cars.
### Instructions
Extract the drives_right column as a Pandas Series and store it as dr.
Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
Print sel, and assert that drives_right is True for all observations.

## Driving right (2)
100xp
The code in the previous example worked fine, but you actually unnecessarily created a new variable dr. You can achieve the same result without this intermediate variable. Put the code that computes dr straight into the square brackets that select observations from cars.
### Instructions
Convert the code on the right to a one-liner that calculates the variable sel as before.


## Cars per capita (1)
100xp
Let's stick to the cars data some more. This time you want to find out which countries have a high cars per capita figure. In other words, in which countries do many people have a car, or maybe multiple cars.
Similar to the previous example, you'll want to build up a boolean Series, that you can then use to subset the cars DataFrame to select certain observations. If you want to do this in a one-liner, that's perfectly fine!
### Instructions
Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
Use cpc in combination with a comparison operator and 500. You want to end up with a boolean Series that's True if the corresponding country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars.
Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
Print out car_maniac to see if you got it right.

## Cars per capita (2)
100xp
Remember about np.logical_and(), np.logical_or() and np.logical_not(), the Numpy variants of the and, or and notoperators? You can also use them on Pandas Series to do more advanced filtering operations.
Take this example that selects the observations that have a cars_per_capbetween 10 and 80. Try out these lines of code step by step to see what's happening.
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 10, cpc < 80)
medium = cars[between]


### Instructions
Use the code sample above to create a DataFrame medium, that includes all the observations of cars that have a cars_per_cap between 100 and 500.
Print out medium.





