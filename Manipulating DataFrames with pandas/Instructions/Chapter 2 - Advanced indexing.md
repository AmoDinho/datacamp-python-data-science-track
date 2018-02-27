# Chapter 2 - Advanced indexing

## Changing index of a DataFrame
100xp
As you saw in the previous exercise, indexes are immutable objects. This means that if you want to change or modify the index in a DataFrame, then you need to change the whole index. You will do this now, using a list comprehension to create the new index.
A list comprehension is a succinct way to generate a list in one line. For example, the following list comprehension generates a list that contains the cubes of all numbers from 0 to 9: cubes = [i**3 for i in range(10)]. This is equivalent to the following code:
cubes = []
for i in range(10):
    cubes.append(i**3)


Before getting started, print the sales DataFrame in the IPython Shell and verify that the index is given by month abbreviations containing lowercase characters.
### Instructions
Create a list new_idx with the same elements as in sales.index, but with all characters capitalized.
Assign new_idx to sales.index.
Print the sales dataframe. This has been done for you, so hit 'Submit Answer' and to see how the index changed.

## Changing index name labels
100xp
Notice that in the previous exercise, the index was not labeled with a name. In this exercise, you will set its name to 'MONTHS'.
Similarly, if all the columns are related in some way, you can provide a label for the set of columns.
To get started, print the sales DataFrame in the IPython Shell and verify that the index has no name, only its data (the month names).
### Instructions
Assign the string 'MONTHS' to sales.index.name to create a name for the index.
Print the sales dataframe to see the index name you just created.
Now assign the string 'PRODUCTS' to sales.columns.name to give a name to the set of columns.
Print the sales dataframe again to see the columns name you just created.

## Building an index, then a DataFrame
100xp
You can also build the DataFrame and index independently, and then put them together. If you take this route, be careful, as any mistakes in generating the DataFrame or the index can cause the data and the index to be aligned incorrectly.
In this exercise, the sales DataFrame has been provided for you without the month index. Your job is to build this index separately and then assign it to the salesDataFrame. Before getting started, print the sales DataFrame in the IPython Shell and note that it's missing the month information.
### Instructions
Generate a list months with the data ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']. This has been done for you.
Assign months to sales.index.
Print the modified sales dataframe and verify that you now have month information in the index.

## Extracting data with a MultiIndex
100xp
In the video, Dhavide explained the concept of a hierarchical index, or a MultiIndex. You will now practice working with these types of indexes.
The sales DataFrame you have been working with has been extended to now include State information as well. In the IPython Shell, print the new sales DataFrame to inspect the data. Take note of the MultiIndex!
Extracting elements from the outermost level of a MultiIndex is just like in the case of a single-level Index. You can use the .loc[] accessor as Dhavide demonstrated in the video.
### Instructions
Print sales.loc[['CA', 'TX']]. Note how New York is excluded.
Print sales['CA':'TX']. Note how New York is included.

## Setting & sorting a MultiIndex
100xp
In the previous exercise, the MultiIndex was created and sorted for you. Now, you're going to do this yourself! With a MultiIndex, you should always ensure the index is sorted. You can skip this only if you know the data is already sorted on the index fields.
To get started, print the pre-loaded sales DataFrame in the IPython Shell to verify that there is no MultiIndex.
### Instructions
Create a MultiIndex by setting the index to be the columns ['state', 'month'].
Sort the MultiIndex using the .sort_index() method.
Print the sales DataFrame. This has been done for you, so hit 'Submit Answer' to verify that indeed you have an index with the fields state and month!

## Using .loc[] with nonunique indexes
100xp
As Dhavide mentioned in the video, it is always preferable to have a meaningful index that uniquely identifies each row. Even though pandas does not require unique index values in DataFrames, it works better if the index values are indeed unique. To see an example of this, you will index your sales data by 'state' in this exercise.
As always, begin by printing the sales DataFrame in the IPython Shell and inspecting it.
### Instructions
Set the index of sales to be the column 'state'.
Print the sales DataFrame to verify that indeed you have an index with state values.
Access the data from 'NY' and print it to verify that you obtain two rows.

## Indexing Multiple levels of an MultiIndex



ract rows from all Symbols for the dates Oct. 3rd through 4th inclusive:
stocks.loc[(slice(None), slice('2016-10-03', '2016-10-04')), :]


Pay particular attention to the tuple (slice(None), slice('2016-10-03', '2016-10-04')).
### Instructions
Look up data for the New York column ('NY') in month 1.
Look up data for the California and Texas columns ('CA', 'TX') in month 2.
Look up data for all states in month 2. Use (slice(None), 2) to extract all rows in month 2.

