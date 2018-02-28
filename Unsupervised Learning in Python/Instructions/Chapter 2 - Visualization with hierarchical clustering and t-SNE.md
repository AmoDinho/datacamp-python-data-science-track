# Chapter 2 - Visualization with hierarchical clustering and t-SNE


## Hierarchical clustering of the grain data
In the video, you learned that the SciPy linkage() function performs hierarchical clustering on an array of samples. Use the linkage() function to obtain a hierarchical clustering of the grain samples, and use dendrogram() to visualize the result. A sample of the grain measurements is provided in the array samples, while the variety of each grain sample is given by the list varieties.
### INSTRUCTIONS
100XP
Import:
linkage and dendrogram from scipy.cluster.hierarchy.
matplotlib.pyplot as plt.
Perform hierarchical clustering on samples using the linkage() function with the method='complete' keyword argument. Assign the result to mergings.
Plot a dendrogram using the dendrogram() function on mergings. Specify the keyword arguments labels=varieties, leaf_rotation=90, and leaf_font_size=6.


## Hierarchies of stocks
In chapter 1, you used k-means clustering to cluster companies according to their stock price movements. Now, you'll perform hierarchical clustering of the companies. You are given a NumPy array of price movements movements, where the rows correspond to companies, and a list of the company names companies. SciPy hierarchical clustering doesn't fit into a sklearn pipeline, so you'll need to use the normalize() function from sklearn.preprocessing instead of Normalizer.
linkage and dendrogram have already been imported from sklearn.cluster.hierarchy, and PyPlot has been imported as plt.
### INSTRUCTIONS
100XP
Import normalize from sklearn.preprocessing.
Rescale the price movements for each stock by using the normalize() function on movements.
Apply the linkage() function to normalized_movements, using 'complete' linkage, to calculate the hierarchical clustering. Assign the result to mergings.
Plot a dendrogram of the hierarchical clustering, using the list companies of company names as the labels. In addition, specify the leaf_rotation=90, and leaf_font_size=6keyword arguments as you did in the previous exercise.

## Which clusters are closest?
In the video, you learned that the linkage method defines how the distance between clusters is measured. In complete linkage, the distance between clusters is the distance between the furthest points of the clusters. In single linkage, the distance between clusters is the distance between the closest points of the clusters.
Consider the three clusters in the diagram. Which of the following statements are true?


A. In single linkage, cluster 3 is the closest to cluster 2.
B. In complete linkage, cluster 1 is the closest to cluster 2.


## Different linkage, different hierarchical clustering!
In the video, you saw a hierarchical clustering of the voting countries at the Eurovision song contest using 'complete'linkage. Now, perform a hierarchical clustering of the voting countries with 'single' linkage, and compare the resulting dendrogram with the one in the video. Different linkage, different hierarchical clustering!
You are given an array samples. Each row corresponds to a voting country, and each column corresponds to a performance that was voted for. The list country_names gives the name of each voting country. This dataset was obtained from Eurovision.

### INSTRUCTIONS
100XP
Import:
linkage and dendrogram from scipy.cluster.hierarchy.
matplotlib.pyplot as plt.
Perform hierarchical clustering on samples using the linkage() function with the method='single' keyword argument. Assign the result to mergings.
Plot a dendrogram of the hierarchical clustering, using the list country_names as the labels. In addition, specify the leaf_rotation=90, and leaf_font_size=6 keyword arguments as you have done earlier.

## Intermediate clusterings
Displayed on the right is the dendrogram for the hierarchical clustering of the grain samples that you computed earlier. If the hierarchical clustering were stopped at height 6 on the dendrogram, how many clusters would there be?


3

## Extracting the cluster labels
In the previous exercise, you saw that the intermediate clustering of the grain samples at height 6 has 3 clusters. Now, use the fcluster() function to extract the cluster labels for this intermediate clustering, and compare the labels with the grain varieties using a cross-tabulation.
The hierarchical clustering has already been performed and mergings is the result of the linkage() function. The list varieties gives the variety of each grain sample.

### INSTRUCTIONS
100XP
Import:
pandas as pd.
fcluster from scipy.cluster.hierarchy.
Perform a flat hierarchical clustering by using the fcluster()function on mergings. Specify a maximum height of 6 and the keyword argument criterion='distance'.
Create a DataFrame df with two columns named 'labels'and 'varieties', using labels and varieties, respectively, for the column values. This has been done for you.
Create a cross-tabulation ct between df['labels'] and df['varieties'] to count the number of times each grain variety coincides with each cluster label.
## t-SNE visualization of grain dataset
In the video, you saw t-SNE applied to the iris dataset. In this exercise, you'll apply t-SNE to the grain samples data and inspect the resulting t-SNE features using a scatter plot. You are given an array samples of grain samples and a list variety_numbersgiving the variety number of each grain sample.
### INSTRUCTIONS
100XP
Import TSNE from sklearn.manifold.
Create a TSNE instance called model with learning_rate=200.
Apply the .fit_transform() method of model to samples. Assign the result to tsne_features.
Select the column 0 of tsne_features. Assign the result to xs.
Select the column 1 of tsne_features. Assign the result to ys.
Make a scatter plot of the t-SNE features xs and ys. To color the points by the grain variety, specify the additional keyword argument c=variety_numbers.

## A t-SNE map of the stock market
t-SNE provides great visualizations when the individual samples can be labeled. In this exercise, you'll apply t-SNE to the company stock price data. A scatter plot of the resulting t-SNE features, labeled by the company names, gives you a map of the stock market! The stock price movements for each company are available as the array normalized_movements (these have already been normalized for you). The list companies gives the name of each company. PyPlot (plt) has been imported for you.

### INSTRUCTIONS
100XP
Import TSNE from sklearn.manifold.
Create a TSNE instance called model with learning_rate=50.
Apply the .fit_transform() method of model to normalized_movements. Assign the result to tsne_features.
Select column 0 and column 1 of tsne_features.
Make a scatter plot of the t-SNE features xs and ys. Specify the additional keyword argument alpha=0.5.
Code to label each point with its company name has been written for you using plt.annotate(), so just hit 'Submit Answer' to see the visualization!

