# Chapter 4 Building a "fake news" classifier

## CountVectorizer for text classification
100xp
It's time to begin building your text classifier! The data has been loaded into a DataFrame called df. Explore it in the IPython Shell to investigate what columns you can use. The .head() method is particularly informative.
In this exercise, you'll use pandas alongside scikit-learn to create a sparse text vectorizer you can use to train and test a simple supervised model. To begin, you'll set up a CountVectorizer and investigate some of its features.
### Instructions
Import CountVectorizer from sklearn.feature_extraction.text and train_test_split from sklearn.model_selection.
Create a Series y to use for the labels by assigning the .label attribute of df to y.
Using df["text"] (features) and y (labels), create training and test sets using train_test_split(). Use a test_size of 0.33 and a random_state of 53.
Create a CountVectorizer object called count_vectorizer. Ensure you specify the keyword argument stop_words="english" so that stop words are removed.
Fit and transform the training data X_train using the .fit_transform() method. Do the same with the test data X_test, except using the .transform() method.
Print the first 10 features of the count_vectorizer using its .get_feature_names() method.

## TfidfVectorizer for text classification
100xp
Similar to the sparse CountVectorizer created in the previous exercise, you'll work on creating tf-idf vectors for your documents. You'll set up a TfidfVectorizer and investigate some of its features.
In this exercise, you'll use pandas and sklearn along with the same X_train, y_train and X_test, y_test DataFrames and Series you created in the last exercise.
### Instructions
Import TfidfVectorizer from sklearn.feature_extraction.text.
Create a TfidfVectorizer object called tfidf_vectorizer. When doing so, specify the keyword arguments stop_words="english" and max_df=0.7.
Fit and transform the training data.
Transform the test data.
Print the first 10 features of tfidf_vectorizer.
Print the first 5 vectors of the tfidf training data using slicing on the .A (or array) attribute of tfidf_train.

## Inspecting Vectors
100xp
To get a better idea of how the vectors work, you'll investigate them by converting them into pandas DataFrames.
Here, you'll use the same data structures you created in the previous two exercises (count_train, count_vectorizer, tfidf_train, tfidf_vectorizer) as well as pandas, which is imported as pd.
### Instructions
Create the DataFrames count_df and tfidf_df by using pd.DataFrame() and specifying the values as the first argument and the columns (or features) as the second argument.
The values can be accessed by using the .A attribute of, respectively, count_train and tfidf_train.
The columns can be accessed using the .get_feature_names() methods of count_vectorizer and tfidf_vectorizer.
Print the head of each DataFrame to investigate their structure.
Test if the column names are the same for each DataFrame by creating a new object called difference to see the difference between the columns that count_df has from tfidf_df. Columns can be accessed using the .columns attribute of a DataFrame. Subtract the set of tfidf_df.columns from the set of count_df.columns.
Test if the two DataFrames are equivalent by using the .equals() method on count_df with tfidf_df as the argument.

Text classification models
50xp
Which of the below is the most reasonable model to use when training a new supervised model using text vector data?
Possible Answers
Random Forests


Naive Bayes


Linear Regression


Deep Learning
## Training and testing the "fake news" model with CountVectorizer
100xp
Now it's your turn to train the "fake news" model using the features you identified and extracted. In this first exercise you'll train and test a Naive Bayes model using the CountVectorizer data.
The training and test sets have been created, and count_vectorizer, count_train, and count_test have been computed.
### Instructions
Import the metrics module from sklearn and MultinomialNB from sklearn.naive_bayes.
Instantiate a MultinomialNB classifier called nb_classifier.
Fit the classifier to the training data.
Compute the predicted tags for the test data.
Calculate and print the accuracy score of the classifier.
Compute the confusion matrix. To make it easier to read, specify the keyword argument labels=['FAKE', 'REAL'].


## Training and testing the "fake news" model with TfidfVectorizer
100xp
Now that you have evaluated the model using the CountVectorizer, you'll do the same using the TfidfVectorizer with a Naive Bayes model.
The training and test sets have been created, and tfidf_vectorizer, tfidf_train, and tfidf_test have been computed. Additionally, MultinomialNB and metrics have been imported from, respectively, sklearn.naive_bayes and sklearn.
### Instructions
Instantiate a MultinomialNB classifier called nb_classifier.
Fit the classifier to the training data.
Compute the predicted tags for the test data.
Calculate and print the accuracy score of the classifier.
Compute the confusion matrix. As in the previous exercise, specify the keyword argument labels=['FAKE', 'REAL'] so that the resulting confusion matrix is easier to read.

## Improving your model
100xp
Your job in this exercise is to test a few different alpha levels using the Tfidf vectors to determine if there is a better performing combination.
The training and test sets have been created, and tfidf_vectorizer, tfidf_train, and tfidf_test have been computed.
### Instructions
Create a list of alphas to try using np.arange(). Values should range from 0 to 1 with steps of 0.1.
Create a function train_and_predict() that takes in one argument: alpha. The function should:
Instantiate a MultinomialNBclassifier with alpha=alpha.
Fit it to the training data.
Compute predictions on the test data.
Compute and return the accuracy score.
Using a for loop, print the alpha, score and a newline in between. Use your train_and_predict() function to compute the score. Does the score change along with the alpha? What is the best alpha?

## Inspecting your model
100xp
Now that you have built a "fake news" classifier, you'll investigate what it has learned. You can map the important vector weights back to actual words using some simple inspection techniques.
You have your well performing tfidf Naive Bayes classifier available as nb_classifier, and the vectors as tfidf_vectorizer.
### Instructions
Save the class labels as class_labelsby accessing the .classes_ attribute of nb_classifier.
Extract the features using the .get_feature_names() method of tfidf_vectorizer.
Create a zipped array of the classifier coefficients with the feature names and sort them by the coefficients. To do this, first use zip() with the arguments nb_classifier.coef_[0] and feature_names. Then, use sorted() on this.
Print the top 20 weighted features for the first label of class_labels.
Print the bottom 20 weighted features for the second label of class_labels.

