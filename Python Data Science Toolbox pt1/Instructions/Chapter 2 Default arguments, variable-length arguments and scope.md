
# Chapter 2 Default arguments, variable-length arguments and scope

## The keyword global
100xp
Let's work more on your mastery of scope. In this exercise, you will use the keyword global within a function to alter the value of a variable defined in the global scope.

## Nested Functions I
0xp
You've learned in the last video about nesting functions within functions. One reason why you'd like to do this is to avoid writing out the same computations within functions repeatedly. There's nothing new about defining nested functions: you simply define it as you would a regular function with def and embed it inside another function!
In this exercise, inside a function three_shouts(), you will define a nested function inner() that concatenates a string object with !!!. three_shouts() then returns a tuple of three elements, each a string concatenated with !!! using inner(). Go for it!
### Instructions
Complete the function header of the nested function with the function name inner() and a single parameter word.
Complete the return value: each element of the tuple should be a call to inner(), passing in the parameters from three_shouts() as arguments to each call.

## Nested Functions II
100xp
Great job, you've just nested a function within another function. One other pretty cool reason for nesting functions is the idea of a closure. This means that the nested or inner function remembers the state of its enclosing scope when called. Thus, anything defined locally in the enclosing scope is available to the inner function even when the outer function has finished execution.
Let's move forward then! In this exercise, you will complete the definition of the inner function inner_echo() and then call echo() a couple of times, each with a different argument. Complete the exercise and see what the output will be!
### Instructions
Complete the function header of the inner function with the function name inner_echo() and a single parameter word1.
Complete the function echo() so that it returns inner_echo.
We have called echo(), passing 2 as an argument, and assigned the resulting function to twice. Your job is to call echo(), passing 3 as an argument. Assign the resulting function to thrice.
Hit Submit to call twice() and thrice() and print the results.


## The keyword nonlocal and nested functions
100xp
Let's once again work further on your mastery of scope! In this exercise, you will use the keyword nonlocal within a nested function to alter the value of a variable defined in the enclosing scope.
### Instructions
Assign to echo_word the string word, concatenated with itself.
Use the keyword nonlocal to alter the value of echo_wordin the enclosing scope.
Alter echo_word to echo_word concatenated with '!!!'.
Call the function echo_shout(), passing it a single argument 'hello'.

## Functions with one default argument
100xp
In the previous chapter, you've learned to define functions with more than one parameter and then calling those functions by passing the required number of arguments. In the last video, Hugo built on this idea by showing you how to define functions with default arguments. You will practice that skill in this exercise by writing a function that uses a default argument and then calling the function a couple of times.
### Instructions
Complete the function header with the function name shout_echo. It accepts an argument word1 and a default argument echo with default value 1, in that order.
Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
Call shout_echo() with just the string, "Hey". Assign the result to no_echo.
Call shout_echo() with the string "Hey" and the value 5 for the default argument, echo. Assign the result to with_echo.

## Functions with multiple default arguments
100xp
You've now defined a function that uses a default argument - don't stop there just yet! You will now try your hand at defining a function with more than one default argument and then calling this function in various ways.
After defining the function, you will call it by supplying values to all the default arguments of the function. Additionally, you will call the function by not passing a value to one of the default arguments - see how that changes the output of your function!
### Instructions
Complete the function header with the function name shout_echo. It accepts an argument word1, a default argument echo with default value 1 and a default argument intense with default value False, in that order.
In the body of the if statement, capitalize the string object echo_word by applying the method .upper() on it.
Call shout_echo() with the string, "Hey", the value 5for echo and the value True for intense. Assign the result to with_big_echo.
Call shout_echo() with the string "Hey" and the value True for intense. Assign the result to big_no_echo.
## Function with variable-length arguments (*args)
100xp
Flexible arguments enable you to pass a variable number of arguments to a function. In this exercise, you will practice defining a function that accepts a variable number of string arguments.
The function you will define is gibberish() which can accept a variable number of string values. Its return value is a single string composed of all the string arguments concatenated together in the order they were passed to the function call. You will call the function with a single string argument and see how the output changes with another call using more than one string argument. Recall from the previous video that, within the function definition, args is a tuple.
### Instructions
Complete the function header with the function name gibberish. It accepts a single flexible argument *args.
Initialize a variable hodgepodge to an empty string.
Return the variable hodgepodge at the end of the function body.
Call gibberish() with the single string, "luke". Assign the result to one_word.
Hit the Submit button to call gibberish() with multiple arguments and to print the value to the Shell.’’
## Function with variable-length keyword arguments (**kwargs)
100xp
Let's push further on what you've learned about flexible arguments - you've used *args, you're now going to use **kwargs! What makes **kwargs different is that it allows you to pass a variable number of keyword arguments to functions. Recall from the previous video that, within the function definition, kwargs is a dictionary.
To understand this idea better, you're going to use **kwargs in this exercise to define a function that accepts a variable number of keyword arguments. The function simulates a simple status report system that prints out the status of a character in a movie.
### Instructions
Complete the function header with the function name report_status. It accepts a single flexible argument **kwargs.
Iterate over the key-value pairs of kwargs to print out the keys and values, separated by a colon ':'.
In the first call to report_status(), pass the following keyword-value pairs: name="luke", affiliation="jedi"and status="missing".
In the second call to report_status(), pass the following keyword-value pairs: name="anakin", affiliation="sith lord" and status="deceased".
## Bringing it all together (1)
100xp
Recall the Bringing it all together exercise in the previous chapter where you did a simple Twitter analysis by developing a function that counts how many tweets are in certain languages. The output of your function was a dictionary that had the language as the keys and the counts of tweets in that language as the value.
In this exercise, we will generalize the Twitter language analysis that you did in the previous chapter. You will do that by including a default argumentthat takes a column name.
For your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DataFrame tweets_df. Parts of the code from your previous work are also provided.
### Instructions
Complete the function header by supplying the parameter for a DataFrame df and the parameter col_name with a default value of 'lang' for the DataFrame column name.
Call count_entries() by passing the tweets_dfDataFrame and the column name 'lang'. Assign the result to result1. Note that since 'lang' is the default value of the col_name parameter, you don't have to specify it here.
Call count_entries() by passing the tweets_dfDataFrame and the column name 'source'. Assign the result to result2.

## Bringing it all together (2)
100xp
Wow, you've just generalized your Twitter language analysis that you did in the previous chapter to include a default argument for the column name. You're now going to generalize this function one step further by allowing the user to pass it a flexible argument, that is, in this case, as many column names as the user would like!
Once again, for your convenience, pandas has been imported as pdand the 'tweets.csv' file has been imported into the DataFrame tweets_df. Parts of the code from your previous work are also provided.
### Instructions
Complete the function header by supplying the parameter for the dataframe df and the flexible argument *args.
Complete the for loop within the function definition so that the loop occurs of the tuple args.
Call count_entries() by passing the tweets_dfDataFrame and the column name 'lang'. Assign the result to result1.
Call count_entries() by passing the tweets_dfDataFrame and the column names 'lang' and 'source'. Assign the result to result2.




