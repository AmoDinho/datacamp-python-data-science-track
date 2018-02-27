# Chapter 4 - Putting It All Together! A Case Study
## Some exploratory plots of the data
Here, you'll continue your Exploratory Data Analysis by making a simple plot of Life Expectancy vs Fertility for the year 1970.
Your job is to import the relevant Bokeh modules and then prepare a ColumnDataSource object with the fertility, life and Country columns, where you only select the rows with the index value 1970.
Remember, as with the figures you generated in previous chapters, you can interact with your figures here with a variety of tools.
### INSTRUCTIONS
100XP
Import output_file and show from bokeh.io, figure from bokeh.plotting, and HoverTool and ColumnDataSource from bokeh.models.
Make a ColumnDataSource called source with x set to the fertilitycolumn, y set to the life column and country set to the Country column. For all columns, select the rows with index value 1970. This can be done using data.loc[1970].column_name.




## Beginning with just a plot
Let's get started on the Gapminder app. Your job is to make the ColumnDataSourceobject, prepare the plot, and add circles for Life expectancy vs Fertility. You'll also set x and y ranges for the axes.
As in the previous chapter, the DataCamp environment executes the bokeh servecommand to run the app for you. When you hit 'Submit Answer', you'll see in the IPython Shell that bokeh serve script.py gets called to run the app. This is something to keep in mind when you are creating your own interactive visualizations outside of the DataCamp environment.

### INSTRUCTIONS
100XP
Make a ColumnDataSource object called source with 'x', 'y', 'country', 'pop' and 'region' keys. The Pandas selections are provided for you.
Save the minimum and maximum values of the life expectancy column data.life as ymin and ymax. As a guide, you can refer to the way we saved the minimum and maximum values of the fertility column data.fertility as xmin and xmax.
Create a plot called plot() by specifying the title, setting plot_height to 400, plot_width to 700, and adding the x_range and y_rangeparameters.
Add circle glyphs to the plot. Specify an fill_alpha of 0.8 and source=source.

## Enhancing the plot with some shading
Now that you have the base plot ready, you can enhance it by coloring each circle glyph by continent.
Your job is to make a list of the unique regions from the data frame, prepare a ColorMapper, and add it to the circle glyph.
### INSTRUCTIONS
100XP
Make a list of the unique values from the region column. You can use the unique() and tolist() methods on data.region to do this.
Import CategoricalColorMapper from bokeh.models and the Spectral6palette from bokeh.palettes.
Use the CategoricalColorMapper() function to make a color mapper called color_mapper with factors=regions_list and palette=Spectral6.
Add the color mapper to the circle glyph as a dictionary with dict(field='region', transform=color_mapper) as the argument passed to the color parameter of plot.circle(). Also set the legend parameter to be the 'region'.
Set the legend.location attribute of plot to 'top_right'.

## Adding a slider to vary the year
Until now, we've been plotting data only for 1970. In this exercise, you'll add a slider to your plot to change the year being plotted. To do this, you'll create an update_plot() function and associate it with a slider to select values between 1970 and 2010.
After you are done, you may have to scroll to the right to view the entire plot. As you play around with the slider, notice that the title of the plot is not updated along with the year. This is something you'll fix in the next exercise!
### INSTRUCTIONS
100XP
Import the widgetbox and row functions from bokeh.layouts, and the Slider function from bokeh.models.
Define the update_plot callback function with parameters attr, old and new.
Set the yr name to slider.value and set source.data = new_data.
Make a slider object called slider using the Slider() function with a startyear of 1970, end year of 2010, step of 1, value of 1970, and title of 'Year'.
Attach the callback to the 'value' property of slider. This can be done using on_change() and passing in 'value' and update_plot.
Make a row layout of widgetbox(slider) and plot and add it to the current document.

## Customizing based on user input
Remember how in the plot from the previous exercise, the title did not update along with the slider? In this exercise, you'll fix this.
In Python, you can format strings by specifying placeholders with the % keyword. For example, if you have a string company = 'DataCamp', you can use print('%s' % company) to print DataCamp. Placeholders are useful when you are printing values that are not static, such as the value of the year slider. You can specify a placeholder for a number with %d. Here, when you're updating the plot title inside your callback function, you should make use of a placeholder so that the year displayed is in accordance with the value of the year slider.
In addition to updating the plot title, you'll also create the callback function and slider as you did in the previous exercise, so you get a chance to practice these concepts further.
All necessary modules have been imported for you, and as in the previous exercise, you may have to scroll to the right to view the entire figure.
### INSTRUCTIONS
100XP
Define the update_plot callback function with parameters attr, old and new.
Inside update_plot(), assign the value of the slider, slider.value, to yr and set source.data = new_data.
Inside update_plot(), specify plot.title.text to update the plot title and add it to the figure. You want the plot to update based on the value of the slider, which you have assigned above to yr. Make use of the placeholder syntax provided for you.
Make a slider object called slider using the Slider() function with a startyear of 1970, end year of 2010, step of 1, value of 1970, and title of 'Year'.
Attach the callback to the 'value' property of slider. This can be done using on_change() and passing in 'value' and update_plot.

#Adding a hover tool
In this exercise, you'll practice adding a hover tool to drill down into data column values and display more detailed information about each scatter point.
After you're done, experiment with the hover tool and see how it displays the name of the country when your mouse hovers over a point!
The figure and slider have been created for you and are available in the workspace as plot and slider.
### INSTRUCTIONS
100XP
Import HoverTool from bokeh.models.
Create a HoverTool object called hover with tooltips=[('Country', '@country')].
Add the HoverTool object you created to the plot using add_tools().
Create a row layout using widgetbox(slider) and plot.
Add the layout to the current document. This has already been done for you.

## Adding dropdowns to the app
As a final step in enhancing your application, in this exercise you'll add dropdowns for interactively selecting different data features. In combination with the hover tool you added in the previous exercise, as well as the slider to change the year, you'll have a powerful app that allows you to interactively and quickly extract some great insights from the dataset!
All necessary modules have been imported, and the previous code you wrote is taken care off. In the provided sample code, the dropdown for selecting features on the x-axis has been added for you. Using this as a reference, your job in this final exercise is to add a dropdown menu for selecting features on the y-axis.
Take a moment, after you are done, to enjoy exploring the visualization by experimenting with the hover tools, sliders, and dropdown menus that you have learned how to implement in this course.
### INSTRUCTIONS
100XP
Inside the update_plot() callback function, read in the current value of the ydropdown, y_select.
Use plot.yaxis.axis_label to label the y-axis as y.
Set the start and end range of the y-axis of plot.
Specify the parameters of the y_select dropdown widget: options, value, and title. The default value should be 'life'.
Attach the callback to the 'value' property of y_select. This can be done using on_change() and passing in 'value' and update_plot.

