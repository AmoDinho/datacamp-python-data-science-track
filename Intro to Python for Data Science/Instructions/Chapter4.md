
# Chapter 4

 ## Your First Numpy Array
100xp
We're going to dive into the world of baseball. Along the way, you'll get comfortable with the basics of Numpy, a powerful package to do data science.
A list baseball has already been defined in the Python script, representing the height of some baseball players in centimeters. Can you add some code here and there to create a Numpy array from it?
### Instructions
- Import the numpy package as np, so that you can refer to numpy with np.
- Use np.array() to create a Numpy array from baseball. Name this array np_baseball.
- Print out the type of np_baseball to check that you got it right.

## Baseball players' height
100xp
You are a huge baseball fan. You decide to call the MLB (Major League Baseball) and ask around for some more statistics on the height of the main players. They pass along data on more than a thousand players, which is stored as a regular Python list: height. The height is expressed in inches. Can you make a Numpy array out of it and convert the units to centimeters?
height is already available and the numpy package is loaded, so you can start straight away (Source: stat.ucla.edu).
### Instructions
- Create a Numpy array from height. Name this new array np_height.
- Print np_height.
- Multiply np_height with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
- Print out np_height_m and check if the output makes sense.

## Baseball player's BMI
100xp
The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: height and weight. height is in inches and weight is in pounds.
It's now possible to calculate the BMI of each baseball player. Python code to convert height to a Numpy array with the correct units is already available in the workspace. Follow the instructions step by step and finish the game!
### Instructions
- Create a Numpy array from the weight list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting Numpy array as np_weight_kg.
- Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
BMI=weight(kg)height(m)2BMI=weight(kg)height(m)2
- Save the resulting numpy array as bmi.
- Print out bmi.

## Lightweight baseball players
100xp
To subset both regular Python lists and Numpy arrays, you can use square brackets:
x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]


For Numpy specifically, you can also use boolean Numpy arrays:
high = y > 5
y[high]


The code that calculates the BMI of all baseball players is already included. Follow the instructions and reveal interesting things from the data!
### Instructions
- Create a boolean Numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. You can use the < operator for this. Name the array light.
- Print the array light.
- Print out a Numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.

## Subsetting Numpy Arrays
100xp
You've seen it with your own eyes: Python lists and Numpy arrays sometimes behave differently. Luckily, there are still certainties in this world. For example, subsetting (using the square bracket notation on lists or arrays) works exactly the same. To see this for yourself, try the following lines of code in the IPython Shell:
x = ["a", "b", "c"]
x[1]

np_x = np.array(x)
np_x[1]


The script on the right already contains code that imports numpy as np, and stores both the height and weight of the MLB players as Numpy arrays.
### Instructions
- Subset np_weight: print out the element at index 50.
- Print out a sub-array of np_height: It contains the elements at index 100 up to and including index 110


## Your First 2D Numpy Array
100xp
Before working on the actual MLB data, let's try to create a 2D Numpy array from a small list of lists.
In this exercise, baseball is a list of lists. The main list contains 4 elements. Each of these elements is a list containing the height and the weight of 4 baseball players, in this order. baseball is already coded for you in the script.
### Instructions
- Use np.array() to create a 2D Numpy array from baseball. Name it np_baseball.
- Print out the type of np_baseball.
- Print out the shape attribute of np_baseball. Use np_baseball.shape.

## Baseball data in 2D form
100xp
You have another look at the MLB data and realize that it makes more sense to restructure all this information in a 2D Numpy array. This array should have 1015 rows, corresponding to the 1015 baseball players you have information on, and 2 columns (for height and weight).
The MLB was, again, very helpful and passed you the data in a different structure, a Python list of lists. In this list of lists, each sublist represents the height and weight of a single baseball player. The name of this embedded list is baseball.
Can you store the data as a 2D array to unlock Numpy's extra functionality?
### Instructions
- Use np.array() to create a 2D Numpy array from baseball. Name it np_baseball.
- Print out the shape attribute of np_baseball.

## Subsetting 2D Numpy Arrays
100xp
If your 2D Numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.
# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

# numpy
import numpy as np
np_x = np.array(x)
np_x[:,0]


For regular Python lists, this is a real pain. For 2D Numpy arrays, however, it's pretty intuitive! The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.
The code that converts the pre-loaded baseball list to a 2D Numpy array is already in the script. Add some lines to make the correct selections. Remember that in Python, the first element is at index 0!
### Instructions
- Print out the 50th row of np_baseball.
- Make a new variable, np_weight, containing the entire second column of np_baseball.
-Select the height (first column) of the 124th baseball player in np_baseball and print it out.


## 2D Arithmetic
100xp
Remember how you calculated the Body Mass Index for all baseball players? Numpy was able to perform all calculations element-wise. For 2D Numpy arrays this isn't any different! You can combine matrices with single numbers, with vectors, and with other matrices.
Execute the code below in the IPython shell and see if you understand:
import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat


np_baseball is coded for you; it's again a 2D Numpy array with 3 columns representing height, weight and age.
### Instructions
- You managed to get hold on the changes in weight, height and age of all baseball players. It is available as a 2D Numpy array, update. Add np_baseball and update and print out the result.
- You want to convert the units of height and weight. As a first step, create a Numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
- Multiply np_baseball with conversion and print out the result.

## Average versus median
100xp
You now know how to use Numpy functions to a get a better feeling for your data. It basically comes down to importing Numpy and then calling several simple functions on the Numpy arrays:
import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)


The baseball data is available as a 2D Numpy array with 3 columns (height, weight, age) and 1015 rows. The name of this Numpy array is np_baseball. After restructuring the data, however, you notice that some height values are abnormally high. Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called outliers.
### Instructions
- Create Numpy array np_height, that is equal to first column of np_baseball.
- Print out the mean of np_height.
- Print out the median of np_height.

## Explore the baseball data
0xp
Because the mean and median are so far apart, you decide to complain to the MLB. They find the error and send the corrected data over to you. It's again available as a 2D Numpy array np_baseball, with three columns.
The Python script on the right already includes code to print out informative messages with the different summary statistics. Can you finish the job?
### Instructions
- The code to print out the mean height is already included. Complete the code for the median height. Replace None with the correct code.
- Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the correct code.
- Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr. Replace None with the correct code.

## Blend it all together
100xp
In the last few exercises you've learned everything there is to know about heights and weights of baseball players. Now it's time to dive into another sport: soccer.
You've contacted the FIFA for some data and they handed you two lists. The lists are the following: positions = ['GK', 'M', 'A', 'D', ...] heights = [191, 184, 185, 180, ...] Each element in the lists corresponds to a player. The first list, positions, contains strings representing each player's position. The possible positions are: 'GK' (goalkeeper), 'M' (midfield), 'A' (attack) and 'D'(defense). The second list, heights, contains integers representing the height of the player in cm. The first player in the lists is a goalkeeper and is pretty tall (191 cm).
You're fairly confident that the median height of goalkeepers is higher than that of other players on the soccer field. Some of your friends don't believe you, so you are determined to show them using the data you received from FIFA and your newly acquired Python skills.
### Instructions
- Convert heights and positions, which are regular lists, to numpy arrays. Call them np_heights and np_positions.
- Extract all the heights of the goalkeepers. You can use a little trick here: use np_positions == 'GK' as an index for np_heights. Assign the result to gk_heights.
- Extract all the heights of the all the other players. This time use np_positions != 'GK' as an index for np_heights. Assign the result to other_heights.
- Print out the median height of the goalkeepers using np.median(). Replace None with the correct code.
- Do the same for the other players. Print out their median height. Replace None with the correct code.
