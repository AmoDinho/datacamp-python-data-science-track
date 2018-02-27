# Chapter 1 - Preparing data

## Reading DataFrames from multiple files in a loop
100xp
As you saw in the video, loading data from multiple files into DataFrames is more efficient in a loop or a list comprehension.
Notice that this approach is not restricted to working with CSV files. That is, even if your data comes in other formats, as long as pandas has a suitable data import function, you can apply a loop or comprehension to generate a list of DataFrames imported from the source files.
Here, you'll continue working with The Guardian's Olympic medal dataset.
### Instructions
Create a list of file names called filenames with three strings 'Gold.csv', 'Silver.csv', & 'Bronze.csv'. This has been done for you.
Use a for loop to create another list called dataframescontaining the three DataFrames loaded from filenames:
Iterate over filenames.
Read each CSV file in filenames into a DataFrame and append it to dataframes by using pd.read_csv()inside a call to .append().
Print the first 5 rows of the first DataFrame of the list dataframes. This has been done for you, so hit 'Submit Answer' to see the results.

## Combining DataFrames from multiple data files
100xp
In this exercise, you'll combine the three DataFrames from earlier exercises - gold, silver, & bronze - into a single DataFrame called medals. The approach you'll use here is clumsy. Later on in the course, you'll see various powerful methods that are frequently used in practice for concatenating or merging DataFrames.
Remember, the column labels of each DataFrame are NOC, Country, and Total, where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won.
### Instructions
Construct a copy of the DataFrame gold called medalsusing the .copy() method.
Create a list called new_labels with entries 'NOC', 'Country', & 'Gold'. This is the same as the column labels from gold with the column label 'Total' replaced by 'Gold'.
Rename the columns of medals by assigning new_labelsto medals.columns.
Create new columns 'Silver' and 'Bronze' in medalsusing silver['Total'] & bronze['Total'].
Print the top 5 rows of the final DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!


## Sorting DataFrame with the Index & columns
0xp
It is often useful to rearrange the sequence of the rows of a DataFrame by sorting. You don't have to implement these yourself; the principal methods for doing this are .sort_index() and .sort_values().
In this exercise, you'll use these methods with a DataFrame of temperature values indexed by month names. You'll sort the rows alphabetically using the Index and numerically using a column. Notice, for this data, the original ordering is probably most useful and intuitive: the purpose here is for you to understand what the sorting methods do.
### Instructions
Read 'monthly_max_temp.csv' into a DataFrame called weather1with 'Month' as the index.
Sort the index of weather1 in alphabetical order using the .sort_index() method and store the result in weather2.
Sort the index of weather1 in reverse alphabetical order by specifying the additional keyword argument ascending=False inside .sort_index().
Use the .sort_values() method to sort weather1 in increasing numerical order according to the values of the column 'Max TemperatureF'.

## Reindexing DataFrame from a list
100xp
Sorting methods are not the only way to change DataFrame Indexes. There is also the .reindex() method.
In this exercise, you'll reindex a DataFrame of quarterly-sampled mean temperature values to contain monthly samples (this is an example of upsampling or increasing the rate of samples, which you may recall from the pandas Foundations course).
The original data has the first month's abbreviation of the quarter (three-month interval) on the Index, namely Apr, Jan, Jul, and Sep. This data has been loaded into a DataFrame called weather1 and has been printed in its entirety in the IPython Shell. Notice it has only four rows (corresponding to the first month of each quarter) and that the rows are not sorted chronologically.
You'll initially use a list of all twelve month abbreviations and subsequently apply the .ffill() method to forward-fill the null entries when upsampling. This list of month abbreviations has been pre-loaded as year.
### Instructions
Reorder the rows of weather1 using the .reindex() method with the list year as the argument, which contains the abbreviations for each month.
Reorder the rows of weather1 just as you did above, this time chaining the .ffill() method to replace the null values with the last preceding non-null value.

## Reindexing using another DataFrame Index
100xp
Another common technique is to reindex a DataFrame using the Index of another DataFrame. The DataFrame .reindex() method can accept the Index of a DataFrame or Series as input. You can access the Index of a DataFrame with its .index attribute.
The Baby Names Dataset from data.gov summarizes counts of names (with genders) from births registered in the US since 1881. In this exercise, you will start with two baby-names DataFrames names_1981 and names_1881 loaded for you.
The DataFrames names_1981 and names_1881 both have a MultiIndex with levels name and gender giving unique labels to counts in each row. If you're interested in seeing how the MultiIndexes were set up, names_1981 and names_1881 were read in using the following commands:
names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'], index_col=(0,1))
names_1881 = pd.read_csv('names1881.csv', header=None, names=['name','gender','count'], index_col=(0,1))


As you can see by looking at their shapes, which have been printed in the IPython Shell, the DataFrame corresponding to 1981 births is much larger, reflecting the greater diversity of names in 1981 as compared to 1881.
Your job here is to use the DataFrame .reindex() and .dropna() methods to make a DataFrame common_names counting names from 1881 that were still popular in 1981.
### Instructions
Create a new DataFrame common_names by reindexing names_1981using the Index of the DataFrame names_1881 of older names.
Print the shape of the new common_names DataFrame. This has been done for you. It should be the same as that of names_1881.
Drop the rows of common_names that have null counts using the .dropna() method. These rows correspond to names that fell out of fashion between 1881 & 1981.
Print the shape of the reassigned common_names DataFrame. This has been done for you, so hit 'Submit Answer' to see the result!

## Broadcasting in arithmetic formulas
100xp
In this exercise, you'll work with weather data pulled from wunderground.com. The DataFrame weather has been pre-loaded along with pandas as pd. It has 365 rows (observed each day of the year 2013 in Pittsburgh, PA) and 22 columns reflecting different weather measurements each day.
You'll subset a collection of columns related to temperature measurements in degrees Fahrenheit, convert them to degrees Celsius, and relabel the columns of the new DataFrame to reflect the change of units.
Remember, ordinary arithmetic operators (like +, -, *, and /) broadcastscalar values to conforming DataFrames when combining scalars & DataFrames in arithmetic expressions. Broadcasting also works with pandas Series and NumPy arrays.
### Instructions
Create a new DataFrame temps_f by extracting the columns 'Min TemperatureF', 'Mean TemperatureF', & 'Max TemperatureF' from weather as a new DataFrame temps_f. To do this, pass the relevant columns as a list to weather[].
Create a new DataFrame temps_c from temps_f using the formula (temps_f - 32) * 5/9.
Rename the columns of temps_c to replace 'F' with 'C' using the .str.replace('F', 'C') method on temps_c.columns.
Print the first 5 rows of DataFrame temps_c. This has been done for you, so hit 'Submit Answer' to see the result!


## Computing percentage growth of GDP
100xp
Your job in this exercise is to compute the yearly percent-change of US GDP (Gross Domestic Product) since 2008.
The data has been obtained from the Federal Reserve Bank of St. Louis and is available in the file GDP.csv, which contains quarterly data; you will resample it to annual sampling and then compute the annual growth of GDP. For a refresher on resampling, check out the relevant material from pandas Foundations.
### Instructions
Read the file 'GDP.csv' into a DataFrame called gdp.
Use parse_dates=True and index_col='DATE'.
Create a DataFrame post2008 by slicing gdp such that it comprises all rows from 2008 onward.
Print the last 8 rows of the slice post2008. This has been done for you. This data has quarterly frequency so the indices are separated by three-month intervals.
Create the DataFrame yearly by resampling the slice post2008 by year. Remember, you need to chain .resample() (using the alias 'A' for annual frequency) with some kind of aggregation; you will use the aggregation method .last() to select the last element when resampling.
Compute the percentage growth of the resampled DataFrame yearlywith .pct_change() * 100.
## Converting currency of stocks
In this exercise, stock prices in US Dollars for the S&P 500 in 2015 have been obtained from Yahoo Finance. The files sp500.csv for sp500 and exchange.csv for the exchange rates are both provided to you.
Using the daily exchange rate to Pounds Sterling, your task is to convert both the Open and Close column prices.

### Instructions 
Read the DataFrames sp500 & exchange from the files 'sp500.csv' & 'exchange.csv' respectively..
Use parse_dates=True and index_col='Date'.
Extract the columns 'Open' & 'Close' from the DataFrame sp500as a new DataFrame dollars and print the first 5 rows.
Construct a new DataFrame pounds by converting US dollars to British pounds. You'll use the .multiply() method of dollars with exchange['GBP/USD'] and axis='rows'
Print the first 5 rows of the new DataFrame pounds. This has been done for you, so hit 'Submit Answer' to see the results!.

