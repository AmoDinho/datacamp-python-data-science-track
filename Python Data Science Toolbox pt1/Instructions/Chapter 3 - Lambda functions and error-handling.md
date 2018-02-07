# Chapter 3Lambda functions and error-handling

## Writing a lambda function you already know
100xp
Some function definitions are simple enough that they can be converted to a lambda function. By doing this, you write less lines of code, which is pretty awesome and will come in handy, especially when you're writing and maintaining big programs. In this exercise, you will use what you know about lambda functions to convert a function that does a simple task into a lambda function. Take a look at this function definition:
def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words


The function echo_word takes 2 parameters: a string value, word1 and an integer value, echo. It returns a string that is a concatenation of echo copies of word1. Your task is to convert this simple function into a lambda function.
### Instructions
- Define the lambda function echo_word using the variables word1 and echo. Replicate what the original function definition for echo_word() does above.
- Call echo_word() with the string argument 'hey' and the value 5, in that order. Assign the call to result.

## Map() and lambda functions
100xp
So far, you've used lambda functions to write short, simple functions as well as to redefine functions with simple functionality. The best use case for lambda functions, however, are for when you want these simple functionalities to be anonymously embedded within larger expressions. What that means is that the functionality is not stored in the environment, unlike a function defined with def. To understand this idea better, you will use a lambda function in the context of the map() function.
Recall from the video that map() applies a function over an object, such as a list. Here, you can use lambda functions to define the function that map() will use to process the object. For example:
nums = [2, 4, 6, 8, 10]

result = map(lambda a: a ** 2, nums)


You can see here that a lambda function, which raises a value a to the power of 2, is passed to map() alongside a list of numbers, nums. The map object that results from the call to map() is stored in result. You will now practice the use of lambda functions with map(). For this exercise, you will map the functionality of the add_bangs() function you defined in previous exercises over a list of strings.
### Instructions
- In the map() call, pass a lambda function that concatenates the string '!!!' to a string item; also pass the list of strings, spells. Assign the resulting map object to shout_spells.
- Convert shout_spells to a list and print out the list.

## Filter() and lambda functions
100xp
In the previous exercise, you used lambda functions to anonymously embed an operation within map(). You will practice this again in this exercise by using a lambda function with filter(), which may be new to you! The function filter() offers a way to filter out elements from a list that don't satisfy certain criteria.
Your goal in this exercise is to use filter() to create, from an input list of strings, a new list that contains only strings that have more than 6 characters.
### Instructions
- In the filter() call, pass a lambda function and the list of strings, fellowship. The lambda function should check if the number of characters in a string member is greater than 6; use the len() function to do this. Assign the resulting filter object to result.
- Convert result to a list and print out the list.

## Reduce() and lambda functions
100xp
You're getting very good at using lambda functions! Here's one more function to add to your repertoire of skills. The reduce() function is useful for performing some computation on a list and, unlike map() and filter(), returns a single value as a result. To use reduce(), you must import it from the functools module.
Remember gibberish() from a few exercises back?
# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""
    hodgepodge = ''
    for word in args:
        hodgepodge += word
    return hodgepodge


gibberish() simply takes a list of strings as an argument and returns, as a single-value result, the concatenation of all of these strings. In this exercise, you will replicate this functionality by using reduce() and a lambda function that concatenates strings together.
### Instructions
- Import the reduce function from the functools module.
- In the reduce() call, pass a lambda function that takes two string arguments item1 and item2 and concatenates them; also pass the list of strings, stark. Assign the result to result. The first argument to reduce() should be the lambda function and the second argument is the list stark.

## Error handling with try-except
100xp
A good practice in writing your own functions is also anticipating the ways in which other people (or yourself, if you accidentally misuse your own function) might use the function you defined.
As in the previous exercise, you saw that the len() function is able to handle input arguments such as strings, lists, and tuples, but not int type ones and raises an appropriate error and error message when it encounters invalid input arguments. One way of doing this is through exception handling with the try-except block.
In this exercise, you will define a function as well as use a try-exceptblock for handling cases when incorrect input arguments are passed to the function.
Recall the shout_echo() function you defined in previous exercises; parts of the function definition are provided in the sample code. Your goal is to complete the exception handling code in the function definition and provide an appropriate error message when raising an error.
### Instructions
- Initialize the variables echo_word and shout_words to empty strings.
- Add the keywords try and except in the appropriate locations for the exception handling block.
- Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
- Concatenate the string '!!!' to echo_word. Assign the result to shout_words.
## Error handling by raising an error
100xp
Another way to raise an error is by using raise. In this exercise, you will add a raise statement to the shout_echo() function you defined before to raise an error message when the value supplied by the user to the echo argument is less than 0.
The call to shout_echo() uses valid argument values. To test and see how the raise statement works, simply change the value for the echoargument to a negative value. Don't forget to change it back to valid values to move on to the next exercise!
### Instructions
- Complete the if statement by checking if the value of echois less than 0.
- In the body of the if statement, add a raise statement that raises the error message 'echo must be greater than 0' when the value supplied by the user to echo is less than 0.

## Bringing it all together (1)
100xp
This is awesome! You have now learned how to write anonymous functions using lambda, how to pass lambda functions as arguments to other functions such as map(), filter(), and reduce(), as well as how to write errors and output custom error messages within your functions. You will now put together these learnings to good use by working with a Twitter dataset. Before practicing your new error handling skills,in this exercise, you will write a lambda function and use filter() to select retweets, that is, tweets that begin with the string 'RT'.
To help you accomplish this, the Twitter data has been imported into the DataFrame, tweets_df. Go for it!
### Instructions
- In the filter() call, pass a lambda function and the sequence of tweets as strings, tweets_df['text']. The lambda function should check if the first 2 characters in a tweet x are 'RT'. Assign the resulting filter object to result. To get the first 2 characters in a tweet x, use x[0:2]. To check equality, use a Boolean filter with ==.
- Convert result to a list and print out the list.

## Bringing it all together (2)
100xp
Sometimes, we make mistakes when calling functions - even ones you made yourself. But don't fret! In this exercise, you will improve on your previous work with the count_entries() function in the last chapter by adding a try-except block to it. This will allow your function to provide a helpful message when the user calls your count_entries() function but provides a column name that isn't in the DataFrame.
Once again, for your convenience, pandas has been imported as pdand the 'tweets.csv' file has been imported into the DataFrame tweets_df. Parts of the code from your previous work are also provided.
### Instructions
- Add a try block so that when the function is called with the correct arguments, it processes the DataFrame and returns a dictionary of results.
- Add an except block so that when the function is called incorrectly, it displays the following error message: 'The DataFrame does not have a ' + col_name + ' column.'.


## Bringing it all together (3)
100xp
In the previous exercise, you built on your function count_entries() to add a try-except block. This was so that users would get helpful messages when calling your count_entries() function and providing a column name that isn't in the DataFrame. In this exercise, you'll instead raise a ValueError in the case that the user provides a column name that isn't in the DataFrame.
Once again, for your convenience, pandas has been imported as pdand the 'tweets.csv' file has been imported into the DatFrame tweets_df. Parts of the code from your previous work are also provided.
### Instructions
- If col_name is NOT a column in the DataFrame df, raise a ValueError 'The DataFrame does not have a ' + col_name + ' column.'.
- Call your new function count_entries() to analyze the 'lang' column of tweets_df. Store the result in result1.
- Print result1. This has been done for you, so hit 'Submit Answer' to check out the result. In the next exercise, you'll see that it raises the necessary ValueErrors.

