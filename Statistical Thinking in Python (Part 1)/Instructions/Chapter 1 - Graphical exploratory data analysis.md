# Chapter 1 - Graphical exploratory data analysis


## Axis labels!
In the last exercise, you made a nice histogram of petal lengths of Iris versicolor, but you didn't label the axes! That's ok; it's not your fault since we didn't ask you to. Now, add axis labels to the plot using plt.xlabel() and plt.ylabel(). Don't forget to add units and assign both statements to _. The packages matplotlib.pyplot and seaborn are already imported with their standard aliases. This will be the case in what follows, unless specified otherwise.

### INSTRUCTIONS
100XP
Label the axes. Don't forget that you should always include units in your axis labels. Your yy-axis label is just 'count'. Your xx-axis label is 'petal length (cm)'. The units are essential!
Display the plot constructed in the above steps using plt.show().

## Adjusting the number of bins in a histogram
The histogram you just made had ten bins. This is the default of matplotlib. The "square root rule" is a commonly-used rule of thumb for choosing number of bins: choose the number of bins to be the square root of the number of samples. Plot the histogram of Iris versicolor petal lengths again, this time using the square root rule for the number of bins. You specify the number of bins using the bins keyword argument of plt.hist().
The plotting utilities are already imported and the seaborn defaults already set. The variable you defined in the last exercise, versicolor_petal_length, is already in your namespace.

### INSTRUCTIONS
100XP
Import numpy as np. This gives access to the square root function, np.sqrt().
Determine how many data points you have using len().
Compute the number of bins using the square root rule.
Convert the number of bins to an integer using the built in int() function.
Generate the histogram and make sure to use the binskeyword argument.
Hit 'Submit Answer' to plot the figure and see the fruit of your labors!


## Plotting the ECDF
You will now use your ecdf() function to compute the ECDF for the petal lengths of Anderson's Iris versicolor flowers. You will then plot the ECDF. Recall that your ecdf() function returns two arrays so you will need to unpack them. An example of such unpacking is x, y = foo(data), for some function foo().
### INSTRUCTIONS
100XP
Use ecdf() to compute the ECDF of versicolor_petal_length. Unpack the output into x_versand y_vers.
Plot the ECDF as dots. Remember to include marker = '.'and linestyle = 'none' in addition to x_vers and y_versas arguments inside plt.plot().
Set the margins of the plot with plt.margins() so that no data points are cut off. Use a 2% margin.
Label the axes. You can label the y-axis 'ECDF'.
Show your plot.

## Computing the ECDF
In this exercise, you will write a function that takes as input a 1D array of data and then returns the x and y values of the ECDF. You will use this function over and over again throughout this course and its sequel. ECDFs are among the most important plots in statistical analysis. You can write your own function, foo(x,y) according to the following skeleton:
def foo(a,b):
    """State what function does here"""
    # Computation performed here
    return x, y


The function foo() above takes two arguments a and band returns two values x and y. The function header def foo(a,b): contains the function signature foo(a,b), which consists of the function name, along with its parameters. For more on writing your own functions, see DataCamp's course Python Data Science Toolbox (Part 1) here!

### INSTRUCTIONS
100XP
Define a function with the signature ecdf(data). Within the function definition,
Compute the number of data points, n, using the len()function.
The xx-values are the sorted data. Use the np.sort()function to perform the sorting.
The yy data of the ECDF go from 1/n to 1 in equally spaced increments. You can construct this using np.arange(). Remember, however, that the end value in np.arange() is not inclusive. Therefore, np.arange() will need to go from 1 to n+1. Be sure to divide this by n.
The function returns the values x and y.

## Comparison of ECDFs
ECDFs also allow you to compare two or more distributions (though plots get cluttered if you have too many). Here, you will plot ECDFs for the petal lengths of all three iris species. You already wrote a function to generate ECDFs so you can put it to good use!
To overlay all three ECDFs on the same plot, you can use plt.plot() three times, once for each ECDF. Remember to include marker='.' and linestyle='none' as arguments inside plt.plot().
### INSTRUCTIONS
100XP
Compute ECDFs for each of the three species using your ecdf() function. The variables setosa_petal_length, versicolor_petal_length, and virginica_petal_lengthare all in your namespace. Unpack the ECDFs into x_set, y_set, x_vers, y_vers and x_virg, y_virg, respectively.
Plot all three ECDFs on the same plot as dots. To do this, you will need three plt.plot() commands. Assign the result of each to _.
Specify 2% margins.
A legend and axis labels have been added for you, so hit 'Submit Answer' to see all the ECDFs!

