# Chapter 2 - Exploratory data analysis


## pandas line plots
100xp
In the previous chapter, you saw that the .plot() method will place the Index values on the x-axis by default. In this exercise, you'll practice making line plots with specific columns on the x and y axes.
You will work with a dataset consisting of monthly stock prices in 2015 for AAPL, GOOG, and IBM. The stock prices were obtained from Yahoo Finance. Your job is to plot the 'Month' column on the x-axis and the AAPL and IBM prices on the y-axis using a list of column names.
All necessary modules have been imported for you, and the DataFrame is available in the workspace as df. Explore it using methods such as .head(), .info(), and .describe() to see the column names.
### Instructions
- Create a list of y-axis column names called y_columnsconsisting of 'AAPL' and 'IBM'.
- Generate a line plot with x='Month' and y=y_columns as inputs.
- Give the plot a title of 'Monthly stock prices'.
- Specify the y-axis label.
- Display the plot.

## pandas scatter plots
100xp
Pandas scatter plots are generated using the kind='scatter' keyword argument. Scatter plots require that the x and y columns be chosen by specifying the x and y parameters inside .plot(). Scatter plots also take an s keyword argument to provide the radius of each circle to plot in pixels.
In this exercise, you're going to plot fuel efficiency (miles-per-gallon) versus horse-power for 392 automobiles manufactured from 1970 to 1982 from the UCI Machine Learning Repository.
The size of each circle is provided as a NumPy array called sizes. This array contains the normalized 'weight' of each automobile in the dataset.
All necessary modules have been imported and the DataFrame is available in the workspace as df.
### Instructions
- Generate a scatter plot with 'hp' on the x-axis and 'mpg'on the y-axis. Specify s=sizes.
- Add a title to the plot.
- Specify the x-axis and y-axis labels.

## pandas box plots
100xp
While pandas can plot multiple columns of data in a single figure, making plots that share the same x and y axes, there are cases where two columns cannot be plotted together because their units do not match. The.plot() method can generate subplots for each column being plotted. Here, each plot will be scaled independently.
In this exercise your job is to generate box plots for fuel efficiency (mpg) and weight from the automobiles data set. To do this in a single figure, you'll specify subplots=True inside .plot() to generate two separate plots.
All necessary modules have been imported and the automobiles dataset is available in the workspace as df.
### Instructions
- Make a list called cols of the column names to be plotted: 'weight' and 'mpg'. You can then access it using df[cols].
- Generate a box plot of the two columns in a single figure. To do this, specify subplots=True.

## pandas hist, pdf and cdf
100xp
Pandas relies on the .hist() method to not only generate histograms, but also plots of probability density functions (PDFs) and cumulative density functions (CDFs).
In this exercise, you will work with a dataset consisting of restaurant bills that includes the amount customers tipped.
The original dataset is provided by the Seaborn package.
Your job is to plot a PDF and CDF for the fraction column of the tips dataset. This column contains information about what fraction of the total bill comprised of the tip.
Remember, when plotting the PDF, you need to specify normed=True in your call to .hist(), and when plotting the CDF, you need to specify cumulative=True in addition to normed=True.
All necessary modules have been imported and the tips dataset is available in the workspace as df. Also, some formatting code has been written so that the plots you generate will appear on separate rows.
### Instructions
-Plot a PDF for the values in fraction with 30 binsbetween 0 and 30%. The range has been taken care of for you. ax=axes[0] means that this plot will appear in the first row.
- Plot a CDF for the values in fraction with 30 binsbetween 0 and 30%. Again, the range has been specified for you. To make the CDF appear on the second row, you need to specify ax=axes[1].

## Bachelor's degrees awarded to women
100xp
In this exercise, you will investigate statistics of the percentage of Bachelor's degrees awarded to women from 1970 to 2011. Data is recorded every year for 17 different fields. This data set was obtained from the Digest of Education Statistics.
Your job is to compute the minimum and maximum values of the 'Engineering' column and generate a line plot of the mean value of all 17 academic fields per year. To perform this step, you'll use the .mean()method with the keyword argument axis='columns'. This computes the mean across all columns per row.
The DataFrame has been pre-loaded for you as df with the index set to 'Year'.
### Instructions
Print the minimum value of the 'Engineering' column.
Print the maximum value of the 'Engineering' column.
Construct the mean percentage per year with .mean(axis='columns'). Assign the result to mean.
Plot the average percentage per year. Since 'Year' is the index of df, it will appear on the x-axis of the plot. No keyword arguments are needed in your call to .plot().

## Median vs mean
100xp
In many data sets, there can be large differences in the mean and median value due to the presence of outliers.
In this exercise, you'll investigate the mean, median, and max fare prices paid by passengers on the Titanic and generate a box plot of the fare prices. This data set was obtained from Vanderbilt University.
All necessary modules have been imported and the DataFrame is available in the workspace as df.
### Instructions
- Print summary statistics of the 'fare' column of df with .describe() and print(). Note: df.fare and df['fare'] are equivalent.
- Generate a box plot of the 'fare' column.

## Quantiles
100xp
In this exercise, you'll investigate the probabilities of life expectancy in countries around the world. This dataset contains life expectancy for persons born each year from 1800 to 2015. Since country names change or results are not reported, not every country has values. This dataset was obtained from Gapminder.
First, you will determine the number of countries reported in 2015. There are a total of 206 unique countries in the entire dataset. Then, you will compute the 5th and 95th percentiles of life expectancy over the entire dataset. Finally, you will make a box plot of life expectancy every 50 years from 1800 to 2000. Notice the large change in the distributions over this period.
The dataset has been pre-loaded into a DataFrame called df.
### Instructions
- Print the number of countries reported in 2015. To do this, use the .count() method on the '2015' column of df.
- Print the 5th and 95th percentiles of df. To do this, use the .quantile() method with the list [0.05, 0.95].
- Generate a box plot using the list of columns provided in years. This has already been done for you, so click on 'Submit Answer' to view the result!
## Standard deviation of temperature
100xp
Let's use the mean and standard deviation to explore differences in temperature distributions in Pittsburgh in 2013. The data has been obtained from Weather Underground.
In this exercise, you're going to compare the distribution of daily temperatures in January and March. You'll compute the mean and standard deviation for these two months. You will notice that while the mean values are similar, the standard deviations are quite different, meaning that one month had a larger fluctuation in temperature than the other.
The DataFrames have been pre-loaded for you as january, which contains the January data, and march, which contains the March data.
### Instructions
- Compute and print the means of the January and March data using the .mean() method.
- Compute and print the standard deviations of the January and March data using the .std() method.

## Filtering and counting
50xp
How many automobiles were manufactured in Asia in the automobile dataset? The DataFrame has been provided for you as df. Use filtering and the .count() member method to determine the number of rows where the 'origin' column has the value 'Asia'.
As an example, you can extract the rows that contain 'US' as the country of origin using df[df['origin'] == 'US'].


df[df['origin'] == 'US'].count()


## Separate and summarize
100xp
Let's use population filtering to determine how the automobiles in the US differ from the global average and standard deviation. How the distribution of fuel efficiency (MPG) for the US differ from the global average and standard deviation?
In this exercise, you'll compute the means and standard deviations of all columns in the full automobile dataset. Next, you'll compute the same quantities for just the US population and subtract the global values from the US values.
All necessary modules have been imported and the DataFrame has been pre-loaded as df.
### Instructions
- Compute the global mean and global standard deviations of df using the .mean() and .std() methods. Assign the results to global_mean and global_std.
- Filter the 'US' population from the 'origin' column and assign the result to us.
- Compute the US mean and US standard deviations of us using the .mean() and .std() methods. Assign the results to us_mean and us_std.
- Print the differences between us_mean and global_meanand us_std and global_std. This has already been done for you.
## Separate and plot
100xp
Population filtering can be used alongside plotting to quickly determine differences in distributions between the sub-populations. You'll work with the Titanic dataset.
There were three passenger classes on the Titanic, and passengers in each class paid a different fare price. In this exercise, you'll investigate the differences in these fare prices.
Your job is to use Boolean filtering and generate box plots of the fare prices for each of the three passenger classes. The fare prices are contained in the 'fare' column and passenger class information is contained in the 'pclass' column.
When you're done, notice the portions of the box plots that differ and those that are similar.
The DataFrame has been pre-loaded for you as titanic.
### Instructions
- Inside plt.subplots(), specify the nrows and ncolsparameters so that there are 3 rows and 1 column.
- Filter the rows where the 'pclass' column has the values 1 and generate a box plot of the 'fare' column.
- Filter the rows where the 'pclass' column has the values 2 and generate a box plot of the 'fare' column.
- Filter the rows where the 'pclass' column has the values 3 and generate a box plot of the 'fare' column.

