# Chapter 2 - Concatenating data


## Appending pandas Series
In this exercise, you'll load sales data from the months January, February, and March into DataFrames. Then, you'll extract Series with the 'Units' column from each and append them together with method chaining using .append().
To check that the stacking worked, you'll print slices from these Series, and finally, you'll add the result to figure out the total units sold in the first quarter.
### Instructions

Read the files 'sales-jan-2015.csv', 'sales-feb-2015.csv' and 'sales-mar-2015.csv' into the DataFrames jan, feb, and marrespectively.
Use parse_dates=True and index_col='Date'.
Extract the 'Units' column of jan, feb, and mar to create the Series jan_units, feb_units, and mar_units respectively.
Construct the Series quarter1 by appending feb_units to jan_units and then appending mar_units to the result. Use chained calls to the .append() method to do this.
Verify that quarter1 has the individual Series stacked vertically. To do this:
Print the slice containing rows from jan 27, 2015 to feb 2, 2015.
Print the slice containing rows from feb 26, 2015 to mar 7, 2015.
Compute and print the total number of units sold from the Series quarter1. This has been done for you, so hit 'Submit Answer' to see the result!


## Concatenating pandas Series along row axis
Having learned how to append Series, you'll now learn how to achieve the same result by concatenating Series instead. You'll continue to work with the sales data you've seen previously. This time, the DataFrames jan, feb, and mar have been pre-loaded.
Your job is to use pd.concat() with a list of Series to achieve the same result that you would get by chaining calls to .append().
You may be wondering about the difference between pd.concat() and pandas' .append() method. One way to think of the difference is that .append() is a specific case of a concatenation, while pd.concat() gives you more flexibility, as you'll see in later exercises.
### INSTRUCTIONS
100XP
Create an empty list called units. This has been done for you.
Use a for loop to iterate over [jan, feb, mar]:
In each iteration of the loop, append the 'Units' column of each DataFrame to units.
Concatenate the Series contained in the list units into a longer Series called quarter1 using pd.concat().
Specify the keyword argument axis='rows' to stack the Series vertically.
Verify that quarter1 has the individual Series stacked vertically by printing slices. This has been done for you, so hit 'Submit Answer' to see the result!

## Appending DataFrames with ignore_index
In this exercise, you'll use the Baby Names Dataset (from data.gov) again. This time, both DataFrames names_1981 and names_1881 are loaded without specifying an Index column (so the default Indexes for both are RangeIndexes).
You'll use the DataFrame .append() method to make a DataFrame combined_names. To distinguish rows from the original two DataFrames, you'll add a 'year' column to each with the year (1881 or 1981 in this case). In addition, you'll specify ignore_index=True so that the index values are not used along the concatenation axis. The resulting axis will instead be labeled 0, 1, ..., n-1, which is useful if you are concatenating objects where the concatenation axis does not have meaningful indexing information.
INSTRUCTIONS
100XP
### INSTRUCTIONS
100XP
Create a 'year' column in the DataFrames names_1881 and names_1981, with values of 1881 and 1981 respectively. Recall that assigning a scalar value to a DataFrame column broadcasts that value throughout.
Create a new DataFrame called combined_names by appending the rows of names_1981 underneath the rows of names_1881. Specify the keyword argument ignore_index=True to make a new RangeIndex of unique integers for each row.
Print the shapes of all three DataFrames. This has been done for you.
Extract all rows from combined_names that have the name 'Morgan'. To do this, use the .loc[] accessor with an appropriate filter. The relevant column of combined_nameshere is 'name'.


## Concatenating pandas DataFrames along column axis
The function pd.concat() can concatenate DataFrames horizontally as well as vertically (vertical is the default). To make the DataFrames stack horizontally, you have to specify the keyword argument axis=1 or axis='columns'.
In this exercise, you'll use weather data with maximum and mean daily temperatures sampled at different rates (quarterly versus monthly). You'll concatenate the rows of both and see that, where rows are missing in the coarser DataFrame, null values are inserted in the concatenated DataFrame. This corresponds to an outer join (which you will explore in more detail in later exercises).
The files 'quarterly_max_temp.csv' and 'monthly_mean_temp.csv' have been pre-loaded into the DataFrames weather_max and weather_mean respectively, and pandas has been imported as pd.
### INSTRUCTIONS
100XP
Create a new DataFrame called weather by concatenating the DataFrames weather_max and weather_mean horizontally.
Pass the DataFrames to pd.concat() as a list and specify the keyword argument axis=1 to stack them horizontally.
Print the new DataFrame weather.

## Reading multiple files to build a DataFrame
It is often convenient to build a large DataFrame by parsing many files as DataFrames and concatenating them all at once. You'll do this here with three files, but, in principle, this approach can be used to combine data from dozens or hundreds of files.
Here, you'll work with DataFrames compiled from The Guardian's Olympic medal dataset.
pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.

### INSTRUCTIONS
100XP
Iterate over medal_types in the for loop.
Inside the for loop:
Create file_name using string interpolation with the loop variable medal. This has been done for you. The expression "%s_top5.csv" % medal evaluates as a string with the valueof medal replacing %s in the format string.
Create the list of column names called columns. This has been done for you.
Read file_name into a DataFrame called medal_df. Specify the keyword arguments header=0, index_col='Country', and names=columns to get the correct row and column Indexes.
Append medal_df to medals using the list .append()method.
Concatenate the list of DataFrames medals horizontally (using axis='columns') to create a single DataFrame called medals. Print it in its entirety.

## Concatenating vertically to get MultiIndexed rows
When stacking a sequence of DataFrames vertically, it is sometimes desirable to construct a MultiIndex to indicate the DataFrame from which each row originated. This can be done by specifying the keys parameter in the call to pd.concat(), which generates a hierarchical index with the labels from keysas the outermost index label. So you don't have to rename the columns of each DataFrame as you load it. Instead, only the Index column needs to be specified.
Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset. Once again, pandashas been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.

### INSTRUCTIONS
100XP
Within the for loop:
Read file_name into a DataFrame called medal_df. Specify the index to be 'Country'.
Append medal_df to medals.
Concatenate the list of DataFrames medals into a single DataFrame called medals. Be sure to use the keyword argument keys=['bronze', 'silver', 'gold'] to create a vertically stacked DataFrame with a MultiIndex.
Print the new DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!

## Slicing MultiIndexed DataFrames
This exercise picks up where the last ended (again using The Guardian's Olympic medal dataset).
You are provided with the MultiIndexed DataFrame as produced at the end of the preceding exercise. Your task is to sort the DataFrame and to use the pd.IndexSlice to extract specific slices. Check out this exercise from Manipulating DataFrames with pandas to refresh your memory on how to deal with MultiIndexed DataFrames.
pandas has been imported for you as pd and the DataFrame medals is already in your namespace.
### INSTRUCTIONS
100XP
Create a new DataFrame medals_sorted with the entries of medals sorted. Use .sort_index(level=0) to ensure the Index is sorted suitably.
Print the number of bronze medals won by Germany and all of the silver medal data. This has been done for you.
Create an alias for pd.IndexSlice called idx. A slicer pd.IndexSlice is required when slicing on the inner level of a MultiIndex.
Slice all the data on medals won by the United Kingdom. To do this, use the .loc[] accessor with idx[:,'United Kingdom'], :.


## Concatenating horizontally to get MultiIndexed columns
It is also possible to construct a DataFrame with hierarchically indexed columns. For this exercise, you'll start with pandas imported and a list of three DataFrames called dataframes. All three DataFrames contain 'Company', 'Product', and 'Units' columns with a 'Date' column as the index pertaining to sales transactions during the month of February, 2015. The first DataFrame describes Hardware transactions, the second describes Software transactions, and the third, Service transactions.
Your task is to concatenate the DataFrames horizontally and to create a MultiIndex on the columns. From there, you can summarize the resulting DataFrame and slice some information from it.
### INSTRUCTIONS
100XP

Construct a new DataFrame february with MultiIndexed columns by concatenating the list dataframes.
Use axis=1 to stack the DataFrames horizontally and the keyword argument keys=['Hardware', 'Software', 'Service'] to construct a hierarchical Index from each DataFrame.
Print summary information from the new DataFrame february using the .info() method. This has been done for you.
Create an alias called idx for pd.IndexSlice.
Extract a slice called slice_2_8 from february (using .loc[] & idx) that comprises rows between Feb. 2, 2015 to Feb. 8, 2015 from columns under 'Company'.
Print the slice_2_8. This has been done for you, so hit 'Submit Answer' to see the sliced data!

## Concatenating DataFrames from a dict
You're now going to revisit the sales data you worked with earlier in the chapter. Three DataFrames jan, feb, and mar have been pre-loaded for you. Your task is to aggregate the sum of all sales over the 'Company' column into a single DataFrame. You'll do this by constructing a dictionary of these DataFrames and then concatenating them.
### INSTRUCTIONS
100XP
Create a list called month_list consisting of the tuples ('january', jan), ('february', feb), and ('march', mar).
Create an empty dictionary called month_dict.
Inside the for loop:
Group month_data by 'Company' and use .sum() to aggregate.
Construct a new DataFrame called sales by concatenating the DataFrames stored in month_dict.
Create an alias for pd.IndexSlice and print all sales by 'Mediacore'. This has been done for you, so hit 'Submit Answer' to see the result!

## Concatenating DataFrames with inner join
Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset.
The DataFrames bronze, silver, and gold have been pre-loaded for you.
Your task is to compute an inner join.

### INSTRUCTIONS
100XP
Construct a list of DataFrames called medal_list with entries bronze, silver, and gold.
Concatenate medal_list horizontally with an inner join to create medals.
Use the keyword argument keys=['bronze', 'silver', 'gold'] to yield suitable hierarchical indexing.
Use axis=1 to get horizontal concatenation.
Use join='inner' to keep only rows that share common index labels.
Print the new DataFrame medals.

## Resampling & concatenating DataFrames with inner join
In this exercise, you'll compare the historical 10-year GDP (Gross Domestic Product) growth in the US and in China. The data for the US starts in 1947 and is recorded quarterly; by contrast, the data for China starts in 1966 and is recorded annually.
You'll need to use a combination of resampling and an inner join to align the index labels. You'll need an appropriate offset aliasfor resampling, and the method .resample() must be chained with some kind of aggregation method (.pct_change() and .last() in this case).
pandas has been imported as pd, and the DataFrames china and us have been pre-loaded, with the output of china.head() and us.head() printed in the IPython Shell.

### INSTRUCTIONS
100XP
Make a new DataFrame china_annual by resampling the DataFrame china with .resample('A') (i.e., with annualfrequency) and chaining two method calls:
Chain .pct_change(10) as an aggregation method to compute the percentage change with an offset of ten years.
Chain .dropna() to eliminate rows containing null values.
Make a new DataFrame us_annual by resampling the DataFrame us exactly as you resampled china.
Concatenate china_annual and us_annual to construct a DataFrame called gdp. Use join='inner' to perform an inner join and use axis=1 to concatenate horizontally.
Print the result of resampling gdp every decade (i.e., using .resample('10A')) and aggregating with the method .last(). This has been done for you, so hit 'Submit Answer' to see the result!

