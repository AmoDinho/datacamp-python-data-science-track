# Chapter 1 - Basic plotting with Bokeh


## A simple scatter plot
In this example, you're going to make a scatter plot of female literacy vs fertility using data from the European Environmental Agency. This dataset highlights that countries with low female literacy have high birthrates. The x-axis data has been loaded for you as fertility and the y-axis data has been loaded as female_literacy.
Your job is to create a figure, assign x-axis and y-axis labels, and plot female_literacy vs fertility using the circle glyph.
After you have created the figure, in this exercise and the ones to follow, play around with it! Explore the different options available to you on the tab to the right, such as "Pan", "Box Zoom", and "Wheel Zoom". You can click on the question mark sign for more details on any of these tools.
Note: You may have to scroll down to view the lower portion of the figure.

### INSTRUCTIONS
100XP
Import the figure function from bokeh.plotting, and the output_file and show functions from bokeh.io.
Create the figure p with figure(). It has two parameters: x_axis_label and y_axis_label.
Add a circle glyph to the figure p using the function p.circle() where the inputs are, in order, the x-axis data and y-axis data.
Use the output_file() function to specify the name 'fert_lit.html' for the output file.
Create and display the output file using show() and passing in the figure p.

## A scatter plot with different shapes
By calling multiple glyph functions on the same figure object, we can overlay multiple data sets in the same figure.
In this exercise, you will plot female literacy vs fertility for two different regions, Africa and Latin America. Each set of x and y data has been loaded separately for you as fertility_africa, female_literacy_africa, fertility_latinamerica, and female_literacy_latinamerica.
Your job is to plot the Latin America data with the circle()glyph, and the Africa data with the x() glyph.
figure has already been imported for you from bokeh.plotting.
### INSTRUCTIONS
100XP
Create the figure p with the figure() function. It has two parameters: x_axis_label and y_axis_label.
Add a circle glyph to the figure p using the function p.circle() where the inputs are the x and y data from Latin America: fertility_latinamerica and female_literacy_latinamerica.
Add an x glyph to the figure p using the function p.x()where the inputs are the x and y data from Africa: fertility_africa and female_literacy_africa.
The code to create, display, and specify the name of the output file has been written for you, so after adding the x glyph, hit 'Submit Answer' to view the figure.
## Customizing your scatter plots
The three most important arguments to customize scatter glyphs are color, size, and alpha. Bokeh accepts colors as hexadecimal strings, tuples of RGB values between 0 and 255, and any of the 147 CSS color names. Size values are supplied in screen space units with 100 meaning the size of the entire figure.
The alpha parameter controls transparency. It takes in floating point numbers between 0.0, meaning completely transparent, and 1.0, meaning completely opaque.
In this exercise, you'll plot female literacy vs fertility for Africa and Latin America as red and blue circle glyphs, respectively.
### INSTRUCTIONS
100XP
Using the Latin America data (fertility_latinamerica and female_literacy_latinamerica), add a blue circle glyph of size=10 and alpha=0.8 to the figure p. To do this, you will need to specify the color, size and alpha keyword arguments inside p.circle().
Using the Africa data (fertility_africa and female_literacy_africa), add a red circle glyph of size=10 and alpha=0.8 to the figure p.
## Lines
We can draw lines on Bokeh plots with the line() glyph function.
In this exercise, you'll plot the daily adjusted closing price of Apple Inc.'s stock (AAPL) from 2000 to 2013.
The data points are provided for you as lists. date is a list ofdatetime objects to plot on the x-axis and price is a list of prices to plot on the y-axis.
Since we are plotting dates on the x-axis, you must add x_axis_type='datetime' when creating the figure object.

### INSTRUCTIONS
100XP
Import the figure function from bokeh.plotting.
Create a figure p using the figure() function with x_axis_type set to 'datetime'. The other two parameters are x_axis_label and y_axis_label.
Plot date and price along the x- and y-axes using p.line().
## Lines and markers
Lines and markers can be combined by plotting them separately using the same data points.
In this exercise, you'll plot a line and circle glyph for the AAPL stock prices. Further, you'll adjust the fill_color keyword argument of the circle() glyph function while leaving the line_color at the default value.
The date and price lists are provided. The Bokeh figure object p that you created in the previous exercise has also been provided.

### INSTRUCTIONS
100XP
Plot date along the x-axis and price along the y-axis with p.line().
With date on the x-axis and price on the y-axis, use p.circle() to add a 'white' circle glyph of size 4. To do this, you will need to specify the fill_color and sizearguments.


## Patches
In Bokeh, extended geometrical shapes can be plotted by using the patches() glyph function. The patches glyph takes as input a list-of-lists collection of numeric values specifying the vertices in x and y directions of each distinct patch to plot.
In this exercise, you will plot the state borders of Arizona, Colorado, New Mexico and Utah. The latitude and longitude vertices for each state have been prepared as lists.
Your job is to plot longitude on the x-axis and latitude on the y-axis. The figure object has been created for you as p.
### INSTRUCTIONS
100XP
Create a list of the longitude positions for each state as x. This has already been done for you.
Create a list of the latitude positions for each state as y. The variable names for the latitude positions are az_lats, co_lats, nm_lats, and ut_lats.
Use p.patches() to add the patches glyph to the figure p. Supply the x and y lists as arguments along with a line_color of 'white'.

## Plotting data from NumPy arrays
In the previous exercises, you made plots using data stored in lists. You learned that Bokeh can plot both numbers and datetime objects.
In this exercise, you'll generate NumPy arrays using np.linspace() and np.cos() and plot them using the circle glyph.
np.linspace() is a function that returns an array of evenly spaced numbers over a specified interval. For example, np.linspace(0, 10, 5) returns an array of 5 evenly spaced samples calculated over the interval [0, 10]. np.cos(x)calculates the element-wise cosine of some array x.
For more information on NumPy functions, you can refer to the NumPy User Guide and NumPy Reference.
The figure p has been provided for you.
### INSTRUCTIONS
100XP
Import numpy as np.
Create an array x using np.linspace() with 0, 5, and 100 as inputs.
Create an array y using np.cos() with x as input.
Add circles at x and y using p.circle().


## Plotting data from Pandas DataFrames
You can create Bokeh plots from Pandas DataFrames by passing column selections to the glyph functions.
Bokeh can plot floating point numbers, integers, and datetime data types. In this example, you will read a CSV file containing information on 392 automobiles manufactured in the US, Europe and Asia from 1970 to 1982.
The CSV file is provided for you as 'auto.csv'.
Your job is to plot miles-per-gallon (mpg) vs horsepower (hp) by passing Pandas column selections into the p.circle()function. Additionally, each glyph will be colored according to values in the color column.

### INSTRUCTIONS
100XP
Import pandas as pd.
Use the read_csv() function of pandas to read in 'auto.csv' and store it in the DataFrame df.
Import figure from bokeh.plotting.
Use the figure() function to create a figure p with the x-axis labeled 'HP' and the y-axis labeled 'MPG'.
Plot mpg (on the y-axis) vs hp (on the x-axis) by colorusing p.circle(). Note that the x-axis should be specified before the y-axis inside p.circle(). You will need to use Pandas DataFrame indexing to pass in the columns. For example, to access the color column, you can use df['color'], and then pass it in as an argument to the color parameter of p.circle(). Also specify a size of 10.

## The Bokeh ColumnDataSource (continued)
You can create a ColumnDataSource object directly from a Pandas DataFrame by passing the DataFrame to the class initializer.
In this exercise, we have imported pandas as pd and read in a data set containing all Olympic medals awarded in the 100 meter sprint from 1896 to 2012. A color column has been added indicating the CSS colorname we wish to use in the plot for every data point.
Your job is to import the ColumnDataSource class, create a new ColumnDataSource object from the DataFrame df, and plot circle glyphs with 'Year' on the x-axis and 'Time' on the y-axis. Color each glyph by the color column.
The figure object p has already been created for you.
### INSTRUCTIONS
100XP
Import the ColumnDataSource class from bokeh.plotting.
Use the ColumnDataSource() function to make a new ColumnDataSource object called source from the DataFrame df.
Use p.circle() to plot circle glyphs of size=8 on the figure p with 'Year' on the x-axis and 'Time' on the y-axis. Be sure to also specify source=source and color='color' so that the ColumnDataSource object is used and each glyph is colored by the color column.

## Selection and non-selection glyphs
In this exercise, you're going to add the box_select tool to a figure and change the selected and non-selected circle glyph properties so that selected glyphs are red and non-selected glyphs are transparent blue.
You'll use the ColumnDataSource object of the Olympic Sprint dataset you made in the last exercise. It is provided to you with the name source.
After you have created the figure, be sure to experiment with the Box Select tool you added! As in previous exercises, you may have to scroll down to view the lower portion of the figure.

### INSTRUCTIONS
100XP
Create a figure p with an x-axis label of 'Year', y-axis label of 'Time', and the 'box_select' tool. To add the 'box_select' tool, you have to specify the keyword argument tools='box_select' inside the figure() function.
Now that you have added 'box_select' to p, add in circle glyphs with p.circle() such that the selected glyphs are red and non-selected glyphs are transparent blue. This can be done by specifying 'red' as the argument to selection_colorand 0.1 to nonselection_alpha. Remember to also pass in the arguments for the x ('Year'), y ('Time'), and source parameters of p.circle().
Click 'Submit Answer' to output the file and show the figure.


## Hover glyphs
Now let's practice using and customizing the hover tool.
In this exercise, you're going to plot the blood glucose levels for an unknown patient. The blood glucose levels were recorded every 5 minutes on October 7th starting at 3 minutes past midnight.
The date and time of each measurement are provided to you as x and the blood glucose levels in mg/dL are provided as y.
A bokeh figure is also provided in the workspace as p.
Your job is to add a circle glyph that will appear red when the mouse is hovered near the data points. You will also add a customized hover tool object to the plot.
When you're done, play around with the hover tool you just created! Notice how the points where your mouse hovers over turn red.

#### INSTRUCTIONS
100XP
Import HoverTool from bokeh.models.
Add a circle glyph to the existing figure p for x and y with a size of 10, fill_color of 'grey', alpha of 0.1, line_color of None, hover_fill_color of 'firebrick', hover_alpha of 0.5, and hover_line_color of 'white'.
Use the HoverTool() function to create a HoverTool called hover with tooltips=None and mode='vline'.
Add the HoverTool hover to the figure p using the p.add_tools() function.

## Colormapping
The final glyph customization we'll practice is using the CategoricalColorMapper to color each glyph by a categorical property.
Here, you're going to use the automobile dataset to plot miles-per-gallon vs weight and color each circle glyph by the region where the automobile was manufactured.
The origin column will be used in the ColorMapper to color automobiles manufactured in the US as blue, Europe as red and Asia as green.
The automobile data set is provided to you as a Pandas DataFrame called df. The figure is provided for you as p.

### INSTRUCTIONS
100XP
Import CategoricalColorMapper from bokeh.models.
Convert the DataFrame df to a ColumnDataSource called source. This has already been done for you.
Make a CategoricalColorMapper object called color_mapperwith the CategoricalColorMapper() function. It has two parameters here: factors and palette.
Add a circle glyph to the figure p to plot 'mpg' (on the y-axis) vs 'weight' (on the x-axis). Remember to pass in source and 'origin' as arguments to source and legend. For the color parameter, use dict(field='origin', transform=color_mapper).

