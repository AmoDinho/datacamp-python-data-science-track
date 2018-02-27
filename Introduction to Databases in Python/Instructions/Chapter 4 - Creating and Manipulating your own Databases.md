# Chapter 4 - Creating and Manipulating your own Databases
## Creating Tables with SQLAlchemy
Previously, you used the Table object to reflect a table from an existing database, but what if you wanted to create a new table? You'd still use the Table object; however, you'd need to replace the autoload and autoload_with parameters with Column objects.
The Column object takes a name, a SQLAlchemy type with an optional format, and optional keyword arguments for different constraints.
When defining the table, recall how in the video Jason passed in 255 as the maximum length of a String by using Column('name', String(255)). Checking out the slides from the video may help: you can dowload them by clicking on 'Slides' next to the IPython Shell.
After defining the table, you can create the table in the database by using the .create_all() method on metadata and supplying the engine as the only parameter. Go for it!
### INSTRUCTIONS
100XP
Import Table, Column, String, Integer, Float, Boolean from sqlalchemy.
Build a new table called data with columns 'name' (String(255)), 'count' (Integer()), 'amount'(Float()), and 'valid' (Boolean()) columns. The second argument of Table() needs to be metadata, which has already been initialized.
Create the table in the database by passing engine to metadata.create_all().


## Constraints and Data Defaults
You're now going to practice creating a table with some constraints! Often, you'll need to make sure that a column is unique, nullable, a positive value, or related to a column in another table. This is where constraints come in.
As Jason showed you in the video, in addition to constraints, you can also set a default value for the column if no data is passed to it via the default keyword on the column.
### INSTRUCTIONS
100XP
Table, Column, String, Integer, Float, Boolean are already imported from sqlalchemy.
Build a new table called data with a unique name (String), count (Integer) defaulted to 1, amount (Float), and valid (Boolean) defaulted to False.
Hit 'Submit Answer' to create the table in the database and to print the table details for data.


## Inserting a single row with an insert() statement
There are several ways to perform an insert with SQLAlchemy; however, we are going to focus on the one that follows the same pattern as the select statement.
It uses an insert statement where you specify the table as an argument, and supply the data you wish to insert into the value via the .values() method as keyword arguments.
Here, the name of the table is data.
### INSTRUCTIONS
100XP
Import insert and select from the sqlalchemy module.
Build an insert statement for the data table to set name to 'Anna', count to 1, amount to 1000.00, and validto True. Save the statement as stmt.
Execute stmt with the connection and store the results.
Print the rowcount attribute of results to see how many records were inserted.
Build a select statement to query for the record with the nameof Anna.
Hit 'Submit Answer' to print the results of executing the select statement.
## Inserting Multiple Records at Once
It's time to practice inserting multiple records at once!
As Jason showed you in the video, you'll want to first build a list of dictionaries that represents the data you want to insert. Then, in the .execute() method, you can pair this list of dictionaries with an insert statement, which will insert all the records in your list of dictionaries.

### INSTRUCTIONS
100XP
Build a list of dictionaries called values_list with two dictionaries. In the first dictionary set name to 'Anna', count to 1, amount to 1000.00, and valid to True. In the second dictionary of the list, set name to 'Taylor', count to 1, amount to 750.00, and valid to False.
Build an insert statement for the data table for a multiple insert, save it as stmt.
Execute stmt with the values_list via connection and store the results. Make sure values_list is the second argument to .execute().
Print the rowcount of the results.
## Loading a CSV into a Table
You've done a great job so far at inserting data into tables! You're now going to learn how to load the contents of a CSV file into a table.
We have used the csv module to set up a csv_reader, which is just a reader object that can iterate over the lines in a given CSV file - in this case, a census CSV file. Using the enumerate()function, you can loop over the csv_reader to handle the results one at a time. Here, for example, the first line it would return is:
0 ['Illinois', 'M', '0', '89600', '95012']
0 is the idx - or line number - while ['Illinois', 'M', '0', '89600', '95012'] is the row, corresponding to the column names 'state' , 'sex', 'age', 'pop2000 'and 'pop2008'. 'Illinois' can be accessed with row[0], 'M' with row[1], and so on. You can create a dictionary containing this information where the keys are the column names and the values are the entries in each line. Then, by appending this dictionary to a list, you can combine it with an insert statement to load it all into a table!

### INSTRUCTIONS
100XP
Create a statement for bulk insert into the census table. To do this, just use insert() and census.
Create an empty list called values_list and a variable called total_rowcount that is set to 0.
Within the for loop:
Complete the data dictionary by filling in the values for each of the keys. The values are contained in row. row[0]represents the value for 'state', row[1] represents the value for 'sex', and so on.
Append data to values_list.
If 51 cleanly divides into the current idx:
Execute stmt with the values_list and save it as results.
Hit 'Submit Answer' to print total_rowcount when done with all the records.

## Updating individual records
The update statement is very similar to an insert statement, except that it also typically uses a where clause to help us determine what data to update. You'll be using the FIPS state code using here, which is appropriated by the U.S. government to identify U.S. states and certain other associated areas. Recall that you can update all wages in the employees table as follows:
stmt = update(employees).values(wage=100.00)


For your convenience, the names of the tables and columns of interest in this exercise are: state_fact (Table), name(Column), and fips_state (Column).

### INSTRUCTIONS
100XP
Build a statement to select all columns from the state_facttable where the name column is New York. Call it select_stmt.
Print the results of executing the select_stmt and fetching all records.
Build an update statement to change the fips_statecolumn code to 36, save it as stmt.
Use a where clause to filter for states with the name of 'New York' in the state_fact table.
Execute stmt via the connection and save the output as results.
Hit 'Submit Answer' to print the rowcount of the resultsand the results of executing select_stmt. This will verify the fips_state code is now 36.
## Updating Multiple Records
As Jason discussed in the video, by using a where clause that selects more records, you can update multiple records at once. It's time now to practice this!
For your convenience, the names of the tables and columns of interest in this exercise are: state_fact (Table), notes(Column), and census_region_name (Column).
### INSTRUCTIONS
100XP
Build an update statement to update the notes column in the state_fact table to 'The Wild West'. Save it as stmt.
Use a where clause to filter for records that have 'West' in the census_region_name column of the state_fact table.
Execute stmt via the connection and save the output as results.
Hit 'Submit Answer' to print rowcount of the results.

## Correlated Updates
You can also update records with data from a select statement. This is called a correlated update. It works by defining a selectstatement that returns the value you want to update the record with and assigning that as the value in an update statement.
You'll be using a flat_census in this exercise as the target of your correlated update. The flat_census table is a summarized copy of your census table.

### INSTRUCTIONS
100XP
Build a statement to select the name column from state_fact. Save the statement as fips_stmt.
Append a where clause to fips_stmt that matches fips_state from the state_fact table with fips_code in the flat_census table.
Build an update statement to set the state_name in flat_census to fips_stmt. Save the statement as update_stmt.
Hit 'Submit Answer' to execute update_stmt, store the results and print the rowcount of results.


## Deleting all the records from a table
Often, you'll need to empty a table of all of its records so you can reload the data. You can do this with a delete statement with just the table as an argument. For example, in the video, Jason deleted the table extra_employees by executing as follows:
delete_stmt = delete(census)
result_proxy = connection.execute(delete_stmt)


Do be careful, though, as deleting cannot be undone!
## INSTRUCTIONS
100XP
Import delete and select from sqlalchemy.
Build a delete statement to remove all the data from the census table. Save it as stmt.
Execute stmt via the connection and save the results.
Hit 'Submit Answer' to select all remaining rows from the census table and print the result to confirm that the table is now empty!

## Deleting specific records
By using a where() clause, you can target the deletestatement to remove only certain records. For example, Jason deleted all columns from the employees table that had id 3 with the following delete statement:
delete(employees).where(employees.columns.id == 3) 


Here you'll delete ALL rows which have 'M' in the sexcolumn and 36 in the age column. We have included code at the start which computes the total number of these rows. It is important to make sure that this is the number of rows that you actually delete.
### INSTRUCTIONS
100XP
Build a delete statement to remove data from the censustable. Save it as stmt_del.
Append a where clause to stmt_del that contains an and_to filter for rows which have 'M' in the sex column AND 36 in the age column.
Execute the delete statement.
Hit 'Submit Answer' to print the rowcount of the results, as well as to_delete, which returns the number of rows that should be deleted. These should match and this is an important sanity check!

## Deleting a Table Completely
You're now going to practice dropping individual tables from a database with the .drop() method, as well as all tables in a database with the .drop_all() method!
As Spider-Man's Uncle Ben (as well as Jason, in the video!) said: With great power, comes great responsibility. Do be careful when deleting tables, as it's not simple or fast to restore large databases! Remember, you can check to see if a table exists with the .exists() method.
This is the final exercise in this chapter: After this, you'll be ready to apply everything you've learned to a case study in the final chapter of this course!

### INSTRUCTIONS
100XP
Drop the state_fact table by applying the method .drop()to it and passing it the argument engine (in fact, engine will be the sole argument for every function/method in this exercise!)
Check to see if state_fact exists via print. Use the .exists() method with engine as the argument.
Drop all the tables via the metadata using the .drop_all()method.
Use a print statement to check if the census table exists.

