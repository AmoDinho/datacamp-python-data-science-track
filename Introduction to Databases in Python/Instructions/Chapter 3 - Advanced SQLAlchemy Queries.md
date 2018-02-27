# Chapter 3 - Advanced SQLAlchemy Queries

## Connecting to a MySQL Database
Before you jump into the calculation exercises, let's begin by connecting to our database. Recall that in the last chapter you connected to a PostgreSQL database. Now, you'll connect to a MySQL database, for which many prefer to use the pymysqldatabase driver, which, like psycopg2 for PostgreSQL, you have to install prior to use.
This connection string is going to start with 'mysql+pymysql://', indicating which dialect and driver you're using to establish the connection. The dialect block is followed by the 'username:password' combo. Next, you specify the host and port with the following '@host:port/'. Finally, you wrap up the connection string with the 'database_name'.
Now you'll practice connecting to a MySQL database: it will be the same census database that you have already been working with. One of the great things about SQLAlchemy is that, after connecting, it abstracts over the type of database it has connected to and you can write the same SQLAlchemy code, regardless!
### INSTRUCTIONS
100XP
Import the create_engine function from the sqlalchemylibrary.
Create an engine to the census database by concatenating the following strings and passing them to create_engine():
'mysql+pymysql://' (the dialect and driver).
'student:datacamp' (the username and password).
'@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/'(the host and port).
'census' (the database name).
Use the .table_names() method on engine to print the table names.


## Calculating a Difference between Two Columns
Often, you'll need to perform math operations as part of a query, such as if you wanted to calculate the change in population from 2000 to 2008. For math operations on numbers, the operators in SQLAlchemy work the same way as they do in Python.
You can use these operators to perform addition (+), subtraction (-), multiplication (*), division (/), and modulus (%) operations. Note: They behave differently when used with non-numeric column types.
Let's now find the top 5 states by population growth between 2000 and 2008.
### INSTRUCTIONS
100XP
Define a select statement called stmt to return:
i) The state column of the census table (census.columns.state).
ii) The difference in population count between 2008 (census.columns.pop2008) and 2000 (census.columns.pop2000) labeled as 'pop_change'.
Group the statement by census.columns.state.
Order the statement by population change ('pop_change') in descending order. Do so by passing it desc('pop_change').
Use the .limit() method on the statement to return only 5 records.
Execute the statement and fetchall the records.
The print statement has already been written for you. Hit 'Submit Answer' to view the results!




## Determining the Overall Percentage of Females
It's possible to combine functions and operators in a single select statement as well. These combinations can be exceptionally handy when we want to calculate percentages or averages, and we can also use the case() expression to operate on data that meets specific criteria while not affecting the query as a whole. The case() expression accepts a list of conditions to match and the column to return if the condition matches, followed by an else_ if none of the conditions match. We can wrap this entire expression in any function or math operation we like.
Often when performing integer division, we want to get a float back. While some databases will do this automatically, you can use the cast() function to convert an expression to a particular type.
### INSTRUCTIONS
100XP

Import case, cast, and Float from sqlalchemy.
Build an expression female_pop2000to calculate female population in 2000. To achieve this:
Use case() inside func.sum().
The first argument of case() is a list containing a tuple of
i) A boolean checking that census.columns.sex is equal to 'F'.
ii) The column census.columns.pop2000.
The second argument is the else_ condition, which should be set to 0.
Calculate the total population in 2000 and use cast() to convert it to Float.
Build a query to calculate the percentage of females in 2000. To do this, divide female_pop2000 by total_pop2000 and multiply by 100.
Execute the query and print percent_female.


## Automatic Joins with an Established Relationship
If you have two tables that already have an established relationship, you can automatically use that relationship by just adding the columns we want from each table to the select statement. Recall that Jason constructed the following query:
stmt = select([census.columns.pop2008, state_fact.columns.abbreviation])


in order to join the census and state_fact tables and select the pop2008 column from the first and the abbreviationcolumn from the second. In this case, the census and state_fact tables had a pre-defined relationship: the statecolumn of the former corresponded to the name column of the latter.
In this exercise, you'll use the same predefined relationship to select the pop2000 and abbreviation columns!
### INSTRUCTIONS
100XP
Build a statement to join the census and state_fact tables and select the pop2000 column from the first and the abbreviation column from the second.
Execute the statement to get the first result and save it as result.
Hit 'Submit Answer' to loop over the keys of the result object, and print the key and value for each!




## Joins
If you aren't selecting columns from both tables or the two tables don't have a defined relationship, you can still use the .join()method on a table to join it with another table and get extra data related to our query. The join() takes the table object you want to join in as the first argument and a condition that indicates how the tables are related to the second argument. Finally, you use the .select_from() method on the select statement to wrap the join clause. For example, in the video, Jason executed the following code to join the census table to the state_facttable such that the state column of the census table corresponded to the name column of the state_fact table.
stmt = stmt.select_from(
    census.join(
        state_fact, census.columns.state == 
        state_fact.columns.name)


### INSTRUCTIONS
100XP
Build a statement to select ALL the columns from the censusand state_fact tables. To select ALL the columns from two tables employees and sales, for example, you would use stmt = select([employees, sales]).
Append a select_from to stmt to join the census table to the state_fact table by the state column in census and the name column in the state_fact table.
Execute the statement to get the first result and save it as result. This code is already written.
Hit 'Submit Answer' to loop over the keys of the result object, and print the key and value for each!
## More Practice with Joins
You can use the same select statement you built in the last exercise, however, let's add a twist and only return a few columns and use the other table in a group_by() clause.
### INSTRUCTIONS
100XP
Build a statement to select:
The state column from the census table.
The sum of the pop2008 column from the census table.
The census_division_name column from the state_facttable.
Append a .select_from() to stmt in order to join the census and state_fact tables by the state and namecolumns.
Group the statement by the name column of the state_facttable.
Execute the statement to get all the records and save it as results.
Hit 'Submit Answer' to loop over the results object and print each record.

## Using alias to handle same table joined queries
Often, you'll have tables that contain hierarchical data, such as employees and managers who are also employees. For this reason, you may wish to join a table to itself on different columns. The .alias() method, which creates a copy of a table, helps accomplish this task. Because it's the same table, you only need a where clause to specify the join condition.
Here, you'll use the .alias() method to build a query to join the employees table against itself to determine to whom everyone reports.

###INSTRUCTIONS
100XP
Save an alias of the employees table as managers. To do so, apply the method .alias() to employees.
Build a query to select the employee name and their manager's name. The manager's name has already been selected for you. Use label to label the name column of employees as 'employee'.
Append a where clause to stmt to match where the idcolumn of the managers table corresponds to the mgrcolumn of the employees table.
Order the statement by the name column of the managerstable.
Execute the statement and store all the results. This code is already written. Hit 'Submit Answer' to print the names of the managers and all their employees.
## Leveraging Functions and Group_bys with Hierarchical Data
It's also common to want to roll up data which is in a hierarchical table. Rolling up data requires making sure you're careful which alias you use to perform the group_bys and which table you use for the function.
Here, your job is to get a count of employees for each manager.

### INSTRUCTIONS
100XP
Save an alias of the employees table as managers.
Build a query to select the name column of the managerstable and the count of the number of their employees. The function func.count() has been imported and will be useful! Use it to count the id column of the employees table.
Using a .where() clause, filter the records where the idcolumn of the managers table and mgr column of the employees table are equal.
Group the query by the name column of the managers table.
Execute the statement and store all the results. Print the names of the managers and their employees. This code has already been written so hit 'Submit Answer' and check out the results!

## Working on Blocks of Records
Fantastic work so far! As Jason discussed in the video, sometimes you may have the need to work on a large ResultProxy, and you may not have the memory to load all the results at once. To work around that issue, you can get blocks of rows from the ResultProxy by using the .fetchmany() method inside a loop. With .fetchmany(), give it an argument of the number of records you want. When you reach an empty list, there are no more rows left to fetch, and you have processed all the results of the query. Then you need to use the .close() method to close out the connection to the database.
You'll now have the chance to practice this on a large ResultProxy called results_proxy that has been pre-loaded for you to work with.

### INSTRUCTIONS
100XP
Use a while loop that checks if there are more_results.
Inside the loop, apply the method .fetchmany() to results_proxy to get 50 records at a time and store those records as partial_results.
After fetching the records, if partial_results is an empty list (that is, if it is equal to []), set more_results to False.
Loop over the partial_results and, if row.state is a key in the state_count dictionary, increment state_count[row.state] by 1; otherwise set state_count[row.state] to 1.
After the while loop, close the ResultProxy results_proxyusing .close().
Hit 'Submit Answer' to print state_count.


