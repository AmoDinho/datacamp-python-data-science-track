# Chapter 5 - Putting it all together
## Setup the Engine and MetaData
In this exercise, your job is to create an engine to the database that will be used in this chapter. Then, you need to initialize its metadata.
Recall how you did this in Chapter 1 by leveraging create_engine() and MetaData.
### INSTRUCTIONS
100XP
Import create_engine and MetaData from sqlalchemy.
Create an engine to the chapter 5 database by using 'sqlite:///chapter5.sqlite' as the connection string.
Create a MetaData object as metadata.


## Create the Table to the Database
Having setup the engine and initialized the metadata, you will now define the census table object and then create it in the database using using the metadata and engine from the previous exercise. To create it in the database, you will have to use the .create_all() method on the metadata with engine as the argument.
It may help to refer back to the Chapter 4 exercise in which you learned how to create a table.

### INSTRUCTIONS
100XP
Import Table, Column, String, and Integer from sqlalchemy.
Define a census table with the following columns:
'state' - String - length of 30
'sex' - String - length of 1
'age' - Integer
'pop2000' - Integer
'pop2008' - Integer
Create the table in the database using the metadata and engine.
## Reading the Data from the CSV
Leverage the Python CSV module from the standard library and load the data into a list of dictionaries.
It may help to refer back to the Chapter 4 exercise in which you did something similar.

### INSTRUCTIONS
100XP
Create an empty list called values_list.
Iterate over the rows of csv_reader with a for loop, creating a dictionary called data for each row and append it to values_list.
Within the for loop, row will be a list whose entries are 'state' , 'sex', 'age', 'pop2000' and 'pop2008'(in that order).
## Load Data from a list into the Table
Using the multiple insert pattern, in this exercise, you will load the data from values_list into the table.
### INSTRUCTIONS
100XP
Import insert from sqlalchemy.
Build an insert statement for the census table.
Execute the statement stmt along with values_list. You will need to pass them both as arguments to connection.execute().
Print the rowcount attribute of results.

## Build a Query to Determine the Average Age by Population
In this exercise, you will use the func.sum() and group_by()methods to first determine the average age weighted by the population in 2008, and then group by sex.
As Jason discussed in the video, a weighted average is calculated as the sum of the product of the weights and averages divided by the sum of all the weights.
For example, the following statement determines the average age weighted by the population in 2000:
stmt = select([census.columns.sex,
               (func.sum(census.columns.pop2000 * census.columns.age) /
                func.sum(census.columns.pop2000)).label('average_age')
               ])


### INSTRUCTIONS
100XP
Import select from sqlalchemy.
Build a statement to:
Select sex from the census table.
Select the average age weighted by the population in 2008 (pop2008). See the example given in the assignment text to see how you can do this. Label this average age calculation as 'average_age'.
Group the query by sex.
Execute the query and store it as results.
Loop over results and print the sex and average_age for each record.
## Build a Query to Determine the Percentage of Population by Gender and State
In this exercise, you will write a query to determine the percentage of the population in 2000 that comprised of women. You will group this query by state.

### INSTRUCTIONS
100XP
Import case, cast and Float from sqlalchemy.
Define a statement to select state and the percentage of females in 2000.
Inside func.sum(), use case() to select females (using the sex column) from pop2000. Remember to specify else_=0 if the sex is not 'F'.
To get the percentage, divide the number of females in the year 2000 by the overall population in 2000. Cast the divisor - census.columns.pop2000 - to Float before multiplying by 100.
Group the query by state.
Execute the query and store it as results.
Print state and percent_female for each record. This has been done for you, so hit 'Submit Answer' to see the result.


## Build a Query to Determine the Difference by State from the 2000 and 2008 Censuses
In this final exercise, you will write a query to calculate the states that changed the most in population. You will limit your query to display only the top 10 states.

### INSTRUCTIONS
100XP
Build a statement to:
Select state.
Calculate the difference in population between 2008 (pop2008) and 2000 (pop2000).
Group the query by census.columns.stateusing the .group_by()method on stmt.
Order by 'pop_change'in descending order using the .order_by()method with the desc()function on 'pop_change'.
Limit the query to the top 10 states using the .limit() method.
Execute the query and store it as results.
Print the state and the population change for each result. This has been done for you, so hit 'Submit Answer' to see the result!


