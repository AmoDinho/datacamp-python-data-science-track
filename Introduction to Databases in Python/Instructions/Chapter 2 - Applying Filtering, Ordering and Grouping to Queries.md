# Chapter 2 - Applying Filtering, Ordering and Grouping to Queries

## Connecting to a PostgreSQL Database
In these exercises, you will be working with real databases hosted on the cloud via Amazon Web Services (AWS)!
Let's begin by connecting to a PostgreSQL database. When connecting to a PostgreSQL database, many prefer to use the psycopg2 database driver as it supports practically all of PostgreSQL's features efficiently and is the standard dialect for PostgreSQL in SQLAlchemy.
You might recall from Chapter 1 that we use the create_engine() function and a connection string to connect to a database.
There are three components to the connection string in this exercise: the dialect and driver ('postgresql+psycopg2://'), followed by the username and password ('student:datacamp'), followed by the host and port ('@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/'), and finally, the database name ('census'). You will have to pass this string as an argument to create_engine() in order to connect to the database.

### INSTRUCTIONS
50XP
Import create_engine from sqlalchemy.
Create an engine to the census database by concatenating the following strings:
'postgresql+psycopg2://'
'student:datacamp'
'@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com'
':5432/census'
Use the .table_names() method on engine to print the table names.

## Filter data selected from a Table - Simple
Having connected to the database, it's now time to practice filtering your queries!
As mentioned in the video, a where() clause is used to filter the data that a statement returns. For example, to select all the records from the census table where the sex is Female (or 'F') we would do the following:
select([census]).where(census.columns.sex == 'F')
In addition to == we can use basically any python comparison operator (such as <=, !=, etc) in the where() clause.
### INSTRUCTIONS
100XP
Select all records from the census table by passing in census as a list to select().
Append a where clause to stmt to return only the records with a state of 'New York'.
Execute the statement stmt using .execute() and retrieve the results using .fetchall().
Iterate over results and print the age, sex and pop2008 columns from each record. For example, you can print out the age of result with result.age.

## Filter data selected from a Table - Expressions
In addition to standard Python comparators, we can also use methods such as in_() to create more powerful where()clauses. You can see a full list of expressions in the SQLAlchemy Documentation.
We've already created a list of some of the most densely populated states.
### INSTRUCTIONS
100XP
Select all records from the census table by passing it in as a list to select().
Append a where clause to return all the records with a statein the states list. Use in_(states) on census.columns.state to do this.
Loop over the ResultProxy connection.execute(stmt) and print the state and pop2000 columns from each record.


## Filter data selected from a Table - Advanced
You're really getting the hang of this! SQLAlchemy also allows users to use conjunctions such as and_(), or_(), and not_() to build more complex filtering. For example, we can get a set of records for people in New York who are 21 or 37 years old with the following code:
stmt([census]).where(
  and_(census.columns.state == 'New York',
       or_(census.columns.age == 21,
          census.columns.age == 37
         )
      )
  )


### INSTRUCTIONS
100XP
Import and_ from the sqlalchemy module.
Select all records from the census table.
Append a where clause to filter all the records whose state is 'California', and whose sex is not 'M'.
Iterate over the ResultProxy and print the age and sexcolumns from each record.


## Ordering by a Single Column
To sort the result output by a field, we use the .order_by()method. By default, the .order_by() method sorts from lowest to highest on the supplied column. You just have to pass in the name of the column you want sorted to .order_by(). In the video, for example, Jason used stmt.order_by(census.columns.state) to sort the result output by the state column.

### INSTRUCTIONS
100XP
Select all records of the state column from the censustable. To do this, pass census.columns.state as a list to select().
Append an .order_by() to sort the result output by the state column.
Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
Print the first 10 rows of results.

## Ordering in Descending Order by a Single Column
You can also use .order_by() to sort from highest to lowest by wrapping a column in the desc() function. Although you haven't seen this function in action, it generalizes what you have already learned.
All you have to just pass in desc() inside an .order_by() with the name of the column you want to sort by. For instance, stmt.order_by(desc(table.columns.column_name)) sorts column_name in descending order.

### INSTRUCTIONS
100XP
Import desc from the sqlalchemy module.
Select all records of the state column from the censustable.
Append an .order_by() to sort the result output by the state column in descending order. Save the result as rev_stmt.
Execute rev_stmt using connection.execute() and fetch all the results with .fetchall(). Save them as rev_results.
Print the first 10 rows of rev_results.

## Ordering by Multiple Columns
We can pass multiple arguments to the .order_by() method to order by multiple columns. In fact, we can also sort in ascending or descending order for each individual column. Each column in the .order_by() method is fully sorted from left to right. This means that the first column is completely sorted, and then within each matching group of values in the first column, it's sorted by the next column in the .order_by() method. This process is repeated until all the columns in the .order_by() are sorted.
### INSTRUCTIONS
100XP
Select all records of the state and age columns from the census table.
Use .order_by() to sort the output of the state column in ascending order and age in descending order. (NOTE: descis already imported).
Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
Print the first 20 results.

## Counting Distinct Data
As mentioned in the video, SQLAlchemy's func module provides access to built-in SQL functions that can make operations like counting and summing faster and more efficient.
In the video, Jason used func.sum() to get a sum of the pop2008 column of census as shown below:
select([func.sum(census.columns.pop2008)])


If instead you want to count the number of values in pop2008, you could use func.count() like this:
select([func.count(census.columns.pop2008)])


Furthermore, if you only want to count the distinct values of pop2008, you can use the .distinct() method:
select([func.count(census.columns.pop2008.distinct())])


In this exercise, you will practice using func.count() and .distinct() to get a count of the distinct number of states in census.
So far, you've seen .fetchall() and .first() used on a ResultProxy to get the results. The ResultProxy also has a method called .scalar() for getting just the value of a query that returns only one row and column.
This can be very useful when you are querying for just a count or sum.
### INSTRUCTIONS
100XP
Build a select statement to count the distinct values in the state field of census.
Execute stmt to get the count and store the results as distinct_state_count.
Print the value of distinct_state_count.


## Count of Records by State
Often, we want to get a count for each record with a particular value in another column. The .group_by() method helps answer this type of query. You can pass a column to the .group_by() method and use in a aggregate function like sum() or count(). Much like the .order_by() method, .group_by() can take multiple columns as arguments.

INSTRUCTIONS
100XP
Import func from sqlalchemy.
Build a select statement to get the value of the state field and a count of the values in the age field, and store it as stmt.
Use the .group_by() method to group the statement by the state column.
Execute stmt using the connection to get the count and store the results as results.
Print the keys/column names of the results returned using results[0].keys().
## Determining the Population Sum by State
To avoid confusion with query result column names like count_1, we can use the .label() method to provide a name for the resulting column. This gets appended to the function method we are using, and its argument is the name we want to use.
We can pair func.sum() with .group_by() to get a sum of the population by State and use the label() method to name the output.
We can also create the func.sum() expression before using it in the select statement. We do it the same way we would inside the select statement and store it in a variable. Then we use that variable in the select statement where the func.sum() would normally be.

### INSTRUCTIONS
100XP
Import func from sqlalchemy.
Build an expression to calculate the sum of the values in the pop2008 field labeled as population.
Build a select statement to get the value of the state field and the sum of the values in pop2008.
Group the statement by state using a .group_by() method.
Execute stmt using the connection to get the count and store the results as results.
Print the keys/column names of the results returned using results[0].keys().

## SQLAlchemy ResultsProxy and Pandas Dataframes
We can feed a ResultProxy directly into a pandas DataFrame, which is the workhorse of many Data Scientists in PythonLand. Jason demonstrated this in the video. In this exercise, you'll follow exactly the same approach to convert a ResultProxy into a DataFrame.
### INSTRUCTIONS
100XP
Import pandas as pd.
Create a DataFrame df using pd.DataFrame() on the ResultProxy results.
Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
Print the DataFrame.


## From SQLAlchemy results to a Graph
We can also take advantage of pandas and Matplotlib to build figures of our data. Remember that data visualization is essential for both exploratory data analysis and communication of your data!

### INSTRUCTIONS
100XP
Import matplotlib.pyplot as plt.
Create a DataFrame df using pd.DataFrame() on the provided results.
Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
Print the DataFrame df.
Use the plot.bar() method on df to create a bar plot of the results.
Display the plot with plt.show().


