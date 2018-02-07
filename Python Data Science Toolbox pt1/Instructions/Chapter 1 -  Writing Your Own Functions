# Writing Your Own Functions

## Write a simple function
0xp
In the last video, Hugo described the basics of how to define a function. You will now write your own function!
Define a function, shout(), which simply prints out a string with three exclamation marks '!!!' at the end. The code for the square()function that we wrote earlier is found below. You can use it as a pattern to define shout().
def square():
    new_value = 4 ** 2
    return new_value


Note that the function body is indented 4 spaces already for you. Function bodies need to be indented by a consistent number of spaces and the choice of 4 is common.
### Instructions
- Complete the function header by adding the appropriate function name, shout.
- In the function body, concatenate the string, 'congratulations' with another string, '!!!'. Assign the result to shout_word.
- Print the value of shout_word.
- Call the shout function.

## Functions with multiple parameters
100xp
Hugo discussed the use of multiple parameters in defining functions in the last lecture. You are now going to use what you've learned to modify the shout() function further. Here, you will modify shout() to accept two arguments. Parts of the function shout(), which you wrote earlier, are shown.
### Instructions
- Modify the function header such that it accepts two parameters, word1 and word2, in that order.
- Concatenate each of word1 and word2 with '!!!' and assign to shout1 and shout2, respectively.
- Concatenate shout1 and shout2 together, in that order, and assign to new_shout.
- Pass the strings 'congratulations' and 'you', in that order, to a call to shout(). Assign the return value to yell.

## A brief introduction to tuples
0xp
Alongside learning about functions, you've also learned about tuples! Here, you will practice what you've learned about tuples: how to construct, unpack, and access tuple elements. Recall how Hugo unpacked the tuple even_nums in the video:
a, b, c = even_nums
A three-element tuple named nums has been preloaded for this exercise. Before completing the script, perform the following:
Print out the value of nums in the IPython shell. Note the elements in the tuple.
In the IPython shell, try to change the first element of nums to the value 2 by doing an assignment: nums[0] = 2. What happens?
### Instructions
- Unpack nums to the variables num1, num2, and num3.
- Construct a new tuple, even_nums composed of the same elements in nums, but with the 1st element replaced with the value, 2.
## Function that return multiple values
100xp
In the previous exercise, you constructed tuples, assigned tuples to variables, and unpacked tuples. Here you will return multiple values from a function using tuples. Let's now update our shout() function to return multiple values. Instead of returning just one string, we will return two strings with the string !!! concatenated to each.
Note that the return statement return x, y has the same result as return (x, y): the former actually packs x and y into a tuple under the hood!
### Instructions
- Modify the function header such that the function name is now shout_all, and it accepts two parameters, word1 and word2, in that order.
- Concatenate the string '!!!' to each of word1 and word2 and assign to shout1 and shout2, respectively.
- Construct a tuple shout_words, composed of shout1 and shout2.
- Call shout_all() with the strings 'congratulations' and 'you'and assign the result to yell1 and yell2 (remember, shout_all returns 2 variables!).

## Bringing it all together (1)
100xp
You've got your first taste of writing your own functions in the previous exercises. You've learned how to add parameters to your own function definitions, return a value or multiple values with tuples, and how to call the functions you've defined.
In this and the following exercise, you will bring together all these concepts and apply them to a simple data science problem. You will load a dataset and develop functionalities to extract simple insights from the data.
For this exercise, your goal is to recall how to load a dataset into a DataFrame. The dataset contains Twitter data and you will iterate over entries in a column to build a dictionary in which the keys are the names of languages and the values are the number of tweets in the given language. The file tweets.csv is available in your current directory.
### Instructions
- Import the pandas package with the alias pd.
- Import the file 'tweets.csv' using the pandas function read_csv(). Assign the resulting DataFrame to df.
- Complete the for loop by iterating over col, the 'lang' column in the DataFrame df.
- Complete the bodies of the if-else statements in the for loop: ifthe key is in the dictionary langs_count, add 1 to its current value, else add the key to langs_count and set its value to 1. Use the loop variable entry in your code.

## Bringing it all together (2)
100xp
Great job! You've now defined the functionality for iterating over entries in a column and building a dictionary with keys the names of languages and values the number of tweets in the given language.
In this exercise, you will define a function with the functionality you developed in the previous exercise, return the resulting dictionary from within the function, and call the function with the appropriate arguments.
For your convenience, the pandas package has been imported as pd and the 'tweets.csv' file has been imported into the tweets_df variable.
### Instructions
- Define the function count_entries(), which has two parameters. The first parameter is df for the DataFrame and the second is col_namefor the column name.
- Complete the bodies of the if-else statements in the for loop: ifthe key is in the dictionary langs_count, add 1 to its current value, else add the key to langs_count and set its value to 1. Use the loop variable entry in your code.
- Return the langs_count dictionary from inside the count_entries() function.
- Call the count_entries() function by passing to it tweets_df and the name of the column, 'lang'. Assign the result of the call to the variable result.


