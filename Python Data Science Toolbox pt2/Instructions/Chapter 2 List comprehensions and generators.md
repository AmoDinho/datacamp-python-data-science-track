# Chapter 2 List comprehensions and generators

## Writing list comprehensions
100xp
You now have all the knowledge necessary to begin writing list comprehensions! Your job in this exercise is to write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9.

### Instructions
Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable, write a list comprehension that produces a list of numbers consisting of the squared values of i.

## Nested list comprehensions
100xp
Great! At this point, you have a good grasp of the basic syntax of list comprehensions. Let's push your code-writing skills a little further. In this exercise, you will be writing a list comprehension within another list comprehension, or nested list comprehensions. It sounds a little tricky, but you can do it!
Let's step aside for a while from strings. One of the ways in which lists can be used are in representing multi-dimension objects such as matrices. Matrices can be represented as a list of lists in Python. For example a 5 x 5 matrix with values 0 to 4 in each row can be written as:
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]


Your task is to recreate this matrix by using nested listed comprehensions. Recall that you can create one of the rows of the matrix with a single list comprehension. To create the list of lists, you simply have to supply the list comprehension as the output expression of the overall list comprehension:
[[output expression] for iterator variable in iterable]
Note that here, the output expression is itself a list comprehension.

### Instructions
In the inner list comprehension - that is, the output expressionof the nested list comprehension - create a list of values from 0to 4 using range(). Use col as the iterator variable.
In the iterable part of your nested list comprehension, use range() to count 5 rows - that is, create a list of values from 0 to 4. Use row as the iterator variable; note that you won't be needing this to create values in the list of lists.

## Using conditionals in comprehensions (1)
0xp
You've been using list comprehensions to build lists of values, sometimes using operations to create these values.
An interesting mechanism in list comprehensions is that you can also create lists with values that meet only a certain condition. One way of doing this is by using conditionals on iterator variables. In this exercise, you will do exactly that!
Recall from the video that you can apply a conditional statement to test the iterator variable by adding an if statement in the optional predicate expression part after the for statement in the comprehension:
[ output expression for iterator variable in iterable if predicate expression ].
You will use this recipe to write a list comprehension for this exercise. You are given a list of strings fellowship and, using a list comprehension, you will create a list that only includes the members of fellowship that have 7 characters or more.

### Instructions
Use member as the iterator variable in the list comprehension. For the conditional, use len() to evaluate the iterator variable. Note that you only want strings with 7 characters or more.

## Using conditionals in comprehensions (2)
100xp
In the previous exercise, you used an if conditional statement in the predicate expression part of a list comprehension to evaluate an iterator variable. In this exercise, you will use an if-else statement on the output expression of the list.
You will work on the same list, fellowship and, using a list comprehension and an if-else conditional statement in the output expression, create a list that keeps members of fellowship with 7 or more characters and replaces others with an empty string. Use member as the iterator variable in the list comprehension.

### Instructions
In the output expression, keep the string as-is if the number of characters is >= 7, else replace it with an empty string - that is, '' or "".

## Dict comprehensions
100xp
Comprehensions aren't relegated merely to the world of lists. There are many other objects you can build using comprehensions, such as dictionaries, pervasive objects in Data Science. You will create a dictionary using the comprehension syntax for this exercise. In this case, the comprehension is called a dict comprehension.
Recall that the main difference between a list comprehension and a dict comprehension is the use of curly braces {} instead of []. Additionally, members of the dictionary are created using a colon :, as in key:value.
You are given a list of strings fellowship and, using a dict comprehension, create a dictionary with the members of the list as the keysand the length of each string as the corresponding values.

### Instructions
Create a dict comprehension where the key is a string in fellowship and the value is the length of the string. Remember to use the syntax key:value in the output expressionpart of the comprehension to create the members of the dictionary. Use member as the iterator variable.

## Write your own generator expressions
100xp
You are familiar with what generators and generator expressions are, as well as its difference from list comprehensions. In this exercise, you will practice building generator expressions on your own.
Recall that generator expressions basically have the same syntax as list comprehensions, except that it uses parentheses () instead of brackets []; this should make things feel familiar! Furthermore, if you have ever iterated over a dictionary with .items(), or used the range()function, for example, you have already encountered and used generators before, without knowing it! When you use these functions, Python creates generators for you behind the scenes.
Now, you will start simple by creating a generator object that produces numeric values.

### Instructions
Create a generator object that will produce values from 0 to 30. Assign the result to result and use num as the iterator variable in the generator expression.
Print the first 5 values by using next() appropriately in print().
Print the rest of the values by using a for loop to iterate over the generator object.

## Changing the output in generator expressions
100xp
Great! At this point, you already know how to write a basic generator expression. In this exercise, you will push this idea a little further by adding to the output expression of a generator expression. Because generator expressions and list comprehensions are so alike in syntax, this should be a familiar task for you!
You are given a list of strings lannister and, using a generator expression, create a generator object that you will iterate over to print its values.

### Instructions
Write a generator expression that will generate the lengths of each string in lannister. Use person as the iterator variable. Assign the result to lengths.
Supply the correct iterable in the for loop for printing the values in the generator object.



## Build a generator
100xp
In previous exercises, you've dealt mainly with writing generator expressions, which uses comprehension syntax. Being able to use comprehension syntax for generator expressions made your work so much easier!
Now, recall from the video that not only are there generator expressions, there are generator functions as well. Generator functions are functions that, like generator expressions, yield a series of values, instead of returning a single value. A generator function is defined as you do a regular function, but whenever it generates a value, it uses the keyword yield instead of return.
In this exercise, you will create a generator function with a similar mechanism as the generator expression you defined in the previous exercise:
lengths = (len(person) for person in lannister)


### Instructions
Complete the function header for the function get_lengths() that has a single parameter, input_list.
In the for loop in the function definition, yield the lengthof the strings in input_list.
Complete the iterable part of the for loop for printing the values generated by the get_lengths() generator function. Supply the call to get_lengths(), passing in the list lannister.

## List comprehensions for time-stamped data
0xp
You will now make use of what you've learned from this chapter to solve a simple data extraction problem. You will also be introduced to a data structure, the pandas Series, in this exercise. We won't elaborate on it much here, but what you should know is that it is a data structure that you will be working with a lot of times when analyzing data from pandas DataFrames. You can think of DataFrame columns as single-dimension arrays called Series.
In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data. The pandas package has been imported as pd and the file 'tweets.csv' has been imported as the dfDataFrame for your use.

### Instructions
Extract the column 'created_at' from df and assign the result to tweet_time. Fun fact: the extracted column in tweet_time here is a Series data structure!
Create a list comprehension that extracts the time from each row in tweet_time. Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. Use entry as the iterator variableand assign the result to tweet_clock_time. Remember that Python uses 0-based indexing!

## Conditional list comprehesions for time-stamped data
100xp
Great, you've successfully extracted the data of interest, the time, from a pandas DataFrame! Let's tweak your work further by adding a conditional that further specifies which entries to select.
In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data. You will add a conditional expression to the list comprehension so that you only select the times in which entry[17:19] is equal to '19'. The pandas package has been imported as pd and the file 'tweets.csv' has been imported as the df DataFrame for your use.

### Instructions
Extract the column 'created_at' from df and assign the result to tweet_time.
Create a list comprehension that extracts the time from each row in tweet_time. Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. Use entry as the iterator variableand assign the result to tweet_clock_time. Additionally, add a conditional expression that checks whether entry[17:19]is equal to '19'.
