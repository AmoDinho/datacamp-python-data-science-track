# Chapter 4 - Discovering interpretable features
## Non-negative data
Which of the following 2-dimensional arrays are examples of non-negative data?
A tf-idf word-frequency array.
An array daily stock market price movements (up and down), where each row represents a company.
An array where rows are customers, columns are products and entries are 0 or 1, indicating whether a customer has purchased a product.

## NMF applied to Wikipedia articles
In the video, you saw NMF applied to transform a toy word-frequency array. Now it's your turn to apply NMF, this time using the tf-idf word-frequency array of Wikipedia articles, given as a csr matrix articles. Here, fit the model and transform the articles. In the next exercise, you'll explore the result.
### INSTRUCTIONS
100XP
Import NMF from sklearn.decomposition.
Create an NMF instance called model with 6 components.
Fit the model to the word count data articles.
Use the .transform() method of model to transform articles, and assign the result to nmf_features.
Print nmf_features to get a first idea what it looks like.

## NMF features of the Wikipedia articles
Now you will explore the NMF features you created in the previous exercise. A solution to the previous exercise has been pre-loaded, so the array nmf_features is available. Also available is a list titles giving the title of each Wikipedia article.
When investigating the features, notice that for both actors, the NMF feature 3 has by far the highest value. This means that both articles are reconstructed using mainly the 3rd NMF component. In the next video, you'll see why: NMF components represent topics (for instance, acting!).
### INSTRUCTIONS
100XP
Import pandas as pd.
Create a DataFrame df from nmf_features using pd.DataFrame(). Set the index to titles using index=titles.
Use the .loc[] accessor of df to select the row with title 'Anne Hathaway', and print the result. These are the NMF features for the article about the actress Anne Hathaway.
Repeat the last step for 'Denzel Washington' (another actor).

## NMF reconstructs samples
In this exercise, you'll check your understanding of how NMF reconstructs samples from its components using the NMF feature values. On the right are the components of an NMF model. If the NMF feature values of a sample are [2, 1], then which of the following is most likely to represent the original sample? A pen and paper will help here! You have to apply the same technique Ben used in the video to reconstruct the sample [0.1203 0.1764 0.3195 0.141]
[2.2, 1.0, 2.0].

## NMF learns topics of documents
In the video, you learned when NMF is applied to documents, the components correspond to topics of documents, and the NMF features reconstruct the documents from the topics. Verify this for yourself for the NMF model that you built earlier using the Wikipedia articles. Previously, you saw that the 3rd NMF feature value was high for the articles about actors Anne Hathaway and Denzel Washington. In this exercise, identify the topic of the corresponding NMF component.
The NMF model you built earlier is available as model, while words is a list of the words that label the columns of the word-frequency array.
After you are done, take a moment to recognise the topic that the articles about Anne Hathaway and Denzel Washington have in common!
### INSTRUCTIONS
100XP
Import pandas as pd.
Create a DataFrame components_df from model.components_, setting columns=words so that columns are labeled by the words.
Print components_df.shape to check the dimensions of the DataFrame.
Use the .iloc[] accessor on the DataFrame components_dfto select row 3. Assign the result to component.
Call the .nlargest() method of component, and print the result. This gives the five words with the highest values for that component.

## Explore the LED digits dataset
In the following exercises, you'll use NMF to decompose grayscale images into their commonly occurring patterns. Firstly, explore the image dataset and see how it is encoded as an array. You are given 100 images as a 2D array samples, where each row represents a single 13x8 image. The images in your dataset are pictures of a LED digital display.

### INSTRUCTIONS
100XP
Import matplotlib.pyplot as plt.
Select row 0 of samples and assign the result to digit. For example, to select column 2 of an array a, you could use a[:,2]. Remember that since samples is a NumPy array, you can't use the .loc[] or iloc[] accessors to select specific rows or columns.
Print digit. This has been done for you. Notice that it is a 1D array of 0s and 1s.
Use the .reshape() method of digit to get a 2D array with shape (13, 8). Assign the result to bitmap.
Print bitmap, and notice that the 1s show the digit 7!
Use the plt.imshow() function to display bitmap as an image.

## NMF learns the parts of images
Now use what you've learned about NMF to decompose the digits dataset. You are again given the digit images as a 2D array samples. This time, you are also provided with a function show_as_image() that displays the image encoded by any 1D array:
def show_as_image(sample):
    bitmap = sample.reshape((13, 8))
    plt.figure()
    plt.imshow(bitmap, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.show()


After you are done, take a moment to look through the plots and notice how NMF has expressed the digit as a sum of the components!
 
### INSTRUCTIONS
100XP
Import NMF from sklearn.decomposition.
Create an NMF instance called model with 7 components. (7 is the number of cells in an LED display).
Apply the .fit_transform() method of model to samples. Assign the result to features.
To each component of the model (accessed via model.components_), apply the show_as_image() function to that component inside the loop.
Assign the row 0 of features to digit_features.
Print digit_features.

## PCA doesn't learn parts
Unlike NMF, PCA doesn't learn the parts of things. Its components do not correspond to topics (in the case of documents) or to parts of images, when trained on images. Verify this for yourself by inspecting the components of a PCA model fit to the dataset of LED digit images from the previous exercise. The images are available as a 2D array samples. Also available is a modified version of the show_as_image() function which colors a pixel red if the value is negative.
After submitting the answer, notice that the components of PCA do not represent meaningful parts of images of LED digits!
### INSTRUCTIONS
100XP
Import PCA from sklearn.decomposition.
Create a PCA instance called model with 7 components.
Apply the .fit_transform() method of model to samples. Assign the result to features.
To each component of the model (accessed via model.components_), apply the show_as_image() function to that component inside the loop.


## Which articles are similar to 'Cristiano Ronaldo'?
In the video, you learned how to use NMF features and the cosine similarity to find similar articles. Apply this to your NMF model for popular Wikipedia articles, by finding the articles most similar to the article about the footballer Cristiano Ronaldo. The NMF features you obtained earlier are available as nmf_features, while titles is a list of the article titles.
INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import normalize from sklearn.preprocessing.
Apply the normalize() function to nmf_features. Store the result as norm_features.
Create a DataFrame df from norm_features, using titles as an index.
Use the .loc[] accessor of df to select the row of 'Cristiano Ronaldo'. Assign the result to article.
Apply the .dot() method of df to article to calculate the cosine similarity of every row with article.
Print the result of the .nlargest() method of similaritiesto display the most similiar articles. This has been done for you, so hit 'Submit Answer' to see the result!

## Recommend musical artists part I
In this exercise and the next, you'll use what you've learned about NMF to recommend popular music artists! You are given a sparse array artists whose rows correspond to artists and whose column correspond to users. The entries give the number of times each artist was listened to by each user.
In this exercise, build a pipeline and transform the array into normalized NMF features. The first step in the pipeline, MaxAbsScaler, transforms the data so that all users have the same influence on the model, regardless of how many different artists they've listened to. In the next exercise, you'll use the resulting normalized NMF features for recommendation!
This data is part of a larger dataset available here.
### INSTRUCTIONS
100XP
Import:
NMF from sklearn.decomposition.
Normalizer and MaxAbsScaler from sklearn.preprocessing.
make_pipeline from sklearn.pipeline.
Create an instance of MaxAbsScaler called scaler.
Create an NMF instance with 20 components called nmf.
Create an instance of Normalizer called normalizer.
Create a pipeline called pipeline that chains together scaler, nmf, and normalizer.
Apply the .fit_transform() method of pipeline to artists. Assign the result to norm_features.
## Recommend musical artists part II
Suppose you were a big fan of Bruce Springsteen - which other musicial artists might you like? Use your NMF features from the previous exercise and the cosine similarity to find similar musical artists. A solution to the previous exercise has been run, so norm_features is an array containing the normalized NMF features as rows. The names of the musical artists are available as the list artist_names.

### INSTRUCTIONS
100XP
Import pandas as pd.
Create a DataFrame df from norm_features, using artist_names as an index.
Use the .loc[] accessor of df to select the row of 'Bruce Springsteen'. Assign the result to artist.
Apply the .dot() method of df to artist to calculate the dot product of every row with artist. Save the result as similarities.
Print the result of the .nlargest() method of similaritiesto display the artists most similar to 'Bruce Springsteen'

