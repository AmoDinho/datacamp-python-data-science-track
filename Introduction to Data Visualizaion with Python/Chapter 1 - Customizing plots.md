# Chapter 1 - Customizing plots
## Multiple plots on single axis
It is time now to put together some of what you have learned and combine line plots on a common set of axes. The data set here comes from records of undergraduate degrees awarded to women in a variety of fields from 1970 to 2011. You can compare trends in degrees most easily by viewing two curves on the same set of axes.
Here, three NumPy arrays have been pre-loaded for you: year(enumerating years from 1970 to 2011 inclusive), physical_sciences (representing the percentage of Physical Sciences degrees awarded to women each in corresponding year), and computer_science (representing the percentage of Computer Science degrees awarded to women in each corresponding year).
You will issue two plt.plot() commands to draw line plots of different colors on the same set of axes. Here, year represents the x-axis, while physical_sciences and computer_scienceare the y-axes.

### INSTRUCTIONS
100XP
Import matplotlib.pyplot as its usual alias.
Add a 'blue' line plot of the % of degrees awarded to women in the Physical Sciences (physical_sciences) from 1970 to 2011 (year). Note that the x-axis should be specified first.
Add a 'red' line plot of the % of degrees awarded to women in Computer Science (computer_science) from 1970 to 2011 (year).
Use plt.show() to display the figure with the curves on the same axes.


## Using axes()
Rather than overlaying line plots on common axes, you may prefer to plot different line plots on distinct axes. The command plt.axes() is one way to do this (but it requires specifying coordinates relative to the size of the figure).
Here, you have the same three arrays year, physical_sciences, and computer_science representing percentages of degrees awarded to women over a range of years. You will use plt.axes() to create separate sets of axes in which you will draw each line plot.
In calling plt.axes([xlo, ylo, width, height]), a set of axes is created and made active with lower corner at coordinates (xlo, ylo) of the specified width and height. Note that these coordinates can be passed to plt.axes() in the form of a list or a tuple.
The coordinates and lengths are values between 0 and 1 representing lengths relative to the dimensions of the figure. After issuing a plt.axes() command, plots generated are put in that set of axes.
### INSTRUCTIONS
100XP
Create a set of plot axes with lower corner xlo and ylo of 0.05and 0.05, width of 0.425, and height of 0.9 (in units relative to the figure dimension).
Note: Remember to pass these coordinates to plt.axes()in the form of a list: [xlo, ylo, width, height].
Plot the percentage of degrees awarded to women in Physical Sciences in blue in the active axes just created.
Create a set of plot axes with lower corner xlo and ylo of 0.525 and 0.05, width of 0.425, and height of 0.9 (in units relative to the figure dimension).
Plot the percentage of degrees awarded to women in Computer Science in red in the active axes just created.

## Using subplot() (1)
The command plt.axes() requires a lot of effort to use well because the coordinates of the axes need to be set manually. A better alternative is to use plt.subplot() to determine the layout automatically.
In this exercise, you will continue working with the same arrays from the previous exercises: year, physical_sciences, and computer_science. Rather than using plt.axes() to explicitly lay out the axes, you will use plt.subplot(m, n, k) to make the subplot grid of dimensions m by n and to make the kth subplot active (subplots are numbered starting from 1 row-wise from the top left corner of the subplot grid).
### INSTRUCTIONS
100XP
Use plt.subplot() to create a figure with 1x2 subplot layout & make the first subplot active.
Plot the percentage of degrees awarded to women in Physical Sciences in blue in the active subplot.
Use plt.subplot() again to make the second subplot active in the current 1x2 subplot grid.
Plot the percentage of degrees awarded to women in Computer Science in red in the active subplot.

## Using subplot() (2)
Now you have some familiarity with plt.subplot(), you can use it to plot more plots in larger grids of subplots of the same figure.
Here, you will make a 2×22×2 grid of subplots and plot the percentage of degrees awarded to women in Physical Sciences (using physical_sciences), in Computer Science (using computer_science), in Health Professions (using health), and in Education (using education).
### INSTRUCTIONS
100XP
Create a figure with 2×22×2 subplot layout, make the top, left subplot active, and plot the % of degrees awarded to women in Physical Sciences in blue in the active subplot.
Make the top, right subplot active in the current 2×22×2 subplot grid and plot the % of degrees awarded to women in Computer Science in red in the active subplot.
Make the bottom, left subplot active in the current 2×22×2subplot grid and plot the % of degrees awarded to women in Health Professions in green in the active subplot.
Make the bottom, right subplot active in the current 2×22×2subplot grid and plot the % of degrees awarded to women in Education in yellow in the active subplot.


## Using xlim(), ylim()
In this exercise, you will work with the matplotlib.pyplotinterface to quickly set the x- and y-limits of your plots.
You will now create the same figure as in the previous exercise using plt.plot(), this time setting the axis extents using plt.xlim() and plt.ylim(). These commands allow you to either zoom or expand the plot or to set the axis ranges to include important values (such as the origin).
In this exercise, as before, the percentage of women graduates in Computer Science and in the Physical Sciences are held in the variables computer_science and physical_sciencesrespectively over year.
After creating the plot, you will use plt.savefig() to export the image produced to a file.
### INSTRUCTIONS
100XP
Use plt.xlim() to set the x-axis range to the period between the years 1990 and 2010.
Use plt.ylim() to set the y-axis range to the interval between 0% and 50% of degrees awarded.
Display the final figure with plt.show() and save the output to 'xlim_and_ylim.png'.


## Using axis()
Using plt.xlim() and plt.ylim() are useful for setting the axis limits individually. In this exercise, you will see how you can pass a 4-tuple to plt.axis() to set limits for both axes at once. For example, plt.axis((1980,1990,0,75)) would set the extent of the x-axis to the period between 1980 and 1990, and would set the y-axis extent from 0 to 75% degrees award.
Once again, the percentage of women graduates in Computer Science and in the Physical Sciences are held in the variables computer_science and physical_sciences where each value was measured at the corresponding year held in the yearvariable.
### INSTRUCTIONS
100XP
Use plt.axis() to select the time period between 1990 and 2010 on the x-axis as well as the interval between 0 and 50% awarded on the y-axis.
Save the resulting plot as 'axis_limits.png'.

## Using legend()
Legends are useful for distinguishing between multiple datasets displayed on common axes. The relevant data are created using specific line colors or markers in various plot commands. Using the keyword argument label in the plotting function associates a string to use in a legend.
For example, here, you will plot enrollment of women in the Physical Sciences and in Computer Science over time. You can label each curve by passing a label argument to the plotting call, and request a legend using plt.legend(). Specifying the keyword argument loc determines where the legend will be placed.

### INSTRUCTIONS
100XP
Modify the plot command provided that draws the enrollment of women in Computer Science over time so that the curve is labelled 'Computer Science' in the legend.
Modify the plot command provided that draws the enrollment of women in the Physical Sciences over time so that the curve is labelled 'Physical Sciences' in the legend.
Add a legend at the lower center (i.e., loc='lower center')


### Using annotate()
It is often useful to annotate a simple plot to provide context. This makes the plot more readable and can highlight specific aspects of the data. Annotations like text and arrows can be used to emphasize specific observations.
Here, you will once again plot enrollment of women in the Physical Sciences and Computer science over time. The legend is set up as before. Additionally, you will mark the inflection point when enrollment of women in Computer Science reached a peak and started declining using plt.annotate().
To enable an arrow, set arrowprops=dict(facecolor='black'). The arrow will point to the location given by xy and the text will appear at the location given by xytext.

### INSTRUCTIONS
100XP
Compute the maximum enrollment of women in Computer Science using the .max() method.
Calculate the year in which there was maximum enrollment of women in Computer Science using the .argmax() method.
Annotate the plot with an arrow at the point of peak women enrolling in Computer Science.
Label the arrow 'Maximum'. The parameter for this is s, but you don't have to specify it.
Pass in the arguments to xy and xytext as tuples.
For xy, use the yr_max and cs_max that you computed.
For xytext, use (yr_max+5, cs_max+5) to specify the displacement of the label from the tip of the arrow.
Draw the arrow by specifying the keyword argument arrowprops=dict(facecolor='black'). The single letter shortcut for 'black' is 'k'.


## Modifying styles
Matplotlib comes with a number of different stylesheets to customize the overall look of different plots. To activate a particular stylesheet you can simply call plt.style.use() with the name of the style sheet you want. To list all the available style sheets you can execute: print(plt.style.available).
### INSTRUCTIONS
100XP
Import matplotlib.pyplot as its usual alias.
Activate the 'ggplot' style sheet with plt.style.use().

