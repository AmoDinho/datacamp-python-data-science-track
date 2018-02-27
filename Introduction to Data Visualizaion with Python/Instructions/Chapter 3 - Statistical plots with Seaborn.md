# Chapter 3 - Statistical plots with Seaborn


## Simple linear regressions
As you have seen, seaborn provides a convenient interface to generate complex and great-looking statistical plots. One of the simplest things you can do using seaborn is to fit and visualize a simple linear regression between two variables using sns.lmplot().
One difference between seaborn and regular matplotlib plotting is that you can pass pandas DataFrames directly to the plot and refer to each column by name. For example, if you were to plot the column 'price' vs the column 'area' from a DataFrame df, you could call sns.lmplot(x='area', y='price', data=df).
In this exercise, you will once again use the DataFrame autocontaining the auto-mpg dataset. You will plot a linear regression illustrating the relationship between automobile weight and horse power.
### INSTRUCTIONS
100XP
Import matplotlib.pyplot and seaborn using the standard names plt and sns respectively.
Plot a linear regression between the 'weight' column (on the x-axis) and the 'hp' column (on the y-axis) from the DataFrame auto.
Display the plot as usual with plt.show(). This has been done for you, so hit 'Submit Answer' to view the plot.


## Plotting residuals of a regression
Often, you don't just want to see the regression itself but also see the residuals to get a better idea how well the regression captured the data. Seaborn provides sns.residplot() for that purpose, visualizing how far datapoints diverge from the regression line.
In this exercise, you will visualize the residuals of a regression between the 'hp' column (horse power) and the 'mpg'column (miles per gallon) of the auto DataFrame used previously.
### INSTRUCTIONS
100XP
Import matplotlib.pyplot and seaborn using the standard names plt and sns respectively.
Generate a green residual plot of the regression between 'hp' (on the x-axis) and 'mpg' (on the y-axis). You will need to specify the additional data and color parameters.
Display the plot as usual using plt.show(). This has been done for you, so hit 'Submit Answer' to view the plot.

## Higher-order regressions
When there are more complex relationships between two variables, a simple first order regression is often not sufficient to accurately capture the relationship between the variables. Seaborn makes it simple to compute and visualize regressions of varying orders.
Here, you will plot a second order regression between the horse power ('hp') and miles per gallon ('mpg') using sns.regplot() (the function sns.lmplot() is a higher-level interface to sns.regplot()). However, before plotting this relationship, compare how the residual changes depending on the order of the regression. Does a second order regression perform significantly better than a simple linear regression?
A principal difference between sns.lmplot() and sns.regplot() is the way in which matplotlib options are passed (sns.regplot() is more permissive).
For both sns.lmplot() and sns.regplot(), the keyword order is used to control the order of polynomial regression.
The function sns.regplot() uses the argument scatter=None to prevent plotting the scatter plot points again.
### INSTRUCTIONS
100XP
Modify the call to plt.scatter() to plot auto['weight'] on the x-axis and auto['mpg'] on the y-axis, filled with red circles and with label='data'.
Plot a linear regression line of 'order 1' between 'weight'and 'mpg' in 'blue' without the scatter points.
You need to specify the label and color parameters, in addition to scatter=None.
Plot a linear regression line of 'order 2' between 'weight'and 'mpg' in 'green' without the scatter points.
To force a higher order regression, you need to specify the order parameter. Here, it should be 2.
Add a legend to the 'upper right'.
## Grouping linear regressions by hue
Often it is useful to compare and contrast trends between different groups. Seaborn makes it possible to apply linear regressions separately for subsets of the data by applying a groupby operation. Using the hue argument, you can specify a categorical variable by which to group data observations. The distinct groups of points are used to produce distinct regressions with different hues in the plot.
In the automobile dataset - which has been pre-loaded here as auto - you can view the relationship between weight ('weight') and horsepower ('hp') of the cars and group them by their origin ('origin'), giving you a quick visual indication how the relationship differs by continent.
### INSTRUCTIONS
100XP
Plot a linear regression between 'weight' and 'hp'grouped by 'origin'.
Use the keyword argument hue to group rows with the categorical column 'origin'.
Use the keyword argument palette to specify the 'Set1' palette for coloring the distinct groups.
## Grouping linear regressions by row or column
Rather than overlaying linear regressions of grouped data in the same plot, we may want to use a grid of subplots. The sns.lmplot() accepts the arguments row and/or col to arrangements of subplots for regressions.
You'll use the automobile dataset again and, this time, you'll use the keyword argument row to display the subplots organized in rows. That is, you'll produce horsepower vs. weight regressions grouped by continent of origin in separate subplots stacked vertically.

### INSTRUCTIONS
100XP
Plot linear regressions of 'hp' (on the y-axis) versus 'weight' (on the x-axis) grouped row-wise by 'origin'from DataFrame auto.
Use the keyword argument row to group observations with the categorical column 'origin' in subplots organized in rows.


## Constructing strip plots
Regressions are useful to understand relationships between two continuous variables. Often we want to explore how the distribution of a single continuous variable is affected by a second categorical variable. Seaborn provides a variety of plot types to perform these types of comparisons between univariate distributions.
The strip plot is one way of visualizing this kind of data. It plots the distribution of variables for each category as individual datapoints. For vertical strip plots (the default), distributions of continuous values are laid out parallel to the y-axis and the distinct categories are spaced out along the x-axis.
For example, sns.stripplot(x='type', y='length', data=df)produces a sequence of vertical strip plots of lengthdistributions grouped by type (assuming length is a continuous column and type is a categorical column of the DataFrame df).
Overlapping points can be difficult to distinguish in strip plots. The argument jitter=True helps spread out overlapping points.
Other matplotlib arguments can be passed to sns.stripplot(), e.g., marker, color, size, etc.
### INSTRUCTIONS
100XP
In the first row of subplots, make a strip plot showing distribution of 'hp' values grouped horizontally by 'cyl'.
In the second row of subplots, make a second strip plot with improved readability. In particular, you'll call sns.stripplot()again, this time adding jitter=True and decreasing the point size to 3 using the size parameter.


## Constructing swarm plots
As you have seen, a strip plot can be visually crowded even with jitter applied and smaller point sizes. An alternative is provided by the swarm plot (sns.swarmplot()), which is very similar but spreads out the points to avoid overlap and provides a better visual overview of the data.
The syntax for sns.swarmplot() is similar to that of sns.stripplot(), e.g., sns.swarmplot(x='type', y='length', data=df).
The orientation for the continuous variable in the strip/swarm plot can be inferred from the choice of the columns x and y from the DataFrame data. The orientation can be set explicitly using orient='h'(horizontal) or orient='v' (vertical).
Another grouping can be added in using the hue keyword. For instance, using sns.swarmplot(x='type', y='length', data=df, hue='build year')makes a swarm plot from the DataFrame df with the 'length' column values spread out vertically, horizontally grouped by the column 'type' and each point colored by the categorical column 'build year'.
In this exercise, you'll use the auto DataFrame again to illustrate the use of sns.swarmplot() with grouping by hueand with explicit specification of the orientation using the keyword orient.
### INSTRUCTIONS
100XP
In the first row of subplots, make a swarm plot showing distribution of 'hp' values grouped horizontally by 'cyl'.
In the second row of subplots, make a second swarm plot with horizontal orientation (i.e., grouped vertically by 'cyl' with 'hp' value spread out horizontally) with points colored by 'origin'. You need to specify the orient parameter to explicitly set the horizontal orientation.


## Constructing violin plots
Both strip and swarm plots visualize all the datapoints. For large datasets, this can result in significant overplotting. Therefore, it is often useful to use plot types which reduce a dataset to more descriptive statistics and provide a good summary of the data. Box and whisker plots are a classic way of summarizing univariate distributions but seaborn provides a more sophisticated extension of the standard box plot, called a violin plot.
Here, you will produce violin plots of the distribution of horse power ('hp') by the number of cylinders ('cyl'). Additionally, you will combine two different plot types by overlaying a strip plot on the violin plot.
As before, the DataFrame has been pre-loaded for you as auto.
### INSTRUCTIONS
100XP
In the first row of subplots, make a violin plot showing the distribution of 'hp' grouped by 'cyl'.
In the second row of subplots, make a second violin plot without the inner annotations (by specifying inner=None) and with the color 'lightgray'.
In the second row of subplots, overlay a strip plot with jitter and a point size of 1.5.


## Plotting joint distributions (1)
There are numerous strategies to visualize how pairs of continuous random variables vary jointly. Regression and residual plots are one strategy. Another is to visualize a bivariate distribution.
Seaborn's sns.jointplot() provides means of visualizing bivariate distributions. The basic calling syntax is similar to that of sns.lmplot(). By default, calling sns.jointplot(x, y, data) renders a few things:
A scatter plot using the specified columns x and y from the DataFrame data.
A (univariate) histogram along the top of the scatter plot showing distribution of the column x.
A (univariate) histogram along the right of the scatter plot showing distribution of the column y.
### INSTRUCTIONS
100XP
Use sns.jointplot() to visualize the joint variation of the columns 'hp' (on the x-axis) and 'mpg' (on the y-axis) from the DataFrame auto


## Plotting joint distributions (2)
The seaborn function sns.jointplot() has a parameter kindto specify how to visualize the joint variation of two continuous random variables (i.e., two columns of a DataFrame)
kind='scatter' uses a scatter plot of the data points
kind='reg' uses a regression plot (default order 1)
kind='resid' uses a residual plot
kind='kde' uses a kernel density estimate of the joint distribution
kind='hex' uses a hexbin plot of the joint distribution
For this exercise, you will again use sns.jointplot() to display the joint distribution of the hp and mpg columns of the autoDataFrame. This time, you will use kind='hex' to generate a hexbin plot of the joint distribution.
### INSTRUCTIONS
100XP
Create a hexbin plot of the joint distribution between 'hp'and 'mpg'.

## Plotting distributions pairwise (1)
Data sets often contain more than two continuous variables. The function sns.jointplot() is restricted to representing joint variation between only two quantities (i.e., two columns of a DataFrame). Visualizing multivariate relationships is trickier.
The function sns.pairplot() constructs a grid of all joint plots pairwise from all pairs of (non-categorical) columns in a DataFrame. The syntax is very simple: sns.pairplot(df), where df is a DataFrame. The non-categorical columns are identified and the corresponding joint plots are plotted in a square grid of subplots. The diagonal of the subplot grid shows the univariate histograms of the individual columns.
In this exercise, you will use a DataFrame auto comprising only three columns from the original auto-mpg data set.

### INSTRUCTIONS
100XP
Print the first five rows of the DataFrame auto. This is done for you.
Plot the joint distributions between columns from the entire DataFrame auto.


## Plotting distributions pairwise (2)
In this exercise, you will generate pairwise joint distributions again. This time, you will make two particular additions:
You will display regressions as well as scatter plots in the off-diagonal subplots. You will do this with the argument kind='reg' (where 'reg' means 'regression'). Another option for kind is 'scatter' (the default) that plots scatter plots in the off-diagonal subplots.
You will also visualize the joint distributions separated by continent of origin. You will do this with the keyword argument hue specifying the 'origin'.

### INSTRUCTIONS
100XP
Plot the pairwise joint distributions separated by continent of origin and display the regressions.

## Visualizing correlations with a heatmap
Plotting relationships between many variables using a pair plot can quickly get visually overwhelming. It is therefore often useful to compute covariances between the variables instead. The covariance matrix can then easily be visualized as a heatmap. A heatmap is effectively a pseudocolor plot with labelled rows and columns (i.e., a pseudocolor plot based on a pandas DataFrame rather than a matrix). The DataFrame does not have to be square or symmetric (but, in the context of a covariance matrix, it is both).
In this exercise, you will view the covariance matrix between the continuous variables in the auto-mpg dataset. You do not have to know here how the covariance matrix is computed; the important point is that its diagonal entries are all 1s, and the off-diagonal entries are between -1 and +1 (quantifying the degree to which variable pairs vary jointly). It is also, then, a symmetric matrix.
### INSTRUCTIONS
100XP
Print the covariance matrix cov_matrix to examine its contents and labels. This has been done for you.
Plot the covariance matrix cov_matrix using sns.heatmap()


