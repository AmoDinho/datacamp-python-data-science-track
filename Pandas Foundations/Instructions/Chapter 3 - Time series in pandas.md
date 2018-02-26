# Chapter 3 - Time series in pandas
## Partial string indexing and slicing
100xp
Pandas time series support "partial string" indexing. What this means is that even when passed only a portion of the datetime, such as the date but not the time, pandas is remarkably good at doing what one would expect. Pandas datetime indexing also supports a wide variety of commonly used datetime string formats, even when mixed.
In this exercise, a time series that contains hourly weather data has been pre-loaded for you. This data was read using the parse_dates=True option in read_csv() with index_col="Dates" so that the Index is indeed a DatetimeIndex.
All data from the 'Temperature' column has been extracted into the variable ts0. Your job is to use a variety of natural date strings to extract one or more values from ts0.
After you are done, you will have three new variables - ts1, ts2, and ts3. You can slice these further to extract only the first and last entries of each. Try doing this after your submission for more practice.
### Instructions
Extract data from ts0 for a single hour - the hour from 9pm to 10pm on 2010-10-11. Assign it to ts1.
Extract data from ts0 for a single day - July 4th, 2010 - and assign it to ts2.
Extract data from ts0 for the second half of December 2010 - 12/15/2010 to 12/31/2010. Assign it to ts3.


## Reindexing the Index
100xp
Reindexing is useful in preparation for adding or otherwise combining two time series data sets. To reindex the data, we provide a new index and ask pandas to try and match the old data to the new index. If data is unavailable for one of the new index dates or times, you must tell pandas how to fill it in. Otherwise, pandas will fill with NaN by default.
In this exercise, two time series data sets containing daily data have been pre-loaded for you, each indexed by dates. The first, ts1, includes weekends, but the second, ts2, does not. The goal is to combine the two data sets in a sensible way. Your job is to reindex the second data set so that it has weekends as well, and then add it to the first. When you are done, it would be informative to inspect your results.
### Instructions
Create a new time series ts3 by reindexing ts2 with the index of ts1. To do this, call .reindex() on ts2 and pass in the index of ts1 (ts1.index).
Create another new time series, ts4, by calling the same .reindex() as above, but also specifiying a fill method, using the keyword argument method="ffill" to forward-fill values.
Add ts1 + ts2. Assign the result to sum12.
Add ts1 + ts3. Assign the result to sum13.
Add ts1 + ts4, Assign the result to sum14.

## Resampling and frequency
100xp
Pandas provides methods for resampling time series data. When downsampling or upsampling, the syntax is similar, but the methods called are different. Both use the concept of 'method chaining' - df.method1().method2().method3() - to direct the output from one method call to the input of the next, and so on, as a sequence of operations, one feeding into the next.
For example, if you have hourly data, and just need daily data, pandas will not guess how to throw out the 23 of 24 points. You must specify this in the method. One approach, for instance, could be to take the mean, as in df.resample('D').mean().
In this exercise, a data set containing hourly temperature data has been pre-loaded for you. Your job is to resample the data using a variety of aggregation methods to answer a few questions.
### Instructions
Downsample the 'Temperature' column of df to 6 hour data using .resample('6h') and .mean(). Assign the result to df1.
Downsample the 'Temperature' column of df to daily data using .resample('D') and then count the number of data points in each day with .count(). Assign the result df2.


## Separating and resampling
100xp
With pandas, you can resample in different ways on different subsets of your data. For example, resampling different months of data with different aggregations. In this exercise, the data set containing hourly temperature data from the last exercise has been pre-loaded.
Your job is to resample the data using a variety of aggregation methods. The DataFrame is available in the workspace as df. You will be working with the 'Temperature' column.
### Instructions
Use partial string indexing to extract temperature data for August 2010 into august.
Use the temperature data for August and downsample to find the daily maximum temperatures. Store the result in august_highs.
Use partial string indexing to extract temperature data for February 2010 into february.
Use the temperature data for February and downsample to find the daily minimum temperatures. Store the result in february_lows.

## Rolling mean and frequency
100xp
In this exercise, some hourly weather data is pre-loaded for you. You will continue to practice resampling, this time using rolling means.
Rolling means (or moving averages) are generally used to smooth out short-term fluctuations in time series data and highlight long-term trends. You can read more about them here.
To use the .rolling() method, you must always use method chaining, first calling .rolling() and then chaining an aggregation method after it. For example, with a Series hourly_data, hourly_data.rolling(window=24).mean() would compute new values for each hourly point, based on a 24-hour window stretching out behind each point. The frequency of the output data is the same: it is still hourly. Such an operation is useful for smoothing time series data.
Your job is to resample the data using the combination of .rolling()and .mean(). You will work with the same DataFrame df from the previous exercise.
### Instructions
Use partial string indexing to extract temperature data from August 1 2010 to August 15 2010. Assign to unsmoothed.
Use .rolling() with a 24 hour window to smooth the mean temperature data. Assign the result to smoothed.
Use a dictionary to create a new DataFrame august with the time series smoothed and unsmoothed as columns.
Plot both the columns of august as line plots using the .plot() method.

## Resample and roll with it
100xp
As of pandas version 0.18.0, the interface for applying rolling transformations to time series has become more consistent and flexible, and feels somewhat like a groupby (If you do not know what a groupby is, don't worry, you will learn about it in the next course!).
You can now more flexibly chain together both resampling as well as rolling operations. In this exercise, the same weather data from the previous exercises has been pre-loaded for you. Your job is to extract one month of data, resample to find the daily high temperatures, and then use a rolling and aggregation operation to smooth the data.
### Instructions
Use partial string indexing to extract August 2010 temperature data, and assign to august.
Resample to daily frequency, saving the maximum daily temperatures, and assign the result to daily_highs.
As part of one long method chain, repeat the above resampling (or you can re-use daily_highs) and then combine it with .rolling() to apply a 7 day .mean() (with window=7inside .rolling()) so as to smooth the daily highs. Assign the result to daily_highs_smoothed and print the result.
## Method chaining and filtering
100xp
We've seen that pandas supports method chaining. This technique can be very powerful when cleaning and filtering data.
In this exercise, a DataFrame containing flight departure data for a single airline and a single airport for the month of July 2015 has been pre-loaded. Your job is to use .str() filtering and method chaining to generate summary statistics on flight delays each day to Dallas.
### Instructions
Use .str.strip() to strip extra whitespace from df.columns. Assign the result back to df.columns.
In the 'Destination Airport' column, extract all entries where Dallas ('DAL') is the destination airport. Use .str.contains('DAL') for this and store the result in dallas.
Resample dallas such that you get the total number of departures each day. Store the result in daily_departures.
Generate summary statistics for daily Dallas departures using .describe(). Store the result in stats.
## Missing values and interpolation
100xp
One common application of interpolation in data analysis is to fill in missing data.
In this exercise, noisy measured data that has some dropped or otherwise missing values has been loaded. The goal is to compare two time series, and then look at summary statistics of the differences. The problem is that one of the data sets is missing data at some of the times. The pre-loaded data ts1 has value for all times, yet the data set ts2 does not: it is missing data for the weekends.
Your job is to first interpolate to fill in the data for all days. Then, compute the differences between the two data sets, now that they both have full support for all times. Finally, generate the summary statistics that describe the distribution of differences.
### Instructions
Replace the index of ts2 with that of ts1, and then fill in the missing values of ts2 by using .interpolate(how='linear'). Save the result as ts2_interp.
Compute the difference between ts1 and ts2_interp. Take the absolute value of the difference with np.abs(), and assign the result to differences.
Generate and print summary statistics of the differenceswith .describe() and print().


## Time zones and conversion
0xp
Time zone handling with pandas typically assumes that you are handling the Index of the Series. In this exercise, you will learn how to handle timezones that are associated with datetimes in the column data, and not just the Index.
You will work with the flight departure dataset again, and this time you will select Los Angeles ('LAX') as the destination airport.
Here we will use a mask to ensure that we only compute on data we actually want. To learn more about Boolean masks, click here!
### Instructions
Create a Boolean mask, mask, such that if the 'Destination Airport' column of df equals 'LAX', the result is True, and otherwise, it is False.
Use the mask to extract only the LAX rows. Assign the result to la.
Concatenate the two columns la['Date (MM/DD/YYYY)'] and la['Wheels-off Time'] with a ' ' space in between. Pass this to pd.to_datetime() to create a datetime array of all the times the LAX-bound flights left the ground.
Use Series.dt.tz_localize() to localize the time to 'US/Central'.
Use the .dt.tz_convert() method to convert datetimes from 'US/Central' to 'US/Pacific'.

## Plotting time series, datetime indexing
100xp
Pandas handles datetimes not only in your data, but also in your plotting.
In this exercise, some time series data has been pre-loaded. However, we have not parsed the date-like columns nor set the index, as we have done for you in the past!
The plot displayed is how pandas renders data with the default integer/positional index. Your job is to convert the 'Date' column from a collection of strings into a collection of datetime objects. Then, you will use this converted 'Date' column as your new index, and re-plot the data, noting the improved datetime awareness. After you are done, you can cycle between the two plots you generated by clicking on the 'Previous Plot' and 'Next Plot' buttons.
Before proceeding, look at the plot shown and observe how pandas handles data with the default integer index. Then, inspect the DataFrame df using the .head()method in the IPython Shell to get a feel for its structure.
### Instructions
Use pd.to_datetime() to convert the 'Date' column to a collection of datetime objects, and assign back to df.Date.
Set the index to this updated 'Date' column, using df.set_index() with the optional keyword argument inplace=True, so that you don't have to assign the result back to df.
Re-plot the DataFrame to see that the axis is now datetime aware. This code has been written for you.

## Plotting date ranges, partial indexing
100xp
Now that you have set the DatetimeIndex in your DataFrame, you have a much more powerful and flexible set of tools to use when plotting your time series data. Of these, one of the most convenient is partial string indexing and slicing. In this exercise, we've pre-loaded a full year of Austin 2010 weather data, with the index set to be the datetime parsed 'Date' column as shown in the previous exercise.
Your job is to use partial string indexing of the dates, in a variety of datetime string formats, to plot all the summer data and just one week of data together. After you are done, you can cycle between the two plots by clicking on the 'Previous Plot' and 'Next Plot' buttons.
First, remind yourself how to extract one month of temperature data using 'May 2010' as a key into df.Temperature[], and call head() to inspect the result: df.Temperature['May 2010'].head().
### Instructions
Plot the summer temperatures using method chaining. The summer ranges from the months '2010-Jun' to '2010-Aug'.
Plot the temperatures for one week in June using the same method chaining, but this time indexing with '2010-06-10':'2010-06-17'before you follow up with .plot().

