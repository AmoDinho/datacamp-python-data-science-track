# Loops

## Basic while loop
100xp
Below you can find the example from the video where the error variable, initially equal to 50.0, is divided by 4 and printed out on every run:
error = 50.0
while error > 1 :
    error = error / 4
    print(error)


This example will come in handy, because it's time to build a while loop yourself! We're going to code a while loop that implements a very basic control system for a inverted pendulum. If there's an offset from standing perfectly straight, the while loop will incrementally fix this offset.
#### Instructions
- Create the variable offset with an initial value of 8.
- Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
- Print out the sentence "correcting...".
- Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
- Finally, print out offset so you can see how it changes.




## Add conditionals
100xp
The while loop that corrects the offset is a good start, but what if offset is negative? You can try to run the sample code on the right where offset is initialized to -6, but your sessions will be disconnected. The while loop will never stop running, because offset will be further decreased on every run. offset != 0 will never become False and the while loop continues forever.
Fix things by putting an if-else statement inside the while loop.
#### Instructions
- Inside the while loop, replace offset = offset - 1 by an if-else statement:
- If offset > 0, you should decrease offset by 1.
- Else, you should increase offset by 1.
- If you've coded things correctly, hitting Submit Answer should work this time.



## Loop over a list
100xp
Have another look at the for loop that Filip showed in the video:
fam = [1.73, 1.68, 1.71, 1.89]
for height in fam : 
    print(height)


As usual, you simply have to indent the code with 4 spaces to tell Python which code should be executed in the for loop.
The areas variable, containing the area of different rooms in your house, is already defined.
#### Instructions
Write a for loop that iterates over all elements of the areas list and prints out every element separately.


## Indexes and values (1)
100xp
Using a for loop to iterate over a list only gives you access to every list element in each run, one after the other. If you also want to access the index information, so where the list element you're iterating over is located, you can use enumerate().
As an example, have a look at how the for loop from the video was converted:
fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam) :
    print("index " + str(index) + ": " + str(height))


#### Instructions
Adapt the for loop in the sample code to use enumerate(). On each run, a line of the form "room x: y" should be printed, where x is the index of the list element and y is the actual list element, i.e. the area. Make sure to print out this exact string, with the correct spacing.


## Indexes and values (2)
100xp
For non-programmer folks, room 0: 11.25 is strange. Wouldn't it be better if the count started at 1?
#### Instructions
Adapt the print() function in the for loop on the right so that the first printout becomes "room 1: 11.25", the second one "room 2: 18.0" and so on.


## Loop over list of lists
100xp
Remember the house variable from the Intro to Python course? Have a look at its definition on the right. It's basically a list of lists, where each sublist contains the name and area of a room in your house.
It's up to you to build a for loop from scratch this time!
#### Instructions
Write a for loop that goes through each sublist of house and prints out the x is y sqm, where x is the name of the room and y is the area of the room.



## Loop over dictionary
100xp
In Python 3, you need the items() method to loop over a dictionary:
world = { "afghanistan":30.55, 
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :
    print(key + " -- " + str(value))


Remember the europe dictionary that contained the names of some European countries as key and their capitals as corresponding value? Go ahead and write a loop to iterate over it!
#### Instructions
Write a for loop that goes through each key:value pair of europe. On each iteration, "the capital of x is y" should be printed out, where x is the key and y is the value of the pair.


## Loop over Numpy array
100xp
If you're dealing with a 1D Numpy array, looping over all elements can be as simple as:
for x in my_array :
    ...


If you're dealing with a 2D Numpy array, it's more complicated. A 2D array is built up of multiple 1D arrays. To explicitly iterate over all separate elements of a multi-dimensional array, you'll need this syntax:
for x in np.nditer(my_array) :
    ...


Two Numpy arrays that you might recognize from the intro course are available in your Python session: np_height, a Numpy array containing the heights of Major League Baseball players, and np_baseball, a 2D Numpy array that contains both the heights (first column) and weights (second column) of those players.
#### Instructions
Import the numpy package under the local alias np.
Write a for loop that iterates over all elements in np_height and prints out "x inches" for each element, where x is the value in the array.
Write a for loop that visits every element of the np_baseball array and prints it out.



## Loop over DataFrame (1)
100xp
Iterating over a Pandas DataFrame is typically done with the iterrows()method. Used in a for loop, every observation is iterated over and on every iteration the row label and actual row contents are available:
for lab, row in brics.iterrows() :
    ...


In this and the following exercises you will be working on the carsDataFrame. It contains information on the cars per capita and whether people drive right or left for seven countries in the world.
#### Instructions
Write a for loop that iterates over the rows of cars and on each iteration perform two print() calls: one to print out the row label and one to print out all of the rows contents.


## Loop over DataFrame (2)
100xp
The row data that's generated by iterrows() on every run is a Pandas Series. This format is not very convenient to print out. Luckily, you can easily select variables from the Pandas Series using square brackets:
for lab, row in brics.iterrows() :
    print(row['country'])


#### Instructions
Adapt the code in the for loop such that the first iteration prints out "US: 809", the second iteration "AUS: 731", and so on. The output should be in the form "country: cars_per_cap". Make sure to print out this exact string, with the correct spacing.



## Add column (1)
0xp
In the video, Filip showed you how to add the length of the country names of the brics DataFrame in a new column:
for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])


You can do similar things on the cars DataFrame.
### Instructions
Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. You can use the string method upper() for this.
To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.



## Add column (2)
100xp
Using iterrows() to iterate over every observation of a Pandas DataFrame is easy to understand, but not very efficient. On every iteration, you're creating a new Pandas Series.
If you want to add a column to a DataFrame by calling a function on another column, the iterrows() method in combination with a for loop is not the preferred way to go. Instead, you'll want to use apply().
Compare the iterrows() version with the apply() version to get the same result in the brics DataFrame:
for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])

brics["name_length"] = brics["country"].apply(len)


We can do a similar thing to call the upper() method on every name in the country column. However, upper() is a method, so we'll need a slightly different approach:
### Instructions
Replace the for loop with a one-liner that uses .apply(str.upper). The call should give the same result: a column COUNTRY should be added to cars, containing an uppercase version of the country names.
As usual, print out cars to see the fruits of your hard labor
