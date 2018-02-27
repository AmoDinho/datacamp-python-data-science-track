## Chapter 5 - Bringing it all together

USA_edition_grouped = medals.loc[medals.NOC == 'USA'].groupby('Edition')

## Using .value_counts() for ranking
100xp
For this exercise, you will use the pandas Series method .value_counts() to determine the top 15 countries ranked by total number of medals.
Notice that .value_counts() sorts by values by default. The result is returned as a Series of counts indexed by unique entries from the original Series with values (counts) ranked in descending order.
The DataFrame has been pre-loaded for you as medals.
### Instructions
Extract the 'NOC' column from the DataFrame medals and assign the result to country_names. Notice that this Series has repeated entries for every medal (of any type) a country has won in any Edition of the Olympics.
Create a Series medal_counts by applying .value_counts() to the Series country_names.
Print the top 15 countries ranked by total number of medals won. This has been done for you, so hit 'Submit Answer' to see the result.


## Using .pivot_table() to count medals by type
100xp
Rather than ranking countries by total medals won and showing that list, you may want to see a bit more detail. You can use a pivot table to compute how many separate bronze, silver and gold medals each country won. That pivot table can then be used to repeat the previous computation to rank by total medals won.
In this exercise, you will use .pivot_table() first to aggregate the total medals by type. Then, you can use .sum() along the columns of the pivot table to produce a new column. When the modified pivot table is sorted by the total medals column, you can display the results from the last exercise with a bit more detail.
### Instructions
Construct a pivot table counted from the DataFrame medals aggregating by count. Use 'NOC' as the index, 'Athlete' for the values, and 'Medal' for the columns.
Modify the DataFrame counted by adding a column counted['totals']. The new column 'totals' should contain the result of taking the sum along the columns (i.e., use .sum(axis='columns')).
Overwrite the DataFrame counted by sorting it with the .sort_values() method. Specify the keyword argument ascending=False.
Print the first 15 rows of counted using .head(15). This has been done for you, so hit 'Submit Answer' to see the result.
## Applying .drop_duplicates()
0xp
What could be the difference between the 'Event_gender' and 'Gender' columns? You should be able to evaluate your guess by looking at the unique values of the pairs (Event_gender, Gender) in the data. In particular, you should not see something like (Event_gender='M', Gender='Women'). However, you will see that, strangely enough, there is an observation with (Event_gender='W', Gender='Men').
The duplicates can be dropped using the .drop_duplicates() method, leaving behind the unique observations. The DataFrame has been loaded as medals.
### Instructions
Select the columns 'Event_gender' and 'Gender'.
Create a dataframe ev_gen_uniques containing the unique pairs contained in ev_gen.
Print ev_gen_uniques. This has been done for you, so hit 'Submit Answer' to see the result.


## Finding possible errors with .groupby()
0xp
You will now use .groupby() to continue your exploration. Your job is to group by 'Event_gender' and 'Gender' and count the rows.
You will see that there is only one suspicious row: This is likely a data error.
The DataFrame is available to you as medals.
### Instructions
Group medals by 'Event_gender' and 'Gender'.
Create a medal_count_by_gender DataFrame with a group count using the .count() method.
Print medal_count_by_gender. This has been done for you, so hit 'Submit Answer' to view the result.

## Locating suspicious data
100xp
You will now inspect the suspect record by locating the offending row.
You will see that, according to the data, Joyce Chepchumba was a man that won a medal in a women's event. That is a data error as you can confirm with a web search.
### Instructions
Create a Boolean Series with a condition that captures the only row that has medals.Event_gender == 'W' and medals.Gender == 'Men'. Be sure to use the & operator.
Use the Boolean Series to create a DataFrame called suspectwith the suspicious row.
Print suspect. This has been 


## Using .nunique() to rank by distinct sports
100xp
You may want to know which countries won medals in the most distinct sports. The .nunique() method is the principal aggregation here. Given a categorical Series S, S.nunique() returns the number of distinct categories.
### Instructions
Group medals by 'NOC'.
Compute the number of distinct sports in which each country won medals. To do this, select the 'Sport' column from country_grouped and apply .nunique().
Sort Nsports in descending order with .sort_values()and ascending=False.
Print the first 15 rows of Nsports. This has been done for you, so hit 'Submit Answer' to see the result.


## Counting USA vs. USSR Cold War Olympic Sports
100xp
The Olympic competitions between 1952 and 1988 took place during the height of the Cold War between the United States of America (USA) & the Union of Soviet Socialist Republics (USSR). Your goal in this exercise is to aggregate the number of distinct sports in which the USA and the USSR won medals during the Cold War years.
The construction is mostly the same as in the preceding exercise. There is an additional filtering stage beforehand in which you reduce the original DataFrame medals by extracting data from the Cold War period that applies only to the US or to the USSR. The relevant country codes in the DataFrame, which has been pre-loaded as medals, are 'USA' & 'URS'.
### Instructions
Create a Boolean Series called during_cold_war by extracting all rows from medals for which the 'Edition' is >= 1952 and <= 1988.
Create a Boolean Series called is_usa_urs by extracting rows from medals for which 'NOC' is either 'USA' or 'URS'.
Filter the medals DataFrame using during_cold_war and is_usa_urs to create a new DataFrame called cold_war_medals.
Group cold_war_medals by 'NOC'.
Create a Series Nsports from country_grouped using indexing & chained methods:
Extract the column 'Sport'.
Use .nunique() to get the number of unique elements in each group;
Apply .sort_values(ascending=False) to rearrange the Series.
Print the final Series Nsports. This has been done for you, so hit 'Submit Answer' to see the result!


## Counting USA vs. USSR Cold War Olympic Medals
100xp
For this exercise, you want to see which country, the USA or the USSR, won the most medals consistently over the Cold War period.
There are several steps involved in carrying out this computation.
You'll need a pivot table with years ('Edition') on the index and countries ('NOC') on the columns. The entries will be the total number of medals each country won that year. If the country won no medals in a given edition, expect a NaN in that entry of the pivot table.
You'll need to slice the Cold War period and subset the 'USA' and 'URS' columns.
You'll need to make a Series from this slice of the pivot table that tells which country won the most medals in that edition using .idxmax(axis='columns'). If .max() returns the maximum value of Series or 1D array, .idxmax() returns the index of the maximizing element. The argument axis=columns or axis=1 is required because, by default, this aggregation would be done along columns for a DataFrame.
The final Series contains either 'USA' or 'URS' according to which country won the most medals in each Olympic edition. You can use .value_counts() to count the number of occurrences of each.
### Instructions
Construct medals_won_by_country using medals.pivot_table().
The index should the years ('Edition') & the columns should be country ('NOC')
the values should be 'Athlete' (which captures every medal regardless of kind) & the aggregation method should be 'count' (which captures the total number of medals won).
Create cold_war_usa_usr_medals by slicing the pivot table medals_won_by_country. Your slice should contain the editions from years 1952:1988 and only the columns 'USA' & 'URS' from the pivot table.
Create the Series most_medals by applying the .idxmax()method to cold_war_usa_usr_medals. Be sure to use axis='columns'.
Print the result of applying .value_counts() to most_medals. The result reported gives the number of times each of the USA or the USSR won more Olympic medals in total than the other between 1952 and 1988.


## Visualizing USA Medal Counts by Edition: Line Plot
0xp
Your job in this exercise is to visualize the medal counts by 'Edition' for the USA. The DataFrame has been pre-loaded for you as medals.
### Instructions
Create a DataFrame usa with data only for the USA.
Group usa such that ['Edition', 'Medal'] is the index. Aggregate the count over 'Athlete'.
Use .unstack() with level='Medal' to reshape the DataFrame usa_medals_by_year.
Construct a line plot from the final DataFrame usa_medals_by_year. This has been done for you, so hit 'Submit Answer' to see the plot!

## Visualizing USA Medal Counts by Edition: Area Plot
100xp
As in the previous exercise, your job in this exercise is to visualize the medal counts by 'Edition' for the USA. This time, you will use an area plot to see the breakdown better. The usa DataFrame has been created and all reshaping from the previous exercise has been done. You need to write the plotting command.
### Instructions
Create an area plot of usa_medals_by_year. This can be done by using .plot.area().



## Visualizing USA Medal Counts by Edition: Area Plot with Ordered Medals
100xp
You may have noticed that the medals are ordered according to a lexicographic (dictionary) ordering: Bronze < Gold < Silver. However, you would prefer an ordering consistent with the Olympic rules: Bronze < Silver < Gold.
You can achieve this using Categorical types. In this final exercise, after redefining the 'Medal' column of the DataFrame medals, you will repeat the area plot from the previous exercise to see the new ordering.
### Instructions
Redefine the 'Medal' column of the DataFrame medals as an ordered categorical. To do this, use pd.Categorical() with three keyword arguments:
values = medals.Medal.
categories=['Bronze', 'Silver', 'Gold'].
ordered=True.
After this, you can verify that the type has changed using medals.info().
Plot the final DataFrame usa_medals_by_year as an area plot. This has been done for you, so hit 'Submit Answer' to see how the plot has changed!
