# Dictionaries & Pandas

 
## Motivation for dictionaries
100xp
To see why dictionaries are useful, have a look at the two lists defined on the right. countriescontains the names of some European countries. capitals lists the corresponding names of their capital.
### Instructions
Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
Use ind_ger to access the capital of Germany from the capitals list. Print it out.

## Create dictionary
100xp
The countries and capitals lists are again available in the script. It's your job to convert this data to a dictionary where the country names are the keys and the capitals are the corresponding values. As a refresher, here is a recipe for creating a dictionary:
my_dict = {
   "key1":"value1",
   "key2":"value2",
}


In this recipe, both the keys and the values are strings. This will also be the case for this exercise.

## Access dictionary
100xp
If the keys of a dictionary are chosen wisely, accessing the values in a dictionary is easy and intuitive. For example, to get the capital for France from europeyou can use:
europe['france']


Here, 'france' is the key and 'paris' the value is returned.
### Instructions
Check out which keys are in europe by calling the keys()method on europe. Print out the result.
Print out the value that belongs to the key 'norway'.

## Dictionary Manipulation (1)
0xp
If you know how to access a dictionary, you can also assign a new value to it. To add a new key-value pair to europe you can use something like this:
europe['iceland'] = 'reykjavik'


### Instructions
Add the key 'italy' with the value 'rome' to europe.
To assert that 'italy' is now a key in europe, print out 'italy' in europe.
Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
Print out europe.
## Dictionary Manipulation (2)
100xp
Somebody thought it would be funny to mess with your accurately generated dictionary. An adapted version of the europe dictionary is available in the script on the right.
Can you clean up? Do not do this by adapting the definition of europe, but by adding Python commands to the script to update and remove key:value pairs.
### Instructions
The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
Australia is not in Europe, Austria is! Remove they key 'australia' from europe.
Print out europe to see if your cleaning work paid off.

## Dictionariception
100xp
Remember lists? They could contain anything, even other lists. Well, for dictionaries the same holds. Dictionaries can contain key:value pairs where the values are again dictionaries.
As an example, have a look at the script where another version of europe- the dictionary you've been working with all along - is coded. The keys are still the country names, but the values are dictionaries that contain more information than just the capital.
It's perfectly possible to chain square brackets to select elements. To fetch the population for Spain from europe, for example, you need:
europe['spain']['population']


### Instructions
Use chained square brackets to select and print out the capital of France.
Create a dictionary, named data, with the keys 'capital'and 'population'. Set them to 'rome' and 59.83, respectively.
Add a new key-value pair to europe; the key is 'italy'and the value is data, the dictionary you just built.

## Dictionary to DataFrame (1)
100xp
Pandas is an open source library, providing high-performance, easy-to-use data structures and data analysis tools for Python. Sounds promising!
The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data where you can label the rows and the columns. One way to build a DataFrame is from a dictionary.
In the exercises that follow you will be working with vehicle data from different countries. Each observation corresponds to a country and the columns give information about the number of vehicles per capita, whether people drive left or right, and so on.
Three lists are defined in the script:
names, containing the country names for which data is available.
dr, a list with booleans that tells whether people drive left or right in the corresponding country.
cpc, the number of motor vehicles per 1000 people in the corresponding country.
Each dictionary key is a column label and each value is a list which contains the column elements.
### Instructions
Import pandas as pd.
Use the pre-defined lists to create a dictionary called my_dict. There should be three key value pairs:
key 'country' and value names.
key 'drives_right' and value dr.
key 'cars_per_cap' and value cpc.
Use pd.DataFrame() to turn your dict into a DataFrame called cars.
Print out cars and see how beautiful it is.
## Dictionary to DataFrame (2)
100xp
The Python code that solves the previous exercise is included on the right. Have you noticed that the row labels (i.e. the labels for the different observations) were automatically set to integers from 0 up to 6?
To solve this a list row_labels has been created. You can use it to specify the row labels of the cars DataFrame. You do this by setting the indexattribute of cars, that you can access as cars.index.
### Instructions
Hit Submit Answer to see that, indeed, the row labels are not correctly set.
Specify the row labels by setting cars.index equal to row_labels.
Print out cars again and check if the row labels are correct this time.

## CSV to DataFrame (1)
100xp
Putting data in a dictionary and then building a DataFrame works, but it's not very efficient. What if you're dealing with millions of observations? In those cases, the data is typically available as files with a regular structure. One of those file types is the CSV file, which is short for "comma-separated values".
To import CSV data into Python as a Pandas DataFrame you can use read_csv().
Let's explore this function with the same cars data from the previous exercises. This time, however, the data is available in a CSV file, named cars.csv. It is available in your current working directory, so the path to the file is simply 'cars.csv'.
Instructions
To import CSV files you still need the pandas package: import it as pd.
Use pd.read_csv() to import cars.csv data as a DataFrame. Store this dataframe as cars.
Print out cars. Does everything look OK?

## CSV to DataFrame (2)
100xp
Your read_csv() call to import the CSV data didn't generate an error, but the output is not entirely what we wanted. The row labels were imported as another column without a name.
Remember index_col, an argument of read_csv(), that you can use to specify which column in the CSV file should be used as a row label? Well, that's exactly what you need here!
Python code that solves the previous exercise is already included; can you make the appropriate changes to fix the data import?
### Instructions
Run the code with Submit Answer and assert that the first column should actually be used as row labels.
Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
Has the printout of cars improved now?
## Square Brackets (1)
100xp
In the video, you saw that you can index and select Pandas DataFrames in many different ways. The simplest, but not the most powerful way, is to use square brackets.
In the sample code on the right, the same cars data is imported from a CSV files as a Pandas DataFrame. To select only the cars_per_cap column from cars, you can use:
cars['cars_per_cap']
cars[['cars_per_cap']]


The single bracket version gives a Pandas Series, the double bracket version gives a Pandas DataFrame.
### Instructions
Use single square brackets to print out the country column of cars as a Pandas Series.
Use double square brackets to print out the country column of cars as a Pandas DataFrame.
Use double square brackets to print out a DataFrame with both the country and drives_right columns of cars, in this order.

## Square Brackets (2)
100xp
Square brackets can do more than just selecting columns. You can also use them to get rows, or observations, from a DataFrame. The following call selects the first five rows from the cars DataFrame:
cars[0:5]


The result is another DataFrame containing only the rows you specified.
Pay attention: You can only select rows using square brackets if you specify a slice, like 0:4. Also, you're using the integer indexes of the rows here, not the row labels!
### Instructions
Select the first 3 observations from cars and print them out.
Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.

## loc and iloc (1)
100xp
With loc and iloc you can do practically any data selection operation on DataFrames you can think of. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.
Try out the following commands in the IPython Shell to experiment with loc and iloc to select observations. Each pair of commands here gives the same result.
cars.loc['RU']
cars.iloc[4]

cars.loc[['RU']]
cars.iloc[[4]]

cars.loc[['RU', 'AUS']]
cars.iloc[[4, 1]]


As before, code is included that imports the cars data as a Pandas DataFrame.
### Instructions
Use loc or iloc to select the observation corresponding to Japan as a Series. The label of this row is JAP, the index is 2. Make sure to print the resulting Series.
Use loc or iloc to select the observations for Australia and Egypt as a DataFrame. You can find out about the labels/indexes of these rows by inspecting cars in the IPython Shell. Make sure to print the resulting DataFrame.

## loc and iloc (2)
100xp
loc and iloc also allow you to select both rows and columns from a DataFrame. To experiment, try out the following commands in the IPython Shell. Again, paired commands produce the same result.
cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]

cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]

cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]


### Instructions
Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.

## loc and iloc (3)
100xp
It's also possible to select only columns with loc and iloc. In both cases, you simply put a slice going from beginning to end in front of the comma:
cars.loc[:, 'country']
cars.iloc[:, 1]

cars.loc[:, ['country','drives_right']]
cars.iloc[:, [1, 2]]


### Instructions
Print out the drives_right column as a Series using locor iloc.
Print out the drives_right column as a DataFrame using loc or iloc.
Print out both the cars_per_cap and drives_rightcolumn as a DataFrame using loc or iloc.




