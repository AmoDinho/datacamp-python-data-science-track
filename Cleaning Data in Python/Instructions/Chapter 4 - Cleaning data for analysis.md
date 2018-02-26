# Chapter 4 - Cleaning data for analysis


## Converting data types
100xp
In this exercise, you'll see how ensuring all categorical variables in a DataFrame are of type category reduces memory usage.
The tips dataset has been loaded into a DataFrame called tips. This data contains information about how much a customer tipped, whether the customer was male or female, a smoker or not, etc.
Look at the output of tips.info() in the IPython Shell. You'll note that two columns that should be categorical - sex and smoker - are instead of type object, which is pandas' way of storing arbitrary strings. Your job is to convert these two columns to type category and note the reduced memory usage.
### Instructions
Convert the sex column of the tips DataFrame to type 'category' using the .astype() method.
Convert the smoker column of the tips DataFrame.
Print the memory usage of tips after converting the data types of the columns. Use the .info() method to do this.

## Working with numeric data
100xp
If you expect the data type of a column to be numeric (int or float), but instead it is of type object, this typically means that there is a non numeric value in the column, which also signifies bad data.
You can use the pd.to_numeric() function to convert a column into a numeric data type. If the function raises an error, you can be sure that there is a bad value within the column. You can either use the techniques you learned in Chapter 1 to do some exploratory data analysis and find the bad value, or you can choose to ignore or coerce the value into a missing value, NaN.
A modified version of the tips dataset has been pre-loaded into a DataFrame called tips. For instructional purposes, it has been pre-processed to introduce some 'bad' data for you to clean. Use the .info() method to explore this. You'll note that the total_bill and tip columns, which should be numeric, are instead of type object. Your job is to fix this.
### Instructions
Use pd.to_numeric() to convert the 'total_bill'column of tips to a numeric data type. Coerce the errors to NaN by specifying the keyword argument errors='coerce'.
Convert the 'tip' column of 'tips' to a numeric data type exactly as you did for the 'total_bill' column.
Print the info of tips to confirm that the data types of 'total_bill' and 'tips' are numeric.

## String parsing with regular expressions
100xp
In the video, Dan introduced you to the basics of regular expressions, which are powerful ways of defining patterns to match strings. This exercise will get you started with writing them.
When working with data, it is sometimes necessary to write a regular expression to look for properly entered values. Phone numbers in a dataset is a common field that needs to be checked for validity. Your job in this exercise is to define a regular expression to match US phone numbers that fit the pattern of xxx-xxx-xxxx.
The regular expression module in python is re. When performing pattern matching on data, since the pattern will be used for a match across multiple rows, it's better to compile the pattern first using re.compile(), and then use the compiled pattern to match values.
### Instructions
Import re.
Compile a pattern that matches a phone number of the format xxx-xxx-xxxx.
Use \d{x} to match x digits. Here you'll need to use it three times: twice to match 3 digits, and once to match 4 digits.
Place the regular expression inside re.compile().
Using the .match() method on prog, check whether the pattern matches the string '123-456-7890'.
Check whether the pattern matches the string '1123-456-7890'.

## Extracting numerical values from strings
100xp
Extracting numbers from strings is a common task, particularly when working with unstructured data or log files.
Say you have the following string: 'the recipe calls for 6 strawberries and 2 bananas'.
It would be useful to extract the 6 and the 2 from this string to be saved for later use when comparing strawberry to banana ratios.
When using a regular expression to extract multiple numbers (or multiple pattern matches, to be exact), you can use the re.findall() function. Dan did not discuss this in the video, but it is straightforward to use: You pass in a pattern and a string to re.findall(), and it will return a list of the matches.
### Instructions
Import re.
Write a pattern that will find all the numbers in the following string: 'the recipe calls for 10 strawberries and 1 banana'. To do this:
Use the re.findall() function and pass it two arguments: the pattern, followed by the string.
\d is the pattern required to find digits. This should be followed with a + so that the previous element is matched one or more times. This ensures that 10 is viewed as one number and not as 1 and 0.
Print the matches to confirm that your regular expression found the values 10 and 1.

## Pattern matching
100xp
In this exercise, you'll continue practicing your regular expression skills. For each provided string, your job is to write the appropriate pattern to match it.
### Instructions
Write patterns to match:
A telephone number of the format xxx-xxx-xxxx. You already did this in a previous exercise.
A string of the format: A dollar sign, an arbitrary number of digits, a decimal point, 2 digits.
Use \$ to match the dollar sign, \d* to match an arbitrary number of digits, \. to match the decimal point, and \d{x} to match x number of digits.
A capital letter, followed by an arbitrary number of alphanumeric characters.
Use [A-Z] to match any capital letter followed by \w* to match an arbitrary number of alphanumeric characters.

## Custom functions to clean data
100xp
You'll now practice writing functions to clean data.
The tips dataset has been pre-loaded into a DataFrame called tips. It has a 'sex' column that contains the values 'Male' or 'Female'. Your job is to write a function that will recode 'Male' to 1, 'Female' to 0, and return np.nan for all entries of 'sex' that are neither 'Male' nor 'Female'.
Recoding variables like this is a common data cleaning task. Functions provide a mechanism for you to abstract away complex bits of code as well as reuse code. This makes your code more readable and less error prone.
As Dan showed you in the videos, you can use the .apply() method to apply a function across entire rows or columns of DataFrames. However, note that each column of a DataFrame is a pandas Series. Functions can also be applied across Series. Here, you will apply your function over the 'sex'column.
### Instructions
Define a function named recode_sex() that has one parameter: sex_value.
If sex_value equals 'Male', return 1.
Else, if sex_value equals 'Female', return 0.
If sex_value does not equal 'Male' or 'Female', return np.nan. NumPy has been pre-imported for you.
Apply your recode_sex() function over tips.sex using the .apply() method to create a new column: 'sex_recode'. Note that when passing in a function inside the .apply() method, you don't need to specify the parentheses after the function name.
Hit 'Submit Answer' and take note of the new 'sex_recode'column in the tips DataFrame!

## Lambda functions
100xp
You'll now be introduced to a powerful Python feature that will help you clean your data more effectively: lambda functions. Instead of using the def syntax that you used in the previous exercise, lambda functions let you make simple, one-line functions.
For example, here's a function that squares a variable used in an .apply()method:
def my_square(x):
    return x ** 2

df.apply(my_square)


The equivalent code using a lambda function is:
df.apply(lambda x: x ** 2)


The lambda function takes one parameter - the variable x. The function itself just squares x and returns the result, which is whatever the one line of code evaluates to. In this way, lambda functions can make your code concise and Pythonic.
The tips dataset has been pre-loaded into a DataFrame called tips. Your job is to clean its 'total_dollar' column by removing the dollar sign. You'll do this using two different methods: With the .replace() method, and with regular expressions. The regular expression module re has been pre-imported.
### Instructions
Use the .replace() method inside a lambda function to remove the dollar sign from the 'total_dollar' column of tips.
You need to specify two arguments to the .replace()method: The string to be replaced ('$'), and the string to replace it by ('').
Apply the lambda function over the 'total_dollar'column of tips.
Use a regular expression to remove the dollar sign from the 'total_dollar' column of tips.
The pattern has been provided for you: It is the first argument of the re.findall() function.
Complete the rest of the lambda function and apply it over the 'total_dollar' column of tips. Notice that because re.findall() returns a list, you have to slice it in order to access the actual value.
Hit 'Submit Answer' to verify that you have removed the dollar sign from the column.

## Dropping duplicate data
100xp
Duplicate data causes a variety of problems. From the point of view of performance, they use up unnecessary amounts of memory and cause unneeded calculations to be performed when processing data. In addition, they can also bias any analysis results.
A dataset consisting of the performance of songs on the Billboard charts has been pre-loaded into a DataFrame called billboard. Check out its columns in the IPython Shell. Your job in this exercise is to subset this DataFrame and then drop all duplicate rows.
### Instructions
Create a new DataFrame called tracks that contains the following columns from billboard: 'year', 'artist', 'track', and 'time'.
Print the info of tracks. This has been done for you.
Drop duplicate rows from tracks using the .drop_duplicates() method. Save the result to tracks_no_duplicates.
Print the info of tracks_no_duplicates. This has been done for you, so hit 'Submit Answer' to see the results!

## Filling missing data
100xp
Here, you'll return to the airquality dataset from Chapter 2. It has been pre-loaded into the DataFrame airquality, and it has missing values for you to practice filling in. Explore airquality in the IPython Shell to checkout which columns have missing values.
It's rare to have a (real-world) dataset without any missing values, and it's important to deal with them because certain calculations cannot handle missing values while some calculations will, by default, skip over any missing values.
Also, understanding how much missing data you have, and thinking about where it comes from is crucial to making unbiased interpretations of data.
### Instructions
Calculate the mean of the Ozone column of airqualityusing the .mean() method on airquality.Ozone.
Use the .fillna() method to replace all the missing values in the Ozone column of airquality with the mean, oz_mean.
Hit 'Submit Answer' to see the result of filling in the missing values!

## Testing your data with asserts
0xp
Here, you'll practice writing assert statements using the Ebola dataset from previous chapters to programmatically check for missing values and to confirm that all values are positive. The dataset has been pre-loaded into a DataFrame called ebola.
In the video, you saw Dan use the .all() method together with the .notnull() DataFrame method to check for missing values in a column. The .all() method returns True if all values are True. When used on a DataFrame, it returns a Series of Booleans - one for each column in the DataFrame. So if you are using it on a DataFrame, like in this exercise, you need to chain another .all() method so that you return only one True or False value. When using these within an assert statement, nothing will be returned if the assert statement is true: This is how you can confirm that the data you are checking are valid.
Note: You can use pd.notnull(df) as an alternative to df.notnull().
### Instructions
Write an assert statement to confirm that there are no missing values in ebola.
Use the pd.notnull() function on ebola (or the .notnull() method of ebola) and chain two .all() methods (that is, .all().all()). The first .all() method will return a True or False for each column, while the second .all() method will return a single True or False.
Write an assert statement to confirm that all values in ebolaare greater than or equal to 0.
Chain two all() methods to the Boolean condition (ebola >= 0).

