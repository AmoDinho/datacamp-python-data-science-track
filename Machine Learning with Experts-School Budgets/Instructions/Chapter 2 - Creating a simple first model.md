# Chapter 2 - Creating a simple first model


## Setting up a train-test split in scikit-learn
Alright, you've been patient and awesome. It's finally time to start training models!
The first step is to split the data into a training set and a test set. Some labels don't occur very often, but we want to make sure that they appear in both the training and the test sets. We provide a function that will make sure at least min_countexamples of each label appear in each split: multilabel_train_test_split.
Feel free to check out the full code for multilabel_train_test_split here.
You'll start with a simple model that uses just the numeric columns of your DataFrame when calling multilabel_train_test_split. The data has been read into a DataFrame df and a list consisting of just the numeric columns is available as NUMERIC_COLUMNS.
### INSTRUCTIONS
100XP
Create a new DataFrame named numeric_data_only by applying the .fillna(-1000) method to the numeric columns (available in the list NUMERIC_COLUMNS) of df.
Convert the labels (available in the list LABELS) to dummy variables. Save the result as label_dummies.
In the call to multilabel_train_test_split(), set the sizeof your test set to be 0.2. Use a seed of 123.
Fill in the .info() method calls for X_train, X_test, y_train, and y_test.

## Training a model
With split data in hand, you're only a few lines away from training a model.
In this exercise, you will import the logistic regression and one versus rest classifiers in order to fit a multi-class logistic regression model to the NUMERIC_COLUMNS of your feature data.
Then you'll test and print the accuracy with the .score()method to see the results of training.
Before you train! Remember, we're ultimately going to be using logloss to score our model, so don't worry too much about the accuracy here. Keep in mind that you're throwing away all of the text data in the dataset - that's by far most of the data! So don't get your hopes up for a killer performance just yet. We're just interested in getting things up and running at the moment.
All data necessary to call multilabel_train_test_split() has been loaded into the workspace.
### INSTRUCTIONS
100XP
Import LogisticRegression from sklearn.linear_modeland OneVsRestClassifier from sklearn.multiclass.
Instantiate the classifier clf by placing LogisticRegression() inside OneVsRestClassifier().
Fit the classifier to the training data X_train and y_train.
Compute and print the accuracy of the classifier using its .score() method, which accepts two arguments: X_testand y_test.
## Use your model to predict values on holdout data
You're ready to make some predictions! Remember, the train-test-split you've carried out so far is for model development. The original competition provides an additional test set, for which you'll never actually see the correct labels. This is called the "holdout data."
The point of the holdout data is to provide a fair test for machine learning competitions. If the labels aren't known by anyone but DataCamp, DrivenData, or whoever is hosting the competition, you can be sure that no one submits a mere copy of labels to artificially pump up the performance on their model.
Remember that the original goal is to predict the probability of each label. In this exercise you'll do just that by using the .predict_proba() method on your trained model.
First, however, you'll need to load the holdout data, which is available in the workspace as the file HoldoutData.csv.
### INSTRUCTIONS
100XP
Read HoldoutData.csv into a DataFrame called holdout. Specify the keyword argument index_col=0 in your call to read_csv().
Generate predictions using .predict_proba() on the numeric columns (available in the NUMERIC_COLUMNS list) of holdout. Make sure to fill in missing values with -1000!

## Writing out your results to a csv for submission
At last, you're ready to submit some predictions for scoring. In this exercise, you'll write your predictions to a .csv using the .to_csv() method on a pandas DataFrame. Then you'll evaluate your performance according to the LogLoss metric discussed earlier!
You'll need to make sure your submission obeys the correct format.
To do this, you'll use your predictions values to create a new DataFrame, prediction_df.
Interpreting LogLoss & Beating the Benchmark:
When interpreting your log loss score, keep in mind that the score will change based on the number of samples tested. To get a sense of how this very basic model performs, compare your score to the DrivenData benchmark model performance: 2.0455, which merely submitted uniform probabilities for each class.
Remember, the lower the log loss the better. Is your model's log loss lower than 2.0455?
### INSTRUCTIONS
100XP
Create the prediction_df DataFrame by specifying the following arguments to the provided parameters pd.DataFrame():
pd.get_dummies(df[LABELS]).columns.
holdout.index.
predictions.
Save prediction_df to a csv file called 'predictions.csv'using the .to_csv() method.
Submit the predictions for scoring by using the score_submission() function with pred_path set to 'predictions.csv'.

## Creating a bag-of-words in scikit-learn
In this exercise, you'll study the effects of tokenizing in different ways by comparing the bag-of-words representations resulting from different token patterns.
You will focus on one feature only, the Position_Extra column, which describes any additional information not captured by the Position_Type label.
For example, in the Shell you can check out the budget item in row 8960 of the data using df.loc[8960]. Looking at the output reveals that this Object_Description is overtime pay. For who? The Position Type is merely "other", but the Position Extra elaborates: "BUS DRIVER". Explore the column further to see more instances. It has a lot of NaN values.
Your task is to turn the raw text in this column into a bag-of-words representation by creating tokes that contain onlyalphanumeric characters.
For comparison purposes, the first 15 tokens of vec_basic, which splits df.Position_Extra into tokens when it encounters only whitespace characters, have been printed along with the length of the representation.

### INSTRUCTIONS
100XP
Import CountVectorizer from sklearn.feature_extraction.text.
Fill missing values in df.Position_Extra using .fillna('')to replace NaNs with empty strings. Specify the additional keyword argument inplace=True so that you don't have to assign the result back to df.
Instantiate the CountVectorizer as vec_alphanumeric by specifying the token_pattern to be TOKENS_ALPHANUMERIC.
Fit vec_alphanumeric to df.Position_Extra.
Hit 'Submit Answer' to see the len of the fitted representation as well as the first 15 elements, and compare to vec_basic.

## Combining text columns for tokenization
In order to get a bag-of-words representation for all of the text data in our DataFrame, you must first convert the text data in each row of the DataFrame into a single string.
In the previous exercise, this wasn't necessary because you only looked at one column of data, so each row was already just a single string. CountVectorizer expects each row to just be a single string, so in order to use all of the text columns, you'll need a method to turn a list of strings into a single string.
In this exercise, you'll complete the function definition combine_text_columns(). When completed, this function will convert all training text data in your DataFrame to a single string per row that can be passed to the vectorizer object and made into a bag-of-words using the .fit_transform() method.
Note that the function uses NUMERIC_COLUMNS and LABELS to determine which columns to drop. These lists have been loaded into the workspace.
### INSTRUCTIONS
100XP
Use the .drop() method on data_frame with to_drop and axis= as arguments to drop the non-text data. Save the result as text_data.
Fill in missing values (inplace) in text_data with blanks (""), using the .fillna() method.
Complete the .apply() method by writing a lambda function that uses the .join() method to join all the items in a row with a space in between.


## What's in a token?
Now you will use combine_text_columns to convert all training text data in your DataFrame to a single vector that can be passed to the vectorizer object and made into a bag-of-words using the .fit_transform() method.
You'll compare the effect of tokenizing using any non-whitespace characters as a token and using only alphanumeric characters as a token.
### INSTRUCTIONS
100XP
Import CountVectorizer from sklearn.feature_extraction.text.
Instantiate vec_basic and vec_alphanumeric using, respectively, the TOKENS_BASIC and TOKENS_ALPHANUMERICpatterns.
Create the text vector by using the combine_text_columns()function on df.
Using the .fit_transform() method with text_vector, fit and transform first vec_basic and then vec_alphanumeric. Print the number of tokens they contain.



