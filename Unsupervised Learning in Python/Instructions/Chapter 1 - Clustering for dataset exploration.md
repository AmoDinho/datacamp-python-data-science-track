# Chapter 1 - Clustering for dataset exploration

## Clustering 2D points
From the scatter plot of the previous exercise, you saw that the points seem to separate into 3 clusters. You'll now create a KMeans model to find 3 clusters, and fit it to the data points from the previous exercise. After the model has been fit, you'll obtain the cluster labels for some new points using the .predict()method.
You are given the array points from the previous exercise, and also an array new_points.

### INSTRUCTIONS
100XP
Import KMeans from sklearn.cluster.
Using KMeans(), create a KMeans instance called model to find 3 clusters. To specify the number of clusters, use the n_clusters keyword argument.
Use the .fit() method of model to fit the model to the array of points points.
Use the .predict() method of model to predict the cluster labels of new_points, assigning the result to labels.
Hit 'Submit Answer' to see the cluster labels of new_points.

## Inspect your clustering
Let's now inspect the clustering you performed in the previous exercise!
A solution to the previous exercise has already run, so new_points is an array of points and labels is the array of their cluster labels.

### INSTRUCTIONS
100XP
Import matplotlib.pyplot as plt.
Assign column 0 of new_points to xs, and column 1 of new_points to ys.
Make a scatter plot of xs and ys, specifying the c=labelskeyword arguments to color the points by their cluster label. Also specify alpha=0.5.
Compute the coordinates of the centroids using the .cluster_centers_ attribute of model.
Assign column 0 of centroids to centroids_x, and column 1 of centroids to centroids_y.
Make a scatter plot of centroids_x and centroids_y, using 'D' (a diamond) as a marker by specifying the markerparameter. Set the size of the markers to be 50 using s=50


## How many clusters of grain?
In the video, you learned how to choose a good number of clusters for a dataset using the k-means inertia graph. You are given an array samples containing the measurements (such as area, perimeter, length, and several others) of samples of grain. What's a good number of clusters in this case?
KMeans and PyPlot (plt) have already been imported for you.
This dataset was sourced from the UCI Machine Learning Repository.
### INSTRUCTIONS
100XP
For each of the given values of k, perform the following steps:
Create a KMeans instance called model with k clusters.
Fit the model to the grain data samples.
Append the value of the inertia_ attribute of model to the list inertias.
The code to plot ks vs inertias has been written for you, so hit 'Submit Answer' to see the plot!
## Evaluating the grain clustering
In the previous exercise, you observed from the inertia plot that 3 is a good number of clusters for the grain data. In fact, the grain samples come from a mix of 3 different grain varieties: "Kama", "Rosa" and "Canadian". In this exercise, cluster the grain samples into three clusters, and compare the clusters to the grain varieties using a cross-tabulation.
You have the array samples of grain samples, and a list varieties giving the grain variety for each sample. Pandas (pd) and KMeans have already been imported for you.
### INSTRUCTIONS
100XP
Create a KMeans model called model with 3 clusters.
Use the .fit_predict() method of model to fit it to samples and derive the cluster labels. Using .fit_predict() is the same as using .fit() followed by .predict().
Create a DataFrame df with two columns named 'labels'and 'varieties', using labels and varieties, respectively, for the column values. This has been done for you.
Use the pd.crosstab() function on df['labels'] and df['varieties'] to count the number of times each grain variety coincides with each cluster label. Assign the result to ct.
Hit 'Submit Answer' to see the cross-tabulation!


## Scaling fish data for clustering
You are given an array samples giving measurements of fish. Each row represents an individual fish. The measurements, such as weight in grams, length in centimeters, and the percentage ratio of height to length, have very different scales. In order to cluster this data effectively, you'll need to standardize these features first. In this exercise, you'll build a pipeline to standardize and cluster the data.
These fish measurement data were sourced from the Journal of Statistics Education.

### INSTRUCTIONS
100XP
Import:
make_pipeline from sklearn.pipeline.
StandardScaler from sklearn.preprocessing.
KMeans from sklearn.cluster.
Create an instance of StandardScaler called scaler.
Create an instance of KMeans with 4 clusters called kmeans.
Create a pipeline called pipeline that chains scaler and kmeans. To do this, you just need to pass them in as arguments to make_pipeline().
## Clustering the fish data
You'll now use your standardization and clustering pipeline from the previous exercise to cluster the fish by their measurements, and then create a cross-tabulation to compare the cluster labels with the fish species.
As before, samples is the 2D array of fish measurements. Your pipeline is available as pipeline, and the species of every fish sample is given by the list species.
### INSTRUCTIONS
100XP
Import pandas as pd.
Fit the pipeline to the fish measurements samples.
Obtain the cluster labels for samples by using the .predict() method of pipeline.
Using pd.DataFrame(), create a DataFrame df with two columns named 'labels' and 'species', using labelsand species, respectively, for the column values.
Using pd.crosstab(), create a cross-tabulation ct of df['labels'] and df['species']


## Clustering stocks using KMeans
In this exercise, you'll cluster companies using their daily stock price movements (i.e. the dollar difference between the closing and opening prices for each trading day). You are given a NumPy array movements of daily price movements from 2010 to 2015 (obtained from Yahoo! Finance), where each row corresponds to a company, and each column corresponds to a trading day.
Some stocks are more expensive than others. To account for this, include a Normalizer at the beginning of your pipeline. The Normalizer will separately transform each company's stock price to a relative scale before the clustering begins.
Note that Normalizer() is different to StandardScaler(), which you used in the previous exercise. While StandardScaler() standardizes features (such as the features of the fish data from the previous exercise) by removing the mean and scaling to unit variance, Normalizer() rescales each sample - here, each company's stock price - independently of the other.
KMeans and make_pipeline have already been imported for you.
### INSTRUCTIONS
100XP
Import Normalizer from sklearn.preprocessing.
Create an instance of Normalizer called normalizer.
Create an instance of KMeans called kmeans with 10clusters.
Using make_pipeline(), create a pipeline called pipelinethat chains normalizer and kmeans.
Fit the pipeline to the movements array.


## Which stocks move together?
In the previous exercise, you clustered companies by their daily stock price movements. So which company have stock prices that tend to change in the same way? You'll now inspect the cluster labels from your clustering to find out.
Your solution to the previous exercise has already been run. Recall that you constructed a Pipeline pipeline containing a KMeans model and fit it to the NumPy array movements of daily stock movements. In addition, a list companies of the company names is available.

### INSTRUCTIONS
100XP
Import pandas as pd.
Use the .predict() method of the pipeline to predict the labels for movements.
Align the cluster labels with the list of company names companies by creating a DataFrame df with labels and companies as columns. This has been done for you.
Use the .sort_values() method of df to sort the DataFrame by the 'labels' column, and print the result.
Hit 'Submit Answer' and take a moment to see which companies are together in each cluster!

