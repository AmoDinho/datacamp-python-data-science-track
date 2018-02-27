# Chapter 2 - Plotting 2D arrays

## Working with 2d arrays
In order to visualize two-dimensional arrays of data, it is necessary to understand how to generate and manipulate 2-D arrays. Many Matplotlib plots support arrays as input and in particular, they support NumPy arrays. The NumPy library is the most widely-supported means for supporting numeric arrays in Python.
In this exercise, you will use the meshgrid function in NumPy to generate 2-D arrays which you will then visualize using plt.imshow(). The simplest way to generate a meshgrid is as follows:
import numpy as np
Y,X = np.meshgrid(range(10),range(20))


This will create two arrays with a shape of (20,10), which corresponds to 20 rows along the Y-axis and 10 columns along the X-axis. In this exercise, you will use np.meshgrid() to generate a regular 2-D sampling of a mathematical function.

### INSTRUCTIONS
100XP
Import the numpy and matplotlib.pyplot modules using the respective aliases np and plt.
Generate two one-dimensional arrays u and v using np.linspace(). The array u should contain 41 values uniformly spaced beween -2 and +2. The array v should contain 21 values uniformly spaced between -1 and +1.
Construct two two-dimensional arrays X and Y from uand v using np.meshgrid(). The resulting arrays should have shape (41,21).
After the array Z is computed using X and Y, visualize the array Z using plt.pcolor() and plt.show().
Save the resulting figure as 'sine_mesh.png'.


## Contour & filled contour plots
Although plt.imshow() or plt.pcolor() are often used to visualize a 2-D array in entirety, there are other ways of visualizing such data without displaying all the available sample values. One option is to use the array to compute contours that are visualized instead.
Two types of contour plot supported by Matplotlib are plt.contour() and plt.contourf() where the former displays the contours as lines and the latter displayed filled areas between contours. Both these plotting commands accept a two dimensional array from which the appropriate contours are computed.
In this exercise, you will visualize a 2-D array repeatedly using both plt.contour() and plt.contourf(). You will use plt.subplot() to display several contour plots in a common figure, using the meshgrid X, Y as the axes. For example, plt.contour(X, Y, Z) generates a default contour map of the array Z.

### INSTRUCTIONS
100XP
Using the meshgrid X, Y as axes:
Generate a default contour plot of the array Z in the upper left subplot.
Generate a contour plot of the array Z in the upper right subplot with 20 contours.
Generate a default filled contour plot of the array Z in the lower left subplot.
Generate a default filled contour plot of the array Z in the lower right subplot with 20 contours.
Improve the spacing between the subplots with plt.tight_layout() and display the figure.


## Modifying colormaps
When displaying a 2-D array with plt.imshow() or plt.pcolor(), the values of the array are mapped to a corresponding color. The set of colors used is determined by a colormap which smoothly maps values to colors, making it easy to understand the structure of the data at a glance.
It is often useful to change the colormap from the default 'jet'colormap used by matplotlib. A good colormap is visually pleasing and conveys the structure of the data faithfully and in a way that makes sense for the application.
Some matplotlib colormaps have unique names such as 'jet', 'coolwarm', 'magma' and 'viridis'.
Others have a naming scheme based on overall color such as 'Greens', 'Blues', 'Reds', and 'Purples'.
Another four colormaps are based on the seasons, namely 'summer', 'autumn', 'winter' and 'spring'.
You can insert the option cmap=<name> into most matplotlib functions to change the color map of the resulting plot.
In this exercise, you will explore four different colormaps together using plt.subplot(). You will use a pregenerated array Z and a meshgrid X, Y to generate the same filled contour plot with four different color maps. Be sure to also add a color bar to each filled contour plot with plt.colorbar().
### INSTRUCTIONS
100XP
Modify the call to plt.contourf() so the filled contours in the top left subplot use the 'viridis' colormap.
Modify the call to plt.contourf() so the filled contours in the top right subplot use the 'gray' colormap.
Modify the call to plt.contourf() so the filled contours in the bottom left subplot use the 'autumn' colormap.
Modify the call to plt.contourf() so the filled contours in the bottom right subplot use the 'winter' colormap.


## Using hist2d()
Given a set of ordered pairs describing data points, you can count the number of points with similar values to construct a two-dimensional histogram. This is similar to a one-dimensional histogram, but it describes the joint variation of two random variables rather than just one.
In matplotlib, one function to visualize 2-D histograms is plt.hist2d().
You specify the coordinates of the points using plt.hist2d(x,y) assuming x and y are two vectors of the same length.
You can specify the number of bins with the argument bins=(nx, ny) where nx is the number of bins to use in the horizontal direction and ny is the number of bins to use in the vertical direction.
You can specify the rectangular region in which the samples are counted in constructing the 2D histogram. The optional parameter required is range=((xmin, xmax), (ymin, ymax)) where
xmin and xmax are the respective lower and upper limits for the variables on the x-axis and
ymin and ymax are the respective lower and upper limits for the variables on the y-axis. Notice that the optional range argument can use nested tuples or lists.
In this exercise, you'll use some data from the auto-mpg data set. There are two arrays mpg and hp that respectively contain miles per gallon and horse power ratings from over three hundred automobiles built.

### INSTRUCTIONS
100XP
Generate a two-dimensional histogram to view the joint variation of the mpg and hp arrays.
Put hp along the horizontal axis and mpg along the vertical axis.
Specify 20 by 20 rectangular bins with the bins argument.
Specify the region covered with the optional range argument so that the plot samples hp between 40 and 235 on the x-axis and mpg between 8 and 48 on the y-axis.
Add a color bar to the histogram.


## Using hexbin()
The function plt.hist2d() uses rectangular bins to construct a two dimensional histogram. As an alternative, the function plt.hexbin() uses hexagonal bins. The underlying algorithm (based on this article from 1987) constructs a hexagonal tesselation of a planar region and aggregates points insidehexagonal bins.
The optional gridsize argument (default 100) gives the number of hexagons across the x-direction used in the hexagonal tiling. If specified as a list or a tuple of length two, gridsize fixes the number of hexagon in the x- and y-directions respectively in the tiling.
The optional parameter extent=(xmin, xmax, ymin, ymax) specifies rectangular region covered by the hexagonal tiling. In that case, xminand xmax are the respective lower and upper limits for the variables on the x-axis and ymin and ymax are the respective lower and upper limits for the variables on the y-axis.
In this exercise, you'll use the same auto-mpg data as in the last exercise (again using arrays mpg and hp). This time, you'll use plt.hexbin() to visualize the two-dimensional histogram.
### INSTRUCTIONS
100XP
Generate a two-dimensional histogram with plt.hexbin() to view the joint variation of the mpg and hp vectors.
Put hp along the horizontal axis and mpg along the vertical axis.
Specify a hexagonal tesselation with 15 hexagons across the x-direction and 12 hexagons across the y-direction using gridsize.
Specify the rectangular region covered with the optional extent argument: use hp from 40 to 235 and mpg from 8 to 48.
Add a color bar to the histogram.

## Loading, examining images
Color images such as photographs contain the intensity of the red, green and blue color channels.
To read an image from file, use plt.imread() by passing the path to a file, such as a PNG or JPG file.
The color image can be plotted as usual using plt.imshow().
The resulting image loaded is a NumPy array of three dimensions. The array typically has dimensions M×N×3M×N×3, where M×NM×N is the dimensions of the image. The third dimensions are referred to as color channels (typically red, green, and blue).
The color channels can be extracted by Numpy array slicing.
In this exercise, you will load & display an image of an astronaut(by NASA (Public domain), via Wikimedia Commons). You will also examine its attributes to understand how color images are represented.
### INSTRUCTIONS
100XP
Load the file '480px-Astronaut-EVA.jpg' into an array.
Print the shape of the img array. How wide and tall do you expect the image to be?
Prepare img for display using plt.imshow().
Turn off the axes using plt.axis('off').

## Pseudocolor plot from image data
Image data comes in many forms and it is not always appropriate to display the available channels in RGB space. In many situations, an image may be processed and analysed in some way before it is visualized in pseudocolor, also known as 'false' color.
In this exercise, you will perform a simple analysis using the image showing an astronaut as viewed from space. Instead of simply displaying the image, you will compute the total intensity across the red, green and blue channels. The result is a single two dimensional array which you will display using plt.imshow()with the 'gray' colormap.

### INSTRUCTIONS
100XP
Print the shape of the existing image array.
Compute the sum of the red, green, and blue channels of imgby using the .sum() method with axis=2.
Print the shape of the intensity array to verify this is the shape you expect.
Plot intensity with plt.imshow() using a 'gray'colormap.
Add a colorbar to the figure.


## Extent and aspect
When using plt.imshow() to display an array, the default behavior is to keep pixels square so that the height to width ratio of the output matches the ratio determined by the shape of the array. In addition, by default, the x- and y-axes are labeled by the number of samples in each direction.
The ratio of the displayed width to height is known as the image aspect and the range used to label the x- and y-axes is known as the image extent. The default aspect value of 'auto'keeps the pixels square and the extents are automatically computed from the shape of the array if not specified otherwise.
In this exercise, you will investigate how to set these options explicitly by plotting the same image in a 2 by 2 grid of subplots with distinct aspect and extent options.
### INSTRUCTIONS
100XP
Display img in the top left subplot with horizontal extent from -1 to 1, vertical extent from -1 to 1, and aspect ratio 0.5.
Display img in the top right subplot with horizontal extent from -1 to 1, vertical extent from -1 to 1, and aspect ratio 1.
Display img in the bottom left subplot with horizontal extent from -1 to 1, vertical extent from -1 to 1, and aspect ratio 2.
Display img in the bottom right subplot with horizontal extent from -2 to 2, vertical extent from -1 to 1, and aspect ratio 2.

## Rescaling pixel intensities
Sometimes, low contrast images can be improved by rescalingtheir intensities. For instance, this image of Hawkes Bay, New Zealand (originally by Phillip Capper, modified by User:Konstable, via Wikimedia Commons, CC BY 2.0) has no pixel values near 0 or near 255 (the limits of valid intensities).
For this exercise, you will do a simple rescaling (remember, an image is NumPy array) to translate and stretch the pixel intensities so that the intensities of the new image fill the range from 0 to 255.

### INSTRUCTIONS
100XP
Use the methods .min() and .max() to save the minimum and maximum values from the array image as pmin and pmax respectively.
Create a new 2-D array rescaled_image using 256*(image-pmin)/(pmax-pmin)
Plot the original array image in the top subplot of a 2×12×1 grid.
Plot the new array rescaled_image in the bottom subplot of a 2×12×1 grid.

