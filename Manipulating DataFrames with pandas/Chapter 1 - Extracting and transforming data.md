# Chapter 1 - Extracting and transforming data




## Positional and labeled indexing
100xp
Given a pair of label-based indices, sometimes it's necessary to find the corresponding positions. In this exercise, you will use the Pennsylvania election results again. The DataFrame is provided for you as election.
Find x and y such that election.iloc[x, y] == election.loc['Bedford', 'winner']. That is, what is the row position of 'Bedford', and the column position of 'winner'? Remember that the first position in Python is 0, not 1!
To answer this question, first explore the DataFrame using election.head() in the IPython Shell and inspect it with your eyes.
### Instructions
Explore the DataFrame in the IPython Shell using election.head().
Assign the row position of election.loc['Bedford'] to x.
Assign the column position of election['winner'] to y.
Hit 'Submit Answer' to print the boolean equivalence of the .loc and .iloc selections.
## Indexing and column rearrangement
100xp
There are circumstances in which it's useful to modify the order of your DataFrame columns. We do that now by extracting just two columns from the Pennsylvania election results DataFrame.
Your job is to read the CSV file and set the index to 'county'. You'll then assign a new DataFrame by selecting the list of columns ['winner', 'total', 'voters']. The CSV file is provided to you in the variable filename.
### Instructions
Import pandas as pd.
Read in filename using pd.read_csv() and set the index to 'county' by specifying the index_col parameter.
Create a separate DataFrame results with the columns ['winner', 'total', 'voters'].
Print the output using results.head(). This has been done for you, so hit 'Submit Answer' to see the new DataFrame!


## Slicing rows
100xp
The Pennsylvania US election results data set that you have been using so far is ordered by county name. This means that county names can be sliced alphabetically. In this exercise, you're going to perform slicing on the county names of the electionDataFrame from the previous exercises, which has been pre-loaded for you.
### Instructions
Slice the row labels 'Perry' to 'Potter' and assign the output to p_counties.
Print the p_counties DataFrame. This has been done for you.
Slice the row labels 'Potter' to 'Perry' in reverse order. To do this for hypothetical row labels 'a' and 'b', you could use a stepsize of -1like so: df.loc['b':'a':-1].
Print the p_counties_rev DataFrame. This has also been done for you, so hit 'Submit Answer' to see the result of your slicing!


## Slicing columns
100xp
Similar to row slicing, columns can be sliced by value. In this exercise, your job is to slice column names from the Pennsylvania election results DataFrame using .loc[].
It has been pre-loaded for you as election, with the index set to 'county'.
### Instructions
Slice the columns from the starting column to 'Obama' and assign the result to left_columns
Slice the columns from 'Obama' to 'winner' and assign the result to middle_columns
Slice the columns from 'Romney' to the end and assign the result to right_columns
The code to print the first 5 rows of left_columns, middle_columns, and right_columns has been written, so hit 'Submit Answer' to see the results!


## Subselecting DataFrames with lists
100xp
You can use lists to select specific row and column labels with the .loc[] accessor. In this exercise, your job is to select the counties ['Philadelphia', 'Centre', 'Fulton'] and the columns ['winner','Obama','Romney'] from the election DataFrame, which has been pre-loaded for you with the index set to 'county'.
### Instructions
Create the list of row labels ['Philadelphia', 'Centre', 'Fulton'] and assign it to rows.
Create the list of column labels ['winner', 'Obama', 'Romney']and assign it to cols.
Create a new DataFrame by selecting with rows and cols in .loc[] and assign it to three_counties.
Print the three_counties DataFrame. This has been done for you, so hit 'Submit Answer` to see your new DataFrame.


## Thresholding data
0xp
In this exercise, we have provided the Pennsylvania election results and included a column called 'turnout' that contains the percentage of voter turnout per county. Your job is to prepare a boolean array to select all of the rows and columns where voter turnout exceeded 70%.
As before, the DataFrame is available to you as election with the index set to 'county'.
### Instructions
Create a boolean array of the condition where the 'turnout' column is greater than 70 and assign it to high_turnout.
Filter the election DataFrame with the high_turnout array and assign it to high_turnout_df.
Print the filtered DataFrame. This has been done for you, so hit 'Submit Answer' to see it!

## Filtering columns using other columns
100xp
The election results DataFrame has a column labeled 'margin' which expresses the number of extra votes the winner received over the losing candidate. This number is given as a percentage of the total votes cast. It is reasonable to assume that in counties where this margin was less than 1%, the results would be too-close-to-call.
Your job is to use boolean selection to filter the rows where the margin was less than 1. You'll then convert these rows of the 'winner' column to np.nan to indicate that these results are too close to declare a winner.
The DataFrame has been pre-loaded for you as election.
### Instructions
Import numpy as np.
Create a boolean array for the condition where the 'margin' column is less than 1 and assign it to too_close.
Convert the entries in the 'winner' column where the result was too close to call to np.nan.
Print the output of election.info(). This has been done for you, so hit 'Submit Answer' to see the results.

## Filtering using NaNs
100xp
In certain scenarios, it may be necessary to remove rows and columns with missing data from a DataFrame. The .dropna() method is used to perform this action. You'll now practice using this method on a dataset obtained from Vanderbilt University, which consists of data from passengers on the Titanic.
The DataFrame has been pre-loaded for you as titanic. Explore it in the IPython Shell and you will note that there are many NaNs. You will focus specifically on the 'age' and 'cabin' columns in this exercise. Your job is to use .dropna() to remove rows where any of these two columns contains missing data and rows where all of these two columns contain missing data.
You'll also use the .shape attribute, which returns the number of rows and columns in a tuple from a DataFrame, or the number of rows from a Series, to see the effect of dropping missing values from a DataFrame.
Finally, you'll use the thresh= keyword argument to drop columns from the full dataset that have more than 1000 missing values.
### Instructions
Select the 'age' and 'cabin' columns of titanic and create a new DataFrame df.
Print the shape of df. This has been done for you.
Drop rows in df with how='any' and print the shape.
Drop rows in df with how='all' and print the shape.
Drop columns from the titanic DataFrame that have more than 1000 missing values by specifying the thresh and axis keyword arguments. Print the output of .info() from this.


## Using apply() to transform a column
0xp
The .apply() method can be used on a pandas DataFrame to apply an arbitrary Python function to every element. In this exercise you'll take daily weather data in Pittsburgh in 2013 obtained from Weather Underground.
A function to convert degrees Fahrenheit to degrees Celsius has been written for you. Your job is to use the .apply() method to perform this conversion on the 'Mean TemperatureF' and 'Mean Dew PointF' columns of the weatherDataFrame.
### Instructions
Apply the to_celsius function over the ['Mean TemperatureF','Mean Dew PointF'] columns of the weatherDataFrame.
Reassign the columns of df_celsius to ['Mean TemperatureC','Mean Dew PointC'].
Hit 'Submit Answer' to see the new DataFrame with the converted units.

## Using .map() with a dictionary
100xp
The .map() method is used to transform values according to a Python dictionary look-up. In this exercise you'll practice this method while returning to working with the election DataFrame, which has been pre-loaded for you.
Your job is to use a dictionary to map the values 'Obama' and 'Romney' in the 'winner' column to the values 'blue' and 'red', and assign the output to the new column 'color'.
### Instructions
Create a dictionary with the key:value pairs 'Obama':'blue' and 'Romney':'red'.
Use the .map() method on the 'winner' column using the red_vs_blue dictionary you created.
Print the output of election.head(). This has been done for you, so hit 'Submit Answer' to see the new column!

## Using vectorized functions
100xp
When performance is paramount, you should avoid using .apply() and .map()because those constructs perform Python for-loops over the data stored in a pandas Series or DataFrame. By using vectorized functions instead, you can loop over the data at the same speed as compiled code (C, Fortran, etc.)! NumPy, SciPy and pandas come with a variety of vectorized functions (called Universal Functions or UFuncs in NumPy).
You can even write your own vectorized functions, but for now we will focus on the ones distributed by NumPy and pandas.
In this exercise you're going to import the zscore method from scipy.statsand use it to compute the deviation in voter turnout in Pennsylvania from the mean in fractions of the standard deviation. In statistics, the z-score is the number of standard deviations by which an observation is above the mean - so if it is negative, it means the observation is below the mean.
Instead of using .apply() as you did in the earlier exercises, the zscore UFunc will take a pandas Series as input and return a NumPy array. You will then assign the values of the NumPy array to a new column in the DataFrame. You will be working with the election DataFrame - it has been pre-loaded for you.
### Instructions
Import zscore from scipy.stats.
Call zscore with election['turnout'] as input .
Print the output of type(turnout_zscore). This has been done for you.
Assign turnout_zscore to a new column in election as 'turnout_zscore'.
Print the output of election.head(). This has been done for you, so hit 'Submit Answer' to view the result.

