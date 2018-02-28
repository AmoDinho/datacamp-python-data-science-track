# Chapter 3 - Improving your model



## Instantiate pipeline
In order to make your life easier as you start to work with all of the data in your original DataFrame, df, it's time to turn to one of scikit-learn's most useful objects: the Pipeline.
For the next few exercises, you'll reacquaint yourself with pipelines and train a classifier on some synthetic (sample) data of multiple datatypes before using the same techniques on the main dataset.
The sample data is stored in the DataFrame, sample_df, which has three kinds of feature data: numeric, text, and numeric with missing values. It also has a label column with two classes, aand b.
In this exercise, your job is to instantiate a pipeline that trains using the numeric column of the sample data.

### INSTRUCTIONS
100XP
Import Pipeline from sklearn.pipeline.
Create training and test sets using the numeric data only. Do this by specifying sample_df[['numeric']] in train_test_split().
Instantiate a pipeline as pl by adding the classifier step. Use a name of 'clf' and the same classifier from Chapter 2: OneVsRestClassifier(LogisticRegression()).
Fit your pipeline to the training data and compute its accuracy to see it in action! Since this is toy data, you'll use the default scoring method for now. In the next chapter, you'll return to log loss scoring.

## Preprocessing text features
Here, you'll perform a similar preprocessing pipeline step, only this time you'll use the text column from the sample data.
To preprocess the text, you'll turn to CountVectorizer() to generate a bag-of-words representation of the data, as in Chapter 2. Using the default arguments, add a (step, transform) tuple to the steps list in your pipeline.
Make sure you select only the text column for splitting your training and test sets.
As usual, your sample_df is ready and waiting in the workspace.
### INSTRUCTIONS
100XP
Import CountVectorizer from sklearn.feature_extraction.text.
Create training and test sets by selecting the correct subset of sample_df: 'text'.
Add the 'CountVectorizer' step (with the name 'vec') to the correct position in the pipeline.
Fit the pipeline to the training data and compute its accuracy.

## Multiple types of processing: FunctionTransformer
The next two exercises will introduce new topics you'll need to make your pipeline truly excel.
Any step in the pipeline must be an object that implements the fit and transform methods. The FunctionTransformercreates an object with these methods out of any Python function that you pass to it. We'll use it to help select subsets of data in a way that plays nicely with pipelines.
You are working with numeric data that needs imputation, and text data that needs to be converted into a bag-of-words. You'll create functions that separate the text from the numeric variables and see how the .fit() and .transform() methods work.
### INSTRUCTIONS
100XP
Compute the selector get_text_data by using a lambda function and FunctionTransformer() to obtain all 'text'columns.
Compute the selector get_numeric_data by using a lambda function and FunctionTransformer() to obtain all the numeric columns (including missing data). These are 'numeric' and 'with_missing'.
Fit and transform get_text_data using the .fit_transform() method with sample_df as the argument.
Fit and transform get_numeric_data using the same approach as above.

## Multiple types of processing: FeatureUnion
Now that you can separate text and numeric data in your pipeline, you're ready to perform separate steps on each by nesting pipelines and using FeatureUnion().
These tools will allow you to streamline all preprocessing steps for your model, even when multiple datatypes are involved. Here, for example, you don't want to impute our text data, and you don't want to create a bag-of-words with our numeric data. Instead, you want to deal with these separately and then join the results together using FeatureUnion().
In the end, you'll still have only two high-level steps in your pipeline: preprocessing and model instantiation. The difference is that the first preprocessing step actually consists of a pipeline for numeric data and a pipeline for text data. The results of those pipelines are joined using FeatureUnion().

### INSTRUCTIONS
100XP
In the process_and_join_features:
Add the steps ('selector', get_numeric_data) and ('imputer', Imputer()) to the 'numeric_features'preprocessing step.
Add the equivalent steps for the text_featurespreprocessing step. That is, use get_text_data and a CountVectorizer step with the name 'vectorizer.
Add the transform step process_and_join_features to 'union' in the main pipeline, pl.
Hit 'Submit Answer' to see the pipeline in action!

## Using FunctionTransformer on the main dataset
In this exercise you're going to use FunctionTransformer on the primary budget data, before instantiating a multiple-datatype pipeline in the next exercise.
Recall from Chapter 2 that you used a custom function combine_text_columns to select and properly format text datafor tokenization; it is loaded into the workspace and ready to be put to work in a function transformer!
Concerning the numeric data, you can use NUMERIC_COLUMNS, preloaded as usual, to help design a subset-selecting lambda function.
You're all finished with sample data. The original df is back in the workspace, ready to use.
### INSTRUCTIONS
100XP
Complete the call to multilabel_train_test_split() by selecting df[NON_LABELS].
Compute get_text_data by using FunctionTransformer()and passing in combine_text_columns. Be sure to also specify validate=False.
Use FunctionTransformer() to compute get_numeric_data. In the lambda function, select out the NUMERIC_COLUMNS of x. Like you did when computing get_text_data, also specify validate=False.



## Add a model to the pipeline
You're about to take everything you've learned so far and implement it in a Pipeline that works with the real, DrivenData budget line item data you've been exploring.
Surprise! The structure of the pipeline is exactly the same as earlier in this chapter:
the preprocessing step uses FeatureUnion to join the results of nested pipelines that each rely on FunctionTransformer to select multiple datatypes
the model step stores the model object
You can then call familiar methods like .fit() and .score()on the Pipeline object pl.

### INSTRUCTIONS
100XP
Complete the 'numeric_features' transform with the following steps:
get_numeric_data, with the name 'selector'.
Imputer(), with the name 'imputer'.
Complete the 'text_features' transform with the following steps:
get_text_data, with the name 'selector'.
CountVectorizer(), with the name 'vectorizer'.
Fit the pipeline to the training data.
Hit 'Submit Answer' to compute the accuracy!

## Try a different class of model
Now you're cruising. One of the great strengths of pipelines is how easy they make the process of testing different models.
Until now, you've been using the model step ('clf', OneVsRestClassifier(LogisticRegression())) in your pipeline.
But what if you want to try a different model? Do you need to build an entirely new pipeline? New nests? New FeatureUnions? Nope! You just have a simple one-line change, as you'll see in this exercise.
In particular, you'll swap out the logistic-regression model and replace it with a random forest classifier, which uses the statistics of an ensemble of decision trees to generate predictions.

### INSTRUCTIONS
100XP
Import the RandomForestClassifier from sklearn.ensemble.
Add a RandomForestClassifier() step named 'clf' to the pipeline.
Hit 'Submit Answer' to fit the pipeline to the training data and compute its accuracy.
## Can you adjust the model or parameters to improve accuracy?
You just saw a substantial improvement in accuracy by swapping out the model. Pipelines are amazing!
Can you make it better? Try changing the parameter n_estimators of RandomForestClassifier(), whose default value is 10, to 15.

### INSTRUCTIONS
100XP
Import the RandomForestClassifier from sklearn.ensemble.
Add a RandomForestClassifier() step with n_estimators=15 to the pipeline with a name of 'clf'.
Hit 'Submit Answer' to fit the pipeline to the training data and compute its accuracy.


