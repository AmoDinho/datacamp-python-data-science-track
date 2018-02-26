# Chapter 3 - Combining data for analysis

## Combining rows of data
100xp
The dataset you'll be working with here relates to NYC Uber data. The original dataset has all the originating Uber pickup locations by time and latitude and longitude. For didactic purposes, you'll be working with a very small portion of the actual data.
Three DataFrames have been pre-loaded: uber1, which contains data for April 2014, uber2, which contains data for May 2014, and uber3, which contains data for June 2014. Your job in this exercise is to concatenate these DataFrames together such that the resulting DataFrame has the data for all three months.
Begin by exploring the structure of these three DataFrames in the IPython Shell using methods such as .head().
### Instructions
Concatenate uber1, uber2, and uber3 together using pd.concat(). You'll have to pass the DataFrames in as a list.
Print the shape and then the head of the concatenated DataFrame, row_concat.

## Combining columns of data
100xp
Think of column-wise concatenation of data as stitching data together from the sides instead of the top and bottom. To perform this action, you use the same pd.concat() function, but this time with the keyword argument axis=1. The default, axis=0, is for a row-wise concatenation.
You'll return to the Ebola dataset you worked with briefly in the last chapter. It has been pre-loaded into a DataFrame called ebola_melt. In this DataFrame, the status and country of a patient is contained in a single column. This column has been parsed into a new DataFrame, status_country, where there are separate columns for status and country.
Explore the ebola_melt and status_country DataFrames in the IPython Shell. Your job is to concatenate them column-wise in order to obtain a final, clean DataFrame.
### Instructions
Concatenate ebola_melt and status_country column-wise into a single DataFrame called ebola_tidy. Be sure to specify axis=1 and to pass the two DataFrames in as a list.
Print the shape and then the head of the concatenated DataFrame, ebola_tidy.


## Finding files that match a pattern
100xp
You're now going to practice using the glob module to find all csv files in the workspace. In the next exercise, you'll programmatically load them into DataFrames.
As Dan showed you in the video, the glob module has a function called glob that takes a pattern and returns a list of the files in the working directory that match that pattern.
For example, if you know the pattern is part_ single digit number.csv, you can write the pattern as 'part_?.csv' (which would match part_1.csv, part_2.csv, part_3.csv, etc.)
Similarly, you can find all .csv files with '*.csv', or all parts with 'part_*'. The ? wildcard represents any 1 character, and the *wildcard represents any number of characters.
### Instructions
Import the glob module along with pandas (as its usual alias pd).
Write a pattern to match all .csv files.
Save all files that match the pattern using the glob() function within the glob module. That is, by using glob.glob().
Print the list of file names. This has been done for you.
Read the second file in csv_files (i.e., index 1) into a DataFrame called csv2.
Hit 'Submit Answer' to print the head of csv2. Does it look familiar?

## Iterating and concatenating all matches
100xp
Now that you have a list of filenames to load, you can load all the files into a list of DataFrames that can then be concatenated.
You'll start with an empty list called frames. Your job is to use a forloop to iterate through each of the filenames, read each filename into a DataFrame, and then append it to the frames list.
You can then concatenate this list of DataFrames using pd.concat(). Go for it!
### Instructions
Write a for loop to iterate though csv_files:
In each iteration of the loop, read csv into a DataFrame called df.
After creating df, append it to the list frames using the .append() method.
Concatenate frames into a single DataFrame called uber.
Hit 'Submit Answer' to see the head and shape of the concatenated DataFrame!
## 1-to-1 data merge
100xp
Merging data allows you to combine disparate datasets into a single dataset to do more complex analysis.
Here, you'll be using survey data that contains readings that William Dyer, Frank Pabodie, and Valentina Roerich took in the late 1920 and 1930 while they were on an expedition towards Antarctica. The dataset was taken from a sqlite database from the Software Carpentry SQL lesson.
Two DataFrames have been pre-loaded: site and visited. Explore them in the IPython Shell and take note of their structure and column names. Your task is to perform a 1-to-1 merge of these two DataFrames using the 'name' column of site and the 'site' column of visited.
### Instructions
Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited.
Print the merged DataFrame o2o

## Many-to-1 data merge
100xp
In a many-to-one (or one-to-many) merge, one of the values will be duplicated and recycled in the output. That is, one of the keys in the merge is not unique.
Here, the two DataFrames site and visited have been pre-loaded once again. Note that this time, visited has multiple entries for the site column. Confirm this by exploring it in the IPython Shell.
The .merge() method call is the same as the 1-to-1 merge from the previous exercise, but the data and output will be different.
### Instructions
Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited, exactly as you did in the previous exercise.
Print the merged DataFrame and then hit 'Submit Answer' to see the different output produced by this merge!
## Many-to-many data merge
100xp
The final merging scenario occurs when both DataFrames do not have unique keys for a merge. What happens here is that for each duplicated key, every pairwise combination will be created.
Two example DataFrames that share common key values have been pre-loaded: df1 and df2. Another DataFrame df3, which is the result of df1 merged with df2, has been pre-loaded. All three DataFrames have been printed - look at the output and notice how pairwise combinations have been created. This example is to help you develop your intuition for many-to-many merges.
Here, you'll work with the site and visited DataFrames from before, and a new survey DataFrame. Your task is to merge site and visited as you did in the earlier exercises. You will then merge this merged DataFrame with survey.
Begin by exploring the site, visited, and survey DataFrames in the IPython Shell.
### Instructions
Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited, exactly as you did in the previous two exercises. Save the result as m2m.
Merge the m2m and survey DataFrames on the 'ident'column of m2m and 'taken' column of survey.
Hit 'Submit Answer' to print the first 20 lines of the merged DataFrame!

