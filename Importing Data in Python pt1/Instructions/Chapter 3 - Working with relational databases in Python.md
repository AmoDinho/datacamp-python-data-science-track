# Chapter 3 - Working with relational databases in Python

## Creating a database engine
100xp
Here, you're going to fire up your very first SQL engine. You'll create an engine to connect to the SQLite database 'Chinook.sqlite', which is in your working directory. Remember that to create an engine to connect to 'Northwind.sqlite', Hugo executed the command
engine = create_engine('sqlite:///Northwind.sqlite')


Here, 'sqlite:///Northwind.sqlite' is called the connection string to the SQLite database Northwind.sqlite. A little bit of background on the Chinook database: the Chinook database contains information about a semi-fictional digital media store in which media data is real and customer, employee and sales data has been manually created.
Why the name Chinook, you ask? According to their website,
The name of this sample database was based on the Northwind database. Chinooks are winds in the interior West of North America, where the Canadian Prairies and Great Plains meet various mountain ranges. Chinooks are most prevalent over southern Alberta in Canada. Chinook is a good name choice for a database that intends to be an alternative to Northwind.
### Instructions
Import the function create_engine from the module sqlalchemy.
Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to engine.
Take Hint (-30xp)

## What are the tables in the database?
100xp
In this exercise, you'll once again create an engine to connect to 'Chinook.sqlite'. Before you can get any data out of the database, however, you'll need to know what tables it contains!
To this end, you'll save the table names to a list using the method table_names() on the engine and then you will print the list.
### Instructions
Import the function create_engine from the module sqlalchemy.
Create an engine to connect to the SQLite database 'Chinook.sqlite'and assign it to engine.
Using the method table_names() on the engine engine, assign the table names of 'Chinook.sqlite' to the variable table_names.
Print the object table_names to the shell.

## The Hello World of SQL Queries!
0xp
Now, it's time for liftoff! In this exercise, you'll perform the Hello World of SQL queries, SELECT, in order to retrieve all columns of the table Album in the Chinook database. Recall that the query SELECT * selects all columns.
### Instructions
Open the engine connection as con using the method connect() on the engine.
Execute the query that selects ALL columns from the Album table. Store the results in rs.
Store all of your query results in the DataFrame df by applying the fetchall() method to the results rs.
Close the connection!


## Customizing the Hello World of SQL Queries
100xp
Congratulations on executing your first SQL query! Now you're going to figure out how to customize your query in order to:
Select specified columns from a table;
Select a specified number of rows;
Import column names from the database table.
Recall that Hugo performed a very similar query customization in the video:
engine = create_engine('sqlite:///Northwind.sqlite')

with engine.connect() as con:
    rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()


Packages have already been imported as follows:
from sqlalchemy import create_engine
import pandas as pd


The engine has also already been created:
engine = create_engine('sqlite:///Chinook.sqlite')


The engine connection is already open with the statement
with engine.connect() as con:


All the code you need to complete is within this context.
### Instructions
Execute the SQL query that selects the columns LastName and Title from the Employee table. Store the results in the variable rs.
Apply the method fetchmany() to rs in order to retrieve 3 of the records. Store them in the DataFrame df.
Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.
## Filtering your database records using SQL's WHERE
100xp
You can now execute a basic SQL query to select records from any table in your database and you can also perform simple query customizations to select particular columns and numbers of rows.
There are a couple more standard SQL query chops that will aid you in your journey to becoming an SQL ninja.
Let's say, for example that you wanted to get all records from the Customer table of the Chinook database for which the Country is 'Canada'. You can do this very easily in SQL using a SELECT statement followed by a WHERE clause as follows:
SELECT * FROM Customer WHERE Country = 'Canada'


In fact, you can filter any SELECT statement by any condition using a WHEREclause. This is called filtering your records.
In this interactive exercise, you'll select all records of the Employee table for which 'EmployeeId' is greater than or equal to 6.
Packages are already imported as follows:
import pandas as pd
from sqlalchemy import create_engine


Query away!
### Instructions
Complete the argument of create_engine() so that the engine for the SQLite database 'Chinook.sqlite' is created.
Execute the query that selects all records from the Employee table where 'EmployeeId' is greater than or equal to 6. Use the >=operator and assign the results to rs.
Apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.
## Ordering your SQL records with ORDER BY
100xp
You can also order your SQL query results. For example, if you wanted to get all records from the Customer table of the Chinook database and order them in increasing order by the column SupportRepId, you could do so with the following query:
"SELECT * FROM Customer ORDER BY SupportRepId"


In fact, you can order any SELECT statement by any column.
In this interactive exercise, you'll select all records of the Employee table and order them in increasing order by the column BirthDate.
Packages are already imported as follows:
import pandas as pd
from sqlalchemy import create_engine


Get querying!
### Instructions
Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
In the context manager, execute the query that selects all records from the Employee table and orders them in increasing order by the column BirthDate. Assign the result to rs.
In a call to pd.DataFrame(), apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
Set the DataFrame's column names to the corresponding names of the table columns.
## Pandas for more complex querying
100xp
Here, you'll become more familiar with the pandas function read_sql_query() by using it to execute a more complex query: a SELECT statement followed by both a WHERE clause AND an ORDER BY clause.
You'll build a DataFrame that contains the rows of the Employee table for which the EmployeeId is greater than or equal to 6 and you'll order these entries by BirthDate.
### Instructions
Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from the Employee table where the EmployeeId is greater than or equal to 6 and ordered by BirthDate (make sure to use WHERE and ORDER BY in this precise order).
## The power of SQL lies in relationships between tables: INNER JOIN
100xp
Here, you'll perform your first INNER JOIN! You'll be working with your favourite SQLite database, Chinook.sqlite. For each record in the Album table, you'll extract the Title along with the Name of the Artist. The latter will come from the Artist table and so you will need to INNER JOIN these two tables on the ArtistID column of both.
Recall that to INNER JOIN the Orders and Customers tables from the Northwind database, Hugo executed the following SQL query:
"SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID"


The following code has already been executed to import the necessary packages and to create the engine:
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')


### Instructions
Assign to rs the results from the following query: select all the records, extracting the Title of the record and Name of the artist of each record from the Album table and the Artist table, respectively. To do so, INNER JOIN these two tables on the ArtistID column of both.
In a call to pd.DataFrame(), apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
Set the DataFrame's column names to the corresponding names of the table columns.
## Filtering your INNER JOIN
100xp
Congrats on performing your first INNER JOIN! You're now going to finish this chapter with one final exercise in which you perform an INNER JOIN and filter the result using a WHERE clause.
Recall that to INNER JOIN the Orders and Customers tables from the Northwind database, Hugo executed the following SQL query:
"SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID"


The following code has already been executed to import the neccesary packages and to create the engine:
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')


### Instructions
Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select allrecords from PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId that satisfy the condition Milliseconds < 250000.

