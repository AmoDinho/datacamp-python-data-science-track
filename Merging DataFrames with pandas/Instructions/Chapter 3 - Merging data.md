# Chapter 3 - Merging data

## Merging on a specific column
This exercise follows on the last one with the DataFrames revenue and managers for your company. You expect your company to grow and, eventually, to operate in cities with the same name on different states. As such, you decide that every branch should have a numerical branch identifier. Thus, you add a branch_id column to both DataFrames. Moreover, new cities have been added to both the revenue and managersDataFrames as well. pandas has been imported as pd and both DataFrames are available in your namespace.
At present, there should be a 1-to-1 relationship between the city and branch_id fields. In that case, the result of a merge on the city columns ought to give you the same output as a merge on the branch_id columns. Do they? Can you spot an ambiguity in one of the DataFrames?
### INSTRUCTIONS
100XP
Using pd.merge(), merge the DataFrames revenue and managers on the 'city' column of each. Store the result as merge_by_city.
Print the DataFrame merge_by_city. This has been done for you.
Merge the DataFrames revenue and managers on the 'branch_id' column of each. Store the result as merge_by_id.
Print the DataFrame merge_by_id. This has been done for you, so hit 'Submit Answer' to see the result!

## Merging on columns with non-matching labels
You continue working with the revenue & managersDataFrames from before. This time, someone has changed the field name 'city' to 'branch' in the managers table. Now, when you attempt to merge DataFrames, an exception is thrown:
>>> pd.merge(revenue, managers, on='city')
Traceback (most recent call last):
    ... <text deleted> ...
    pd.merge(revenue, managers, on='city')
    ... <text deleted> ...
KeyError: 'city'


Given this, it will take a bit more work for you to join or merge on the city/branch name. You have to specify the left_on and right_on parameters in the call to pd.merge().
As before, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace. They have been printed in the IPython Shell so you can examine the columns prior to merging.
Are you able to merge better than in the last exercise? How should the rows with Springfield be handled?

### INSTRUCTIONS
100XP
Merge the DataFrames revenue and managers into a single DataFrame called combined using the 'city' and 'branch' columns from the appropriate DataFrames.
In your call to pd.merge(), you will have to specify the parameters left_on and right_on appropriately.
Print the new DataFrame combined.

## Merging on multiple columns
Another strategy to disambiguate cities with identical names is to add information on the states in which the cities are located. To this end, you add a column called state to both DataFrames from the preceding exercises. Again, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace.
Your goal in this exercise is to use pd.merge() to merge DataFrames using multiple columns (using 'branch_id', 'city', and 'state' in this case).
Are you able to match all your company's branches correctly?
### INSTRUCTIONS
100XP
Create a column called 'state' in the DataFrame revenue, consisting of the list ['TX','CO','IL','CA'].
Create a column called 'state' in the DataFrame managers, consisting of the list ['TX','CO','CA','MO'].
Merge the DataFrames revenue and managers using threecolumns :'branch_id', 'city', and 'state'. Pass them in as a list to the on paramater of pd.merge().



return 5 rows with index labels [10, 20, 30, 31, 47]

revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer')



## Choosing a joining strategy
Suppose you have two DataFrames: students (with columns 'StudentID', 'LastName', 'FirstName', and 'Major') and midterm_results (with columns 'StudentID', 'Q1', 'Q2', and 'Q3' for their scores on midterm questions).
You want to combine the DataFrames into a single DataFrame grades, and be able to easily spot which students wrote the midterm and which didn't (their midterm question scores 'Q1', 'Q2', & 'Q3' should be filled with NaN values).
You also want to drop rows from midterm_results in which the StudentID is not found in students.
Which of the following strategies gives the desired result?
A left join: grades = pd.merge(students, midterm_results, how='left').



## Left & right merging on multiple columns
You now have, in addition to the revenue and managersDataFrames from prior exercises, a DataFrame sales that summarizes units sold from specific branches (identified by city and state but not branch_id).
Once again, the managers DataFrame uses the label branch in place of city as in the other two DataFrames. Your task here is to employ left and right merges to preserve data and identify where data is missing.
By merging revenue and sales with a right merge, you can identify the missing revenue values. Here, you don't need to specify left_on or right_on because the columns to merge on have matching labels.
By merging sales and managers with a left merge, you can identify the missing manager. Here, the columns to merge on have conflicting labels, so you must specify left_on and right_on. In both cases, you're looking to figure out how to connect the fields in rows containing Springfield.
pandas has been imported as pd and the three DataFrames revenue, managers, and sales have been pre-loaded. They have been printed for you to explore in the IPython Shell.

### INSTRUCTIONS
100XP
Execute a right merge using pd.merge() with revenue and sales to yield a new DataFrame revenue_and_sales.
Use how='right' and on=['city', 'state'].
Print the new DataFrame revenue_and_sales. This has been done for you.
Execute a left merge with sales and managers to yield a new DataFrame sales_and_managers.
Use how='left', left_on=['city', 'state'], and right_on=['branch', 'state].
Print the new DataFrame sales_and_managers. This has been done for you, so hit 'Submit Answer' to see the result!
## Merging DataFrames with outer join
This exercise picks up where the previous one left off. The DataFrames revenue, managers, and sales are pre-loaded into your namespace (and, of course, pandas is imported as pd). Moreover, the merged DataFrames revenue_and_salesand sales_and_managers have been pre-computed exactly as you did in the previous exercise.
The merged DataFrames contain enough information to construct a DataFrame with 5 rows with all known information correctly aligned and each branch listed only once. You will try to merge the merged DataFrames on all matching keys (which computes an inner join by default). You can compare the result to an outer join and also to an outer join with restricted subset of columns as keys.

### INSTRUCTIONS
100XP
Merge sales_and_managers with revenue_and_sales. Store the result as merge_default.
Print merge_default. This has been done for you.
Merge sales_and_managers with revenue_and_sales using how='outer'. Store the result as merge_outer.
Print merge_outer. This has been done for you.
Merge sales_and_managers with revenue_and_sales only on ['city','state'] using an outer join. Store the result as merge_outer_on and hit 'Submit Answer' to see what the merged DataFrames look like!


## Using merge_ordered()
This exercise uses pre-loaded DataFrames austin and houston that contain weather data from the cities Austin and Houston respectively. They have been printed in the IPython Shell for you to examine.
Weather conditions were recorded on separate days and you need to merge these two DataFrames together such that the dates are ordered. To do this, you'll use pd.merge_ordered(). After you're done, note the order of the rows before and after merging.
### INSTRUCTIONS
100XP
Perform an ordered merge on austin and houston using pd.merge_ordered(). Store the result as tx_weather.
Print tx_weather. You should notice that the rows are sorted by the date but it is not possible to tell which observation came from which city.
Perform another ordered merge on austin and houston.
This time, specify the keyword arguments on='date' and suffixes=['_aus','_hus'] so that the rows can be distinguished. Store the result as tx_weather_suff.
Print tx_weather_suff to examine its contents. This has been done for you.
Perform a third ordered merge on austin and houston.
This time, in addition to the on and suffixes parameters, specify the keyword argument fill_method='ffill' to use forward-filling to replace NaN entries with the most recent non-null entry, and hit 'Submit Answer' to examine the contents of the merged DataFrames!

## Using merge_asof()
Similar to pd.merge_ordered(), the pd.merge_asof()function will also merge values in order using the on column, but for each row in the left DataFrame, only rows from the right DataFrame whose 'on' column values are less than the left value will be kept.
This function can be use to align disparate datetime frequencies without having to first resample.
Here, you'll merge monthly oil prices (US dollars) into a full automobile fuel efficiency dataset. The oil and automobile DataFrames have been pre-loaded as oil and auto. The first 5 rows of each have been printed in the IPython Shell for you to explore.
These datasets will align such that the first price of the year will be broadcast into the rows of the automobiles DataFrame. This is considered correct since by the start of any given year, most automobiles for that year will have already been manufactured.
You'll then inspect the merged DataFrame, resample by year and compute the mean 'Price' and 'mpg'. You should be able to see a trend in these two columns, that you can confirm by computing the Pearson correlation between resampled 'Price' and 'mpg'.

### INSTRUCTIONS
100XP
Merge auto and oil using pd.merge_asof() with left_on='yr' and right_on='Date'. Store the result as merged.
Print the tail of merged. This has been done for you.
Resample merged using 'A' (annual frequency), and on='Date'. Select [['mpg','Price']] and aggregate the mean. Store the result as yearly.
Hit Submit Answer to examine the contents of yearly and yearly.corr(), which shows the Pearson correlation between the resampled 'Price' and 'mpg'.

