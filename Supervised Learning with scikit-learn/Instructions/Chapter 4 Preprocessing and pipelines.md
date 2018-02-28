# Chapter 4 Preprocessing and pipelines

## Exploring categorical features
0xp
The Gapminder dataset that you worked with in previous chapters also contained a categorical 'Region' feature, which we dropped in previous exercises since you did not have the tools to deal with it. Now however, you do, so we have added it back in!
Your job in this exercise is to explore this feature. Boxplots are particularly useful for visualizing categorical features such as this.
### Instructions
Import pandas as pd.
Read the CSV file 'gapminder.csv' into a DataFrame called df.
Use pandas to create a boxplot showing the variation of life expectancy ('life') by region ('Region'). To do so, pass the column names in to df.boxplot() (in that order).

## Creating dummy variables
100xp
As Andy discussed in the video, scikit-learn does not accept non-numerical features. You saw in the previous exercise that the 'Region'feature contains very useful information that can predict life expectancy. For example, Sub-Saharan Africa has a lower life expectancy compared to Europe and Central Asia. Therefore, if you are trying to predict life expectancy, it would be preferable to retain the 'Region' feature. To do this, you need to binarize it by creating dummy variables, which is what you will do in this exercise.
### Instructions
Use the pandas get_dummies() function to create dummy variables from the df DataFrame. Store the result as df_region.
Print the columns of df_region. This has been done for you.
Use the get_dummies() function again, this time specifying drop_first=True to drop the unneeded dummy variable (in this case, 'Region_America').
Hit 'Submit Answer to print the new columns of df_regionand take note of how one column was dropped!
## Regression with categorical features
100xp
Having created the dummy variables from the 'Region' feature, you can build regression models as you did before. Here, you'll use ridge regression to perform 5-fold cross-validation.
The feature array X and target variable array y have been pre-loaded.
### Instructions
Import Ridge from sklearn.linear_model and cross_val_score from sklearn.model_selection.
Instantiate a ridge regressor called ridge with alpha=0.5 and normalize=True.
Perform 5-fold cross-validation on X and y using the cross_val_score() function.
Print the cross-validated scores.

## Dropping missing data
100xp
The voting dataset from Chapter 1 contained a bunch of missing values that we dealt with for you behind the scenes. Now, it's time for you to take care of these yourself!
The unprocessed dataset has been loaded into a DataFrame df. Explore it in the IPython Shell with the .head() method. You will see that there are certain data points labeled with a '?'. These denote missing values. As you saw in the video, different datasets encode missing values in different ways. Sometimes it may be a '9999', other times a 0 - real-world data can be very messy! If you're lucky, the missing values will already be encoded as NaN. We use NaN because it is an efficient and simplified way of internally representing missing data, and it lets us take advantage of pandas methods such as .dropna() and .fillna(), as well as scikit-learn's Imputation transformer Imputer().
In this exercise, your job is to convert the '?'s to NaNs, and then drop the rows that contain them from the DataFrame.
### Instructions
Explore the DataFrame df in the IPython Shell. Notice how the missing value is represented.
Convert all '?' data points to np.nan.
Count the total number of NaNs using the .isnull()and .sum() methods. This has been done for you.
Drop the rows with missing values from df using .dropna().
Hit 'Submit Answer' to see how many rows were lost by dropping the missing values.


## Imputing missing data in a ML Pipeline I
100xp
As you've come to appreciate, there are many steps to building a model, from creating training and test sets, to fitting a classifier or regressor, to tuning its parameters, to evaluating its performance on new data. Imputation can be seen as the first step of this machine learning process, the entirety of which can be viewed within the context of a pipeline. Scikit-learn provides a pipeline constructor that allows you to piece together these steps into one process and thereby simplify your workflow.
You'll now practice setting up a pipeline with two steps: the imputation step, followed by the instantiation of a classifier. You've seen three classifiers in this course so far: k-NN, logistic regression, and the decision tree. You will now be introduced to a fourth one - the Support Vector Machine, or SVM. For now, do not worry about how it works under the hood. It works exactly as you would expect of the scikit-learn estimators that you have worked with previously, in that it has the same .fit() and .predict() methods as before.
### Instructions
Import Imputer from sklearn.preprocessing and SVC from sklearn.svm. SVC stands for Support Vector Classification, which is a type of SVM.
Setup the Imputation transformer to impute missing data (represented as 'NaN') with the 'most_frequent'value in the column (axis=0).
Instantiate a SVC classifier. Store the result in clf.
Create the steps of the pipeline by creating a list of tuples:
The first tuple should consist of the imputation step, using imp.
The second should consist of the classifier.



## Imputing missing data in a ML Pipeline II
100xp
Having setup the steps of the pipeline in the previous exercise, you will now use it on the voting dataset to classify a Congressman's party affiliation. What makes pipelines so incredibly useful is the simple interface that they provide. You can use the .fit() and .predict() methods on pipelines just as you did with your classifiers and regressors!
Practice this for yourself now and generate a classification report of your predictions. The steps of the pipeline have been set up for you, and the feature array X and target variable array y have been pre-loaded. Additionally, train_test_split and classification_report have been imported from sklearn.model_selection and sklearn.metrics respectively.
### Instructions
Import the following modules:
Imputer from sklearn.preprocessing and Pipeline from sklearn.pipeline.
SVC from sklearn.svm.
Create the pipeline using Pipeline() and steps.
Create training and test sets. Use 30% of the data for testing and a random state of 42.
Fit the pipeline to the training set and predict the labels of the test set.
Compute the classification report.


## Centering and scaling your data
100xp
In the video, Hugo demonstrated how significantly the performance of a model can improve if the features are scaled. Note that this is not always the case: In the Congressional voting records dataset, for example, all of the features are binary. In such a situation, scaling will have minimal impact.
You will now explore scaling for yourself on a new dataset - White Wine Quality! Hugo used the Red Wine Quality dataset in the video. We have used the 'quality' feature of the wine to create a binary target variable: If 'quality' is less than 5, the target variable is 1, and otherwise, it is 0.
The DataFrame has been pre-loaded as df, along with the feature and target variable arrays X and y. Explore it in the IPython Shell. Notice how some features seem to have different units of measurement. 'density', for instance, only takes values between 0 and 1, while 'total sulfur dioxide' has a maximum value of 289. As a result, it may be worth scaling the features here. Your job in this exercise is to scale the features and compute the mean and standard deviation of the unscaled features compared to the scaled features.
### Instructions
Import scale from sklearn.preprocessing.
Scale the features X using scale().
Print the mean and standard deviation of the unscaled features X, and then the scaled features X_scaled. Use the numpy functions np.mean() and np.std()to compute the mean and standard deviations.

## Centering and scaling in a pipeline
100xp
With regard to whether or not scaling is effective, the proof is in the pudding! See for yourself whether or not scaling the features of the White Wine Quality dataset has any impact on its performance. You will use a k-NN classifier as part of a pipeline that includes scaling, and for the purposes of comparison, a k-NN classifier trained on the unscaled data has been provided.
The feature array and target variable array have been pre-loaded as Xand y. Additionally, KNeighborsClassifier and train_test_split have been imported from sklearn.neighbors and sklearn.model_selection, respectively.
### Instructions
Import the following modules:
StandardScaler from sklearn.preprocessing.
Pipeline from sklearn.pipeline.
Complete the steps of the pipeline with StandardScaler() for 'scaler' and KNeighborsClassifier() for 'knn'.
Create the pipeline using Pipeline() and steps.
Create training and test sets, with 30% used for testing. Use a random state of 42.
Fit the pipeline to the training set.
Compute the accuracy scores of the scaled and unscaled models by using the .score() method inside the provided print() functions.

## Bringing it all together I: Pipeline for classification
100xp
It is time now to piece together everything you have learned so far into a pipeline for classification! Your job in this exercise is to build a pipeline that includes scaling and hyperparameter tuning to classify wine quality.
You'll return to using the SVM classifier you were briefly introduced to earlier in this chapter. The hyperparameters you will tune are CC and gammagamma. CC controls the regularization strength. It is analogous to the CC you tuned for logistic regression in Chapter 3, while gammagammacontrols the kernel coefficient: Do not worry about this now as it is beyond the scope of this course.
The following modules have been pre-loaded: Pipeline, svm, train_test_split, GridSearchCV, classification_report, accuracy_score. The feature and target variable arrays X and y have also been pre-loaded.
### Instructions
Setup the pipeline with the following steps:
Scaling, called 'scaler' with StandardScaler().
Classification, called 'SVM' with SVC().
Specify the hyperparameter space using the following notation: 'step_name__parameter_name'. Here, the step_name is SVM, and the parameter_names are C and gamma.
Create training and test sets, with 20% of the data used for the test set. Use a random state of 21.
Instantiate GridSearchCV with the pipeline and hyperparameter space and fit it to the training set. Use 3-fold cross-validation (This is the default, so you don't have to specify it).
Predict the labels of the test set and compute the metrics. The metrics have been computed for you.

## Bringing it all together II: Pipeline for regression
100xp
For this final exercise, you will return to the Gapminder dataset. Guess what? Even this dataset has missing values that we dealt with for you in earlier chapters! Now, you have all the tools to take care of them yourself!
Your job is to build a pipeline that imputes the missing data, scales the features, and fits an ElasticNet to the Gapminder data. You will then tune the l1_ratio of your ElasticNet using GridSearchCV.
All the necessary modules have been imported, and the feature and target variable arrays have been pre-loaded as X and y.
### Instructions
Set up a pipeline with the following steps:
'imputation', which uses the Imputer()transformer and the 'mean' strategy to impute missing data ('NaN') using the mean of the column.
'scaler', which scales the features using StandardScaler().
'elasticnet', which instantiates an ElasticNet regressor.
Specify the hyperparameter space for the l1l1 ratio using the following notation: 'step_name__parameter_name'. Here, the step_name is elasticnet, and the parameter_name is l1_ratio.
Create training and test sets, with 40% of the data used for the test set. Use a random state of 42.
Instantiate GridSearchCV with the pipeline and hyperparameter space. Use 3-fold cross-validation (This is the default, so you don't have to specify it).
Fit the GridSearchCV object to the training set.
Compute R2R2 and the best parameters. This has been done for you, so hit 'Submit Answer' to see the results!

