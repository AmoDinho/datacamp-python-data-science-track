# Chapter 4 - Case Study - Summer Olympics


## Loading Olympic edition DataFrame
In this chapter, you'll be using The Guardian's Olympic medal dataset.
Your first task here is to prepare a DataFrame editions from a tab-separated values (TSV) file.
Initially, editions has 26 rows (one for each Olympic edition, i.e., a year in which the Olympics was held) and 7 columns: 'Edition', 'Bronze', 'Gold', 'Silver', 'Grand Total', 'City', and 'Country'.
For the analysis that follows, you won't need the overall medal counts, so you want to keep only the useful columns from editions: 'Edition', 'Grand Total', City, and Country.
### INSTRUCTIONS
100XP
Read file_path into a DataFrame called editions. The identifier file_path has been pre-defined with the filename 'Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv'. You'll have to use the option sep='\t' because the file uses tabs to delimit fields (pd.read_csv() expects commas by default).
Select only the columns 'Edition', 'Grand Total', 'City', and 'Country' from editions.
Print the final DataFrame editions in entirety (there are only 26 rows). This has been done for you, so hit 'Submit Answer' to see the result!


## Loading IOC codes DataFrame
Your task here is to prepare a DataFrame ioc_codes from a comma-separated values (CSV) file.
Initially, ioc_codes has 200 rows (one for each country) and 3 columns: 'Country', 'NOC', & 'ISO code'.
For the analysis that follows, you want to keep only the useful columns from ioc_codes: 'Country' and 'NOC' (the column 'NOC'contains three-letter codes representing each country).
### INSTRUCTIONS
100XP
Read file_path into a DataFrame called ioc_codes. The identifier file_path has been pre-defined with the filename 'Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv'.
Select only the columns 'Country' and 'NOC' from ioc_codes.
Print the leading 5 and trailing 5 rows of the DataFrame ioc_codes(there are 200 rows in total). This has been done for you, so hit 'Submit Answer' to see the result!


## Building medals DataFrame
Here, you'll start with the DataFrame editions from the previous exercise.
You have a sequence of files summer_1896.csv, summer_1900.csv, ..., summer_2008.csv, one for each Olympic edition (year).
You will build up a dictionary medals_dict with the Olympic editions (years) as keys and DataFrames as values.
The dictionary is built up inside a loop over the year of each Olympic edition (from the Index of editions).
Once the dictionary of DataFrames is built up, you will combine the DataFrames using pd.concat().

### INSTRUCTIONS
100XP
Within the for loop:
Create the file path. This has been done for you.
Read file_path into a DataFrame. Assign the result to the yearkey of medals_dict.
Select only the columns 'Athlete', 'NOC', and 'Medal' from medals_dict[year].
Create a new column called 'Edition' in the DataFrame medals_dict[year] whose entries are all year.
Concatenate the dictionary of DataFrames medals_dict into a DataFame called medals. Specify the keyword argument ignore_index=True to prevent repeated integer indices.
Print the first and last 5 rows of medals. This has been done for you, so hit 'Submit Answer' to see the result!

## Counting medals by country/edition in a pivot table
Here, you'll start with the concatenated DataFrame medals from the previous exercise.
You can construct a pivot table to see the number of medals each country won in each year. The result is a new DataFrame with the Olympic edition on the Index and with 138 country NOC codes as columns. If you want a refresher on pivot tables, it may be useful to refer back to the relevant exercises in Manipulating DataFrames with pandas.

### INSTRUCTIONS
0XP
Construct a pivot table from the DataFrame medals, aggregating by count (by specifying the aggfunc parameter). Use 'Edition' as the Index, 'Athlete' for the values, and 'NOC' for the columns.
Print the first & last 5 rows of medal_counts. This has been done for you, so hit 'Submit Answer' to see the results!


## Computing fraction of medals per Olympic edition
In this exercise, you'll start with the DataFrames editions, medals, & medal_counts from prior exercises.
You can extract a Series with the total number of medals awarded in each Olympic edition.
The DataFrame medal_counts can be divided row-wise by the total number of medals awarded each edition; the method .divide()performs the broadcast as you require.
This gives you a normalized indication of each country's performance in each edition.
### INSTRUCTIONS
100XP
Set the index of the DataFrame editions to be 'Edition' (using the method .set_index()). Save the result as totals.
Extract the 'Grand Total' column from totals and assign the result back to totals.
Divide the DataFrame medal_counts by totals along each row. You will have to use the .divide() method with the option axis='rows'. Assign the result to fractions.
Print first & last 5 rows of the DataFrame fractions. This has been done for you, so hit 'Submit Answer' to see the results!
## Computing percentage change in fraction of medals won
Here, you'll start with the DataFrames editions, medals, medal_counts, & fractions from prior exercises.
To see if there is a host country advantage, you first want to see how the fraction of medals won changes from edition to edition.
The expanding mean provides a way to see this down each column. It is the value of the mean with all the data available up to that point in time. If you are interested in learning more about pandas' expanding transformations, this section of the pandas documentation has additional information.
### INSTRUCTIONS
100XP
Create mean_fractions by chaining the methods .expanding().mean() to fractions.
Compute the percentage change in mean_fractions down each column by applying .pct_change() and multiplying by 100. Assign the result to fractions_change.
Reset the index of fractions_change using the .reset_index()method. This will make 'Edition' an ordinary column.
Print the first and last 5 rows of the DataFrame fractions. This has been done for you, so hit 'Submit Answer' to see the results!

## Building hosts DataFrame
Your task here is to prepare a DataFrame hosts by left joining editions and ioc_codes.
Once created, you will subset the Edition and NOC columns and set Edition as the Index.
There are some missing NOC values; you will set those explicitly.
Finally, you'll reset the Index & print the final DataFrame.

### INSTRUCTIONS
0XP
Create the DataFrame hosts by doing a left join on DataFrames editions and ioc_codes (using pd.merge()).
Clean up hosts by subsetting and setting the Index.
Extract the columns 'Edition' and 'NOC'.
Set 'Edition' column as the Index.
Use the .loc[] accessor to find and assign the missing values to the 'NOC' column in hosts. This has been done for you.
Reset the index of hosts using .reset_index(), and then hit 'Submit Answer' to see what hosts looks like!


## Reshaping for analysis
This exercise starts off with fractions_change and hosts already loaded.
Your task here is to reshape the fractions_change DataFrame for later analysis.
Initially, fractions_change is a wide DataFrame of 26 rows (one for each Olympic edition) and 139 columns (one for the edition and 138 for the competing countries).
On reshaping with pd.melt(), as you will see, the result is a tall DataFrame with 3588 rows and 3 columns that summarizes the fractional change in the expanding mean of the percentage of medals won for each country in blocks.

### INSTRUCTIONS
100XP
Create a DataFrame reshaped by reshaping the DataFrame fractions_change with pd.melt().
You'll need to use the keyword argument id_vars='Edition' to set the identifier variable.
You'll also need to use the keyword argument value_name='Change' to set the measured variables.
Print the shape of the DataFrames reshaped and fractions_change. This has been done for you.
Create a DataFrame chn by extracting all the rows from reshaped in which the three letter code for each country ('NOC') is 'CHN'.
Print the last 5 rows of the DataFrame chn using the .tail()method. This has been done for you, so hit 'Submit Answer' to see the results!

## Merging to compute influence
This exercise starts off with the DataFrames reshaped and hosts in the namespace.
Your task is to merge the two DataFrames and tidy the result.
The end result is a DataFrame summarizing the fractional change in the expanding mean of the percentage of medals won for the host country in each Olympic edition.
### INSTRUCTIONS
100XP
Merge reshaped and hosts using an inner join. Remember, how='inner' is the default behavior for pd.merge().
Print the first 5 rows of the DataFrame merged. This has been done for you. You should see that the rows are jumbled chronologically.
Set the index of merged to be 'Edition' and sort the index.
Print the first 5 rows of the DataFrame influence. This has been done for you, so hit 'Submit Answer' to see the results!

## Plotting influence of host country
This final exercise starts off with the DataFrames influence and editions in the namespace. Your job is to plot the influence of being a host country.
### INSTRUCTIONS
100XP
Create a Series called change by extracting the 'Change' column from influence.
Create a bar plot of change using the .plot() method with kind='bar'. Save the result as ax to permit further customization.
Customize the bar plot of change to improve readability:
Apply the method .set_ylabel("% Change of Host Country Medal Count") toax.
Apply the method .set_title("Is there a Host Country Advantage?") to ax.
Apply the method .set_xticklabels(editions['City']) to ax.
Reveal the final plot using plt.show().

