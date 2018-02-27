#Chapter 1 - Parameter estimation by optimization

## How often do we get no-hitters?
The number of games played between each no-hitter in the modern era (1901-2015) of Major League Baseball is stored in the array nohitter_times.
If you assume that no-hitters are described as a Poisson process, then the time between no-hitters is Exponentially distributed. As you have seen, the Exponential distribution has a single parameter, which we will call \tau\tau, the typical interval time. The value of the parameter ττ that makes the exponential distribution best match the data is the mean interval time (where time is in units of number of games) between no-hitters.
Compute the value of this parameter from the data. Then, use np.random.exponential() to "repeat" the history of Major League Baseball by drawing inter-no-hitter times from an exponential distribution with the ττ you found and plot the histogram as an approximation to the PDF.
NumPy, pandas, matlotlib.pyplot, and seaborn have been imported for you as np, pd, plt, and sns, respectively.
### INSTRUCTIONS
100XP
Seed the random number generator with 42.
Compute the mean time (in units of number of games) between no-hitters.
Draw 100,000 samples from an Exponential distribution with the parameter you computed from the mean of the inter-no-hitter times.
Plot the theoretical PDF using plt.hist(). Remember to use keyword arguments bins=50, normed=True, and histtype='step'. Be sure to label your axes.


## Do the data follow our story?
You have modeled no-hitters using an Exponential distribution. Create an ECDF of the real data. Overlay the theoretical CDF with the ECDF from the data. This helps you to verify that the Exponential distribution describes the observed data.
It may be helpful to remind yourself of the function you created in the previous course to compute the ECDF, as well as the code you wrote to plot it.
### INSTRUCTIONS
100XP
Compute an ECDF from the actual time between no-hitters (nohitter_times). Use the ecdf() function you wrote in the prequel course.
Create a CDF from the theoretical samples you took in the last exercise (inter_nohitter_time).
Plot x_theor and y_theor as a line using plt.plot(). Then overlay the ECDF of the real data x and y as points. To do this, you have to specify the keyword arguments marker = '.' and linestyle = 'none' in addition to xand y inside plt.plot().
Set a 2% margin on the plot.
Show the plot.

## How is this parameter optimal?
Now sample out of an exponential distribution with ττ being twice as large as the optimal ττ. Do it again for ττ half as large. Make CDFs of these samples and overlay them with your data. You can see that they do not reproduce the data as well. Thus, the ττ you computed from the mean inter-no-hitter times is optimal in that it best reproduces the data.
Note: In this and all subsequent exercises, the random number generator is pre-seeded for you to save you some typing.

### Instructions


Take 10000 samples out of an Exponential distribution with parameter τ1/2τ1/2 = tau/2.
Take 10000 samples out of an Exponential distribution with parameter τ2τ2 = 2*tau.
Generate CDFs from these two sets of samples using your ecdf() function.
Add these two CDFs as lines to your plot. This has been done for you, so hit 'Submit Answer' to view the plot!


## EDA of literacy/fertility data
In the next few exercises, we will look at the correlation between female literacy and fertility (defined as the average number of children born per woman) throughout the world. For ease of analysis and interpretation, we will work with the illiteracy rate.
It is always a good idea to do some EDA ahead of our analysis. To this end, plot the fertility versus illiteracy and compute the Pearson correlation coefficient. The Numpy array illiteracyhas the illiteracy rate among females for most of the world's nations. The array fertility has the corresponding fertility data.
Here, it may be useful to refer back to the function you wrote in the previous course to compute the Pearson correlation coefficient.
### INSTRUCTIONS
100XP
Plot fertility (y-axis) versus illiteracy (x-axis) as a scatter plot.
Set a 2% margin.
Compute and print the Pearson correlation coefficient between illiteracy and fertility.

## Linear regression
We will assume that fertility is a linear function of the female illiteracy rate. That is, f=ai+bf=ai+b, where aa is the slope and bb is the intercept. We can think of the intercept as the minimal fertility rate, probably somewhere between one and two. The slope tells us how the fertility rate varies with illiteracy. We can find the best fit line using np.polyfit().
Plot the data and the best fit line. Print out the slope and intercept. (Think: what are their units?)

### INSTRUCTIONS
100XP
Compute the slope and intercept of the regression line using np.polyfit(). Remember, fertility is on the y-axis and illiteracy on the x-axis.
Print out the slope and intercept from the linear regression.
To plot the best fit line, create an array x that consists of 0 and 100 using np.array(). Then, compute the theoretical values of y based on your regression parameters. I.e., y = a * x + b.
Plot the data and the regression line on the same plot. Be sure to label your axes.
Hit 'Submit Answer' to display your plot.

## How is it optimal?
The function np.polyfit() that you used to get your regression parameters finds the optimal slope and intercept. It is optimizing the sum of the squares of the residuals, also known as RSS (for residual sum of squares). In this exercise, you will plot the function that is being optimized, the RSS, versus the slope parameter a. To do this, fix the intercept to be what you found in the optimization. Then, plot the RSS vs. the slope. Where is it minimal?
### INSTRUCTIONS
100XP
Specify the values of the slope for which to compute the RSS. Use np.linspace() to get 200 points in the range between 0 and 0.1. For example, to get 100 points in the range between 0 and 0.5, you could use np.linspace() like so: np.linspace(0, 0.5, 100).
Initialize an array, rss, to contain the RSS using np.empty_like() and the array you created above. The empty_like() function returns a new array with the same shape and type as a given array (in this case, a_vals).
Write a for loop to compute the sum of RSS of the slope. Hint: the RSS is given by np.sum((y_data - a * x_data - b)**2). The variable b you computed in the last exercise is already in your namespace. Here, fertility is the y_data and illiteracy the x_data.
Plot the RSS (rss) versus slope (a_vals).
Hit 'Submit Answer' to see the plot!


## Linear regression on appropriate Anscombe data
For practice, perform a linear regression on the data set from Anscombe's quartet that is most reasonably interpreted with linear regression.

### INSTRUCTIONS
100XP
Compute the parameters for the slope and intercept using np.polyfit(). The Anscombe data are stored in the arrays x and y.
Print the slope a and intercept b.
Generate theoretical xx and yy data from the linear regression. Your xx array, which you can create with np.array(), should consist of 3 and 15. To generate the yy data, multiply the slope by x_theor and add the intercept.
Plot the Anscombe data as a scatter plot and then plot the theoretical line. Remember to include the marker='.' and linestyle='none' keyword arguments in addition to x and y when to plot the Anscombe data as a scatter plot. You do not need these arguments when plotting the theoretical line.
Hit 'Submit Answer' to see the plot!
## Linear regression on all Anscombe data
Now, to verify that all four of the Anscombe data sets have the same slope and intercept from a linear regression, you will compute the slope and intercept for each set. The data are stored in lists; anscombe_x = [x1, x2, x3, x4] and anscombe_y = [y1, y2, y3, y4], where, for example, x2 and y2 are the xx and yy values for the second Anscombe data set.
### INSTRUCTIONS
100XP
Write a for loop to do the following for each Anscombe data set.
Compute the slope and intercept.
Print the slope and intercept.

