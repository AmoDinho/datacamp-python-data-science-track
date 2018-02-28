# Chapter 3 - Decorrelating your data and dimension reduction

## Correlated data in nature
You are given an array grains giving the width and length of samples of grain. You suspect that width and length will be correlated. To confirm this, make a scatter plot of width vs length and measure their Pearson correlation.

### INSTRUCTIONS
100XP
Import:
matplotlib.pyplot as plt.
pearsonr from scipy.stats.
Assign column 0 of grains to width and column 1 of grains to length.
Make a scatter plot with width on the x-axis and length on the y-axis.
Use the pearsonr() function to calculate the Pearson correlation of width and  length

## Decorrelating the grain measurements with PCA
You observed in the previous exercise that the width and length measurements of the grain are correlated. Now, you'll use PCA to decorrelate these measurements, then plot the decorrelated points and measure their Pearson correlation.
### INSTRUCTIONS
100XP
Import PCA from sklearn.decomposition.
Create an instance of PCA called model.
Use the .fit_transform() method of model to apply the PCA transformation to grains. Assign the result to pca_features.
The subsequent code to extract, plot, and compute the Pearson correlation of the first two columns pca_features has been written for you, so hit 'Submit Answer' to see the result!

## Principal components
On the right are three scatter plots of the same point cloud. Each scatter plot shows a different set of axes (in red). In which of the plots could the axes represent the principal components of the point cloud?
Recall that the principal components are the directions along which the the data varies.


Both plot 1 and plot 3.

## The first principal component
The first principal component of the data is the direction in which the data varies the most. In this exercise, your job is to use PCA to find the first principal component of the length and width measurements of the grain samples, and represent it as an arrow on the scatter plot.
The array grains gives the length and width of the grain samples. PyPlot (plt) and PCA have already been imported for you.

### INSTRUCTIONS
100XP
Make a scatter plot of the grain measurements. This has been done for you.
Create a PCA instance called model.
Fit the model to the grains data.
Extract the coordinates of the mean of the data using the .mean_ attribute of model.
Get the first principal component of model using the .components_[0,:] attribute.
Plot the first principal component as an arrow on the scatter plot, using the plt.arrow() function. You have to specify the first two arguments - mean[0] and mean[1]

## Variance of the PCA features
The fish dataset is 6-dimensional. But what is its intrinsicdimension? Make a plot of the variances of the PCA features to find out. As before, samples is a 2D array, where each row represents a fish. You'll need to standardize the features first.
### INSTRUCTIONS
100XP
Create an instance of StandardScaler called scaler.
Create a PCA instance called pca.
Use the make_pipeline() function to create a pipeline chaining scaler and pca.
Use the .fit() method of pipeline to fit it to the fish samples samples.
Extract the number of components used using the .n_components_ attribute of pca. Place this inside a range() function and store the result as features.
Use the plt.bar() function to plot the explained variances, with features on the x-axis and pca.explained_variance_on the y-axis.
## Intrinsic dimension of the fish data
In the previous exercise, you plotted the variance of the PCA features of the fish measurements. Looking again at your plot, what do you think would be a reasonable choice for the "intrinsic dimension" of the the fish measurements? Recall that the intrinsic dimension is the number of PCA features with significant variance.

2
## Dimension reduction of the fish measurements
In a previous exercise, you saw that 2 was a reasonable choice for the "intrinsic dimension" of the fish measurements. Now use PCA for dimensionality reduction of the fish measurements, retaining only the 2 most important components.
The fish measurements have already been scaled for you, and are available as scaled_samples.

### INSTRUCTIONS
100XP
Import PCA from sklearn.decomposition.
Create a PCA instance called pca with n_components=2.
Use the .fit() method of pca to fit it to the scaled fish measurements scaled_samples.
Use the .transform() method of pca to transform the scaled_samples. Assign the result to pca_features.
## A tf-idf word-frequency array
In this exercise, you'll create a tf-idf word frequency array for a toy collection of documents. For this, use the TfidfVectorizerfrom sklearn. It transforms a list of documents into a word frequency array, which it outputs as a csr_matrix. It has fit()and transform() methods like other sklearn objects.
You are given a list documents of toy documents about pets. Its contents have been printed in the IPython Shell.
### INSTRUCTIONS
100XP
Import TfidfVectorizer from sklearn.feature_extraction.text.
Create a TfidfVectorizer instance called tfidf.
Apply .fit_transform() method of tfidf to documentsand assign the result to csr_mat. This is a word-frequency array in csr_matrix format.
Inspect csr_mat by calling its .toarray() method and printing the result. This has been done for you.
The columns of the array correspond to words. Get the list of words by calling the .get_feature_names() method of tfidf, and assign the result to words.

## Clustering Wikipedia part I
You saw in the video that TruncatedSVD is able to perform PCA on sparse arrays in csr_matrix format, such as word-frequency arrays. Combine your knowledge of TruncatedSVD and k-means to cluster some popular pages from Wikipedia. In this exercise, build the pipeline. In the next exercise, you'll apply it to the word-frequency array of some Wikipedia articles.
Create a Pipeline object consisting of a TruncatedSVD followed by KMeans. (This time, we've precomputed the word-frequency matrix for you, so there's no need for a TfidfVectorizer).
The Wikipedia dataset you will be working with was obtained from here.

### INSTRUCTIONS
100XP
Import:
TruncatedSVD from sklearn.decomposition.
KMeans from sklearn.cluster.
make_pipeline from sklearn.pipeline.
Create a TruncatedSVD instance called svd with n_components=50.
Create a KMeans instance called kmeans with n_clusters=6.
Create a pipeline called pipeline consisting of svd and kmeans.


## Clustering Wikipedia part II
It is now time to put your pipeline from the previous exercise to work! You are given an array articles of tf-idf word-frequencies of some popular Wikipedia articles, and a list titles of their titles. Use your pipeline to cluster the Wikipedia articles.
A solution to the previous exercise has been pre-loaded for you, so a Pipeline pipeline chaining TruncatedSVD with KMeans is available.

### INSTRUCTIONS
100XP
Import pandas as pd.
Fit the pipeline to the word-frequency array articles.
Predict the cluster labels.
Align the cluster labels with the list titles of article titles by creating a DataFrame df with labels and titles as columns. This has been done for you.
Use the .sort_values() method of df to sort the DataFrame by the 'label' column, and print the result.
Hit 'Submit Answer' and take a moment to investigate your amazing clustering of Wikipedia pages!

