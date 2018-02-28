#------------------------------------------------------------------------------------------------------------#
#Chapter 2 - Visualization with hierarchical clustering and t-SNE






#------------------------------------------------------------------------------------------------------------#
#Hierarchical clustering of the grain data

# Perform the necessary imports
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Calculate the linkage: mergings
mergings = linkage(samples, method='complete')

# Plot the dendrogram, using varieties as labels
dendrogram(mergings,
           labels=varieties,
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()

#------------------------------------------------------------------------------------------------------------#

#Hierarchies of stocks
# Import normalize
from sklearn.preprocessing import normalize

# Normalize the movements: normalized_movements
normalized_movements = normalize(movements)

# Calculate the linkage: mergings
mergings = linkage(normalized_movements, method='complete')

# Plot the dendrogram
dendrogram(mergings,
           labels=companies,
           leaf_rotation=90,
           leaf_font_size=6,
)

plt.show()


#------------------------------------------------------------------------------------------------------------#
#Different linkage, different hierarchical clustering!
# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Calculate the linkage: mergings
mergings = linkage(samples,method='single')

# Plot the dendrogram
dendrogram(mergings,
           labels=country_names,
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.xlabel('European Nations')
plt.ylabel('Number of votes')
plt.title('EuroVision 2017 Denogram ')
plt.legend(loc='upper right')
plt.show()




#------------------------------------------------------------------------------------------------------------#

#Extracting the cluster labels
# Perform the necessary imports
import pandas as pd
from scipy.cluster.hierarchy import fcluster

# Use fcluster to extract labels: labels
labels = fcluster(mergings,6,criterion='distance')

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
ct = pd.crosstab(df['labels'],df['varieties'])

# Display ct
print(ct)


#------------------------------------------------------------------------------------------------------------#
#t-SNE visualization of grain dataset
# Import TSNE
from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=200)

# Apply fit_transform to samples: tsne_features
tsne_features = model.fit_transform(samples)

# Select the 0th feature: xs
xs = tsne_features[:,0]

# Select the 1st feature: ys
ys = tsne_features[:,1]

# Scatter plot, coloring by variety_numbers
plt.scatter(xs,ys,c=variety_numbers)
plt.show()




#------------------------------------------------------------------------------------------------------------#
#A t-SNE map of the stock market

# Import TSNE
from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=50)

# Apply fit_transform to normalized_movements: tsne_features
tsne_features = model.fit_transform(normalized_movements)

# Select the 0th feature: xs
xs = tsne_features[:,0]

# Select the 1th feature: ys
ys = tsne_features[:,1]

# Scatter plot
plt.scatter(xs,ys,alpha=0.5)

# Annotate the points
for x, y, company in zip(xs, ys, companies):
    plt.annotate(company, (x, y), fontsize=5, alpha=0.75)
plt.show()


#------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------#



#------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------#



#------------------------------------------------------------------------------------------------------------#




#------------------------------------------------------------------------------------------------------------#





#------------------------------------------------------------------------------------------------------------#





#------------------------------------------------------------------------------------------------------------#





#------------------------------------------------------------------------------------------------------------#





#------------------------------------------------------------------------------------------------------------#