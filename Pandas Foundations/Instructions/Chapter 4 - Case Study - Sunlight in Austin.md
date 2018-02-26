# Chapter 4 - Case Study - Sunlight in Austin

## Reading in a data file
100xp
Now that you have identified the method to use to read the data, let's try to read one file. The problem with real data such as this is that the files are almost never formatted in a convenient way. In this exercise, there are several problems to overcome in reading the file. First, there is no header, and thus the columns don't have labels. There is also no obvious index column, since none of the data columns contain a full date or time.
Your job is to read the file into a DataFrame using the default arguments. After inspecting it, you will re-read the file specifying that there are no headers supplied.
The CSV file has been provided for you as 'data.csv'.
### Instructions
Import pandas as pd.
Read the file 'data.csv' into a DataFrame called df.
Print the output of df.head(). This has been done for you. Notice the formatting problems in df.
Re-read the data using specifying the keyword argument header=Noneand assign it to df_headers.
Print the output of df_headers.head(). This has already been done for you. Hit 'Submit Answer' and see how this resolves the formatting issues.

## Re-assigning column names
100xp
After the initial step of reading in the data, the next step is to clean and tidy it so that it is easier to work with.
In this exercise, you will begin this cleaning process by re-assigning column names and dropping unnecessary columns.
pandas has been imported in the workspace as pd, and the file NOAA_QCLCD_2011_hourly_13904.txt has been parsed and loaded into a DataFrame df. The comma separated string of column names, column_labels, and list of columns to drop, list_to_drop, have also been loaded for you.
### Instructions
Convert the comma separated string column_labels to a list of strings using .split(','). Assign the result to column_labels_list.
Reassign df.columns using the list of strings column_labels_list.
Call df.drop() with list_to_drop and axis='columns'. Assign the result to df_dropped.
Print df_dropped.head() to examine the result. This has already been done for you.

## Cleaning and tidying datetime data
0xp
In order to use the full power of pandas time series, you must construct a DatetimeIndex. To do so, it is necessary to clean and transform the date and time columns.
The DataFrame df_dropped you created in the last exercise is provided for you and pandas has been imported as pd.
Your job is to clean up the date and Time columns and combine them into a datetime collection to be used as the Index.
### Instructions
Convert the 'date' column to a string with .astype(str) and assign to df_dropped['date'].
Add leading zeros to the 'Time' column. This has been done for you.
Concatenate the new 'date' and 'Time' columns together. Assign to date_string.
Convert the date_string Series to datetime values with pd.to_datetime(). Specify the format parameter.
Set the index of the df_dropped DataFrame to to be date_times. Assign the result to df_clean.

## Cleaning the numeric columns
100xp
The numeric columns contain missing values labeled as 'M'. In this exercise, your job is to transform these columns such that they contain only numeric values and interpret missing data as NaN.
The pandas function pd.to_numeric() is ideal for this purpose: It converts a Series of values to floating-point values. Furthermore, by specifying the keyword argument errors='coerce', you can force strings like 'M' to be interpreted as NaN.
A DataFrame df_clean is provided for you at the start of the exercise, and as usual, pandas has been imported as pd.
### Instructions
Print the 'dry_bulb_faren' temperature between 8 AM and 9 AM on June 20, 2011.
Convert the 'dry_bulb_faren' column to numeric values with pd.to_numeric(). Specify errors='coerce'.
Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011.
Convert the 'wind_speed' and 'dew_point_faren' columns to numeric values with pd.to_numeric(). Again, specify errors='coerce'.

## Signal min, max, median
100xp
Now that you have the data read and cleaned, you can begin with statistical EDA. First, you will analyze the 2011 Austin weather data.
Your job in this exercise is to analyze the 'dry_bulb_faren' column and print the median temperatures for specific time ranges. You can do this using partial datetime stringselection.
The cleaned dataframe is provided in the workspace as df_clean.
### Instructions
Select the 'dry_bulb_faren' column and print the output of .median().
Use .loc[] to select the range '2011-Apr':'2011-Jun' from dry_bulb_faren' and print the output of .median().
Use .loc[] to select the month '2011-Jan' from 'dry_bulb_faren' and print the output of .median().


## Signal variance
0xp
You're now ready to compare the 2011 weather data with the 30-year normals reported in 2010. You can ask questions such as, on average, how much hotter was every day in 2011 than expected from the 30-year average?
The DataFrames df_clean and df_climate from previous exercises are available in the workspace.
Your job is to first resample df_clean and df_climate by day and aggregate the mean temperatures. You will then extract the temperature related columns from each - 'dry_bulb_faren' in df_clean, and 'Temperature' in df_climate - as NumPy arrays and compute the difference.
Notice that the indexes of df_clean and df_climate are not aligned - df_clean has dates in 2011, while df_climate has dates in 2010. This is why you extract the temperature columns as NumPy arrays. An alternative approach is to use the pandas .reset_index() method to make sure the Series align properly. You will practice this approach as well.
### Instructions
Downsample df_clean with daily frequency and aggregate by the mean. Store the result as daily_mean_2011.
Extract the 'dry_bulb_faren' column from daily_mean_2011 as a NumPy array using .values. Store the result as daily_temp_2011. Note: .values is an attribute, not a method, so you don't have to use ().
Downsample df_climate with daily frequency and aggregate by the mean. Store the result as daily_climate.
Extract the 'Temperature' column from daily_climate using the .reset_index() method. To do this, first reset the index of daily_climate, and then use bracket slicing to access 'Temperature'. Store the result as daily_temp_climate.


## Sunny or cloudy
100xp
On average, how much hotter is it when the sun is shining? In this exercise, you will compare temperatures on sunny days against temperatures on overcast days.
Your job is to use Boolean selection to filter out sunny and overcast days, and then compute the difference of the mean daily maximum temperatures between each type of day.
The DataFrame df_clean from previous exercises has been provided for you. The column 'sky_condition' provides information about whether the day was sunny ('CLR') or overcast ('OVC').
### Instructions
Use .loc[] to select sunny days and assign to sunny. If 'sky_condition' equals 'CLR', then the day is sunny.
Use .loc[] to select overcast days and assign to overcast. If 'sky_condition' contains 'OVC', then the day is overcast.
Resample sunny and overcast and aggregate by the maximum (.max()) daily ('D') temperature. Assign to sunny_daily_maxand overcast_daily_max.
Print the difference between the mean of sunny_daily_max and overcast_daily_max. This has already been done for you, so click 'Submit Answer' to view the result!
## Weekly average temperature and visibility
100xp
Is there a correlation between temperature and visibility? Let's find out.
In this exercise, your job is to plot the weekly average temperature and visibility as subplots. To do this, you need to first select the appropriate columns and then resample by week, aggregating the mean.
In addition to creating the subplots, you will compute the Pearson correlation coefficient using .corr(). The Pearson correlation coefficient, known also as Pearson's r, ranges from -1 (indicating total negative linear correlation) to 1 (indicating total positive linear correlation). A value close to 1 here would indicate that there is a strong correlation between temperature and visibility.
The DataFrame df_clean has been pre-loaded for you.
### Instructions
Import matplotlib.pyplot as plt.
Select the 'visibility' and 'dry_bulb_faren' columns and resample them by week, aggregating the mean. Assign the result to weekly_mean.
Print the output of weekly_mean.corr().
Plot the weekly_mean dataframe with .plot(), specifying subplots=True.

## Daily hours of clear sky
100xp
In a previous exercise, you analyzed the 'sky_condition' column to explore the difference in temperature on sunny days compared to overcast days. Recall that a 'sky_condition' of 'CLR' represents a sunny day. In this exercise, you will explore sunny days in greater detail. Specifically, you will use a box plot to visualize the fraction of days that are sunny.
The 'sky_condition' column is recorded hourly. Your job is to resample this column appropriately such that you can extract the number of sunny hours in a day and the number of total hours. Then, you can divide the number of sunny hours by the number of total hours, and generate a box plot of the resulting fraction.
As before, df_clean is available for you in the workspace.
### Instructions
Create a Boolean Series for sunny days. Assign the result to sunny.
Resample sunny by day and compute the sum. Assign the result to sunny_hours.
Resample sunny by day and compute the count. Assign the result to total_hours.
Divide sunny_hours by total_hours. Assign to sunny_fraction.
Make a box plot of sunny_fraction.

## Heat or humidity
100xp
Dew point is a measure of relative humidity based on pressure and temperature. A dew point above 65 is considered uncomfortable while a temperature above 90 is also considered uncomfortable.
In this exercise, you will explore the maximum temperature and dew point of each month. The columns of interest are 'dew_point_faren' and 'dry_bulb_faren'. After resampling them appropriately to get the maximum temperature and dew point in each month, generate a histogram of these values as subplots. Uncomfortably, you will notice that the maximum dew point is above 65 every month!
df_clean has been pre-loaded for you.
### Instructions
Select the 'dew_point_faren' and 'dry_bulb_faren' columns (in that order). Resample by month and aggregate the maximum monthly temperatures. Assign the result to monthly_max.
Plot a histogram of the resampled data with bins=8, alpha=0.5, and subplots=True.

## Probability of high temperatures
100xp
We already know that 2011 was hotter than the climate normals for the previous thirty years. In this final exercise, you will compare the maximum temperature in August 2011 against that of the August 2010 climate normals. More specifically, you will use a CDF plot to determine the probability of the 2011 daily maximum temperature in August being above the 2010 climate normal value. To do this, you will leverage the data manipulation, filtering, resampling, and visualization skills you have acquired throughout this course.
The two DataFrames df_clean and df_climate are available in the workspace. Your job is to select the maximum temperature in August in df_climate, and then maximum daily temperatures in August 2011. You will then filter out the days in August 2011 that were above the August 2010 maximum, and use this to construct a CDF plot.
Once you've generated the CDF, notice how it shows that there was a 50% probability of the 2011 daily maximum temperature in August being 5 degrees above the 2010 climate normal value!
### Instructions
From df_climate, extract the maximum temperature observed in August 2010. The relevant column here is 'Temperature'. You can select the rows corresponding to August 2010 in multiple ways. For example, df_climate.loc['2011-Feb'] selects all rows corresponding to February 2011, while df_climate.loc['2009-09', 'Pressure'] selects the rows corresponding to September 2009 from the 'Pressure' column.
From df_clean, select the August 2011 temperature data from the 'dry_bulb_faren'. Resample this data by day and aggregate the maximum value. Store the result in august_2011.
Filter out days in august_2011 where the value exceeded august_max. Store the result in august_2011_high.
Construct a CDF of august_2011_high using 25 bins. Remember to specify the kind, normed, and cumulative parameters in addition to bins.
