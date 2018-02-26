# Chapter 1 - Introduction and flat files
## Importing entire text files
100xp
In this exercise, you'll be working with the file moby_dick.txt. It is a text file that contains the opening sentences of Moby Dick, one of the great American novels! Here you'll get experience opening a text file, printing its contents to the shell and, finally, closing it.

### Instructions
Open the file moby_dick.txt as read-only and store it in the variable file. Make sure to pass the filename enclosed in quotation marks ''.
Print the contents of the file to the shell using the print()function. As Hugo showed in the video, you'll need to apply the method read() to the object file.
Check whether the file is closed by executing print(file.closed).
Close the file using the close() method.
Check again that the file is closed as you did above.

## Importing text files line by line
100xp
For large files, we may not want to print all of their content to the shell: you may wish to print only the first few lines. Enter the readline() method, which allows you to do this. When a file called file is open, you can print out the first line by executing file.readline(). If you execute the same command again, the second line will print, and so on.
In the introductory video, Hugo also introduced the concept of a context manager. He showed that you can bind a variable file by using a context manager construct:
with open('huck_finn.txt') as file:


While still within this construct, the variable file will be bound to open('huck_finn.txt'); thus, to print the file to the shell, all the code you need to execute is:
with open('huck_finn.txt') as file:
    print(file.read())


You'll now use these tools to print the first few lines of moby_dick.txt!
### Instructions
Open moby_dick.txt using the with context manager and the variable file.
Print the first three lines of the file to the shell by using readline() three times within the context manager.

## Using NumPy to import flat files
100xp
In this exercise, you're now going to load the MNIST digit recognition dataset using the numpy function loadtxt() and see just how easy it can be:
The first argument will be the filename.
The second will be the delimiter which, in this case, is a comma.
You can find more information about the MNIST dataset here on the webpage of Yann LeCun, who is currently Director of AI Research at Facebook and Founding Director of the NYU Center for Data Science, among many other things.

### Instructions
Fill in the arguments of np.loadtxt() by passing file and a comma ',' for the delimiter.
Fill in the argument of print() to print the type of the object digits. Use the function type().
Execute the rest of the code to visualize one of the rows of the data.

## Customizing your NumPy import
100xp
What if there are rows, such as a header, that you don't want to import? What if your file has a delimiter other than a comma? What if you only wish to import particular columns?
There are a number of arguments that np.loadtxt() takes that you'll find useful: delimiter changes the delimiter that loadtxt() is expecting, for example, you can use ',' and '\t' for comma-delimited and tab-delimited respectively; skiprows allows you to specifyhow many rows (not indices) you wish to skip; usecols takes a list of the indices of the columns you wish to keep.
The file that you'll be importing, digits_header.txt,
has a header
is tab-delimited.

### Instructions
Complete the arguments of np.loadtxt(): the file you're importing is tab-delimited, you want to skip the first row and you only want to import the first and third columns.
Complete the argument of the print() call in order to print the entire array that you just imported.

## Importing different datatypes
100xp
The file seaslug.txt
has a text header, consisting of strings
is tab-delimited.
These data consists of percentage of sea slug larvae that had metamorphosed in a given time period. Read more here.
Due to the header, if you tried to import it as-is using np.loadtxt(), Python would throw you a ValueError and tell you that it could not convert string to float. There are two ways to deal with this: firstly, you can set the data type argument dtype equal to str (for string).
Alternatively, you can skip the first row as we have seen before, using the skiprows argument.

### Instructions
Complete the first call to np.loadtxt() by passing file as the first argument.
Execute print(data[0]) to print the first element of data.
Complete the second call to np.loadtxt(). The file you're importing is tab-delimited, the datatype is float, and you want to skip the first row.
Print the 10th element of data_float by completing the print() command. Be guided by the previous print()call.
Execute the rest of the code to visualize the data.


## Working with mixed datatypes (1)
50xp
Much of the time you will need to import datasets which have different datatypes in different columns; one column may contain strings and another floats, for example. The functionnp.loadtxt() will freak at this. There is another function, np.genfromtxt(), which can handle such structures. If we pass dtype=None to it, it will figure out what types each column should be.
Import 'titanic.csv' using the function np.genfromtxt() as follows:
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)


Here, the first argument is the filename, the second specifies the delimiter , and the third argument names tells us there is a header. Because the data are of different types, data is an object called a structured array. Because numpy arrays have to contain elements that are all the same type, the structured array solves this by being a 1D array, where each element of the array is a row of the flat file imported. You can test this by checking out the array's shape in the shell by executing np.shape(data).
Acccessing rows and columns of structured arrays is super-intuitive: to get the ith row, merely execute data[i] and to get the column with name 'Fare', execute data['Fare'].
Print the entire column with name Survived to the shell. What are the last 4 values of this column?


## Working with mixed datatypes (2)
100xp
You have just used np.genfromtxt() to import data containing mixed datatypes. There is also another function np.recfromcsv() that behaves similarly to np.genfromtxt(), except that its default dtype is None. In this exercise, you'll practice using this to achieve the same result.
 
 ### Instructions
Import titanic.csv using the function np.recfromcsv()and assign it to the variable, d. You'll only need to pass file to it because it has the defaults delimiter=',' and names=True in addition to dtype=None!
Run the remaining code to print the first three entries of the resulting array d.


## Using pandas to import flat files as DataFrames (1)
100xp
In the last exercise, you were able to import flat files containing columns with different datatypes as numpy arrays. However, the DataFrame object in pandas is a more appropriate structure in which to store such data and, thankfully, we can easily import files of mixed data types as DataFrames using the pandas functions read_csv() and read_table().

### Instructions
Import the pandas package using the alias pd.
Read titanic.csv into a DataFrame called df. The file name is already stored in the file object.
In a print() call, view the head of the DataFrame.

##Using pandas to import flat files as DataFrames (2)
0xp
In the last exercise, you were able to import flat files into a pandasDataFrame. As a bonus, it is then straightforward to retrieve the corresponding numpy array using the attribute values. You'll now have a chance to do this using the MNIST dataset, which is available as digits.csv.

### Instructions
Import the first 5 rows of the file into a DataFrame using the function pd.read_csv() and assign the result to data. You'll need to use the arguments nrows and header (there is no header in this file).
Build a numpy array from the resulting DataFrame in dataand assign to data_array.
Execute print(type(data_array)) to print the datatype of data_array

## Customizing your pandas import
100xp
The pandas package is also great at dealing with many of the issues you will encounter when importing data as a data scientist, such as comments occurring in flat files, empty lines and missing values. Note that missing values are also commonly referred to as NA or NaN. To wrap up this chapter, you're now going to import a slightly corrupted copy of the Titanic dataset titanic_corrupt.txt, which
contains comments after the character '#'
is tab-delimited.

### Instructions
Complete the sep (the pandas version of delim), comment and na_values arguments of pd.read_csv(). comment takes characters that comments occur after in the file, which in this case is '#'. na_values takes a list of strings to recognize as NA/NaN, in this case the string 'Nothing'.
Execute the rest of the code to print the head of the resulting DataFrame and plot the histogram of the 'Age' of passengers aboard the Titanic.


