# Chapter 3 Fine-tuning your model

## Metrics for classification
100xp
In Chapter 1, you evaluated the performance of your k-NN classifier based on its accuracy. However, as Andy discussed, accuracy is not always an informative metric. In this exercise, you will dive more deeply into evaluating the performance of binary classifiers by computing a confusion matrix and generating a classification report.
You may have noticed in the video that the classification report consisted of three rows, and an additional support column. The supportgives the number of samples of the true response that lie in that class - so in the video example, the support was the number of Republicans or Democrats in the test set on which the classification report was computed. The precision, recall, and f1-score columns, then, gave the respective metrics for that particular class.
Here, you'll work with the PIMA Indians dataset obtained from the UCI Machine Learning Repository. The goal is to predict whether or not a given female patient will contract diabetes based on features such as BMI, age, and number of pregnancies. Therefore, it is a binary classification problem. A target value of 0 indicates that the patient does not have diabetes, while a value of 1 indicates that the patient does have diabetes. As in Chapters 1 and 2, the dataset has been preprocessed to deal with missing values.
The dataset has been loaded into a DataFrame df and the feature and target variable arrays X and y have been created for you. In addition, sklearn.model_selection.train_test_split and sklearn.neighbors.KNeighborsClassifier have already been imported.
Your job is to train a k-NN classifier to the data and evaluate its performance by generating a confusion matrix and classification report.
### Instructions
Import classification_report and confusion_matrix from sklearn.metrics.
Create training and testing sets with 40% of the data used for testing. Use a random state of 42.
Instantiate a k-NN classifier with 6 neighbors, fit it to the training data, and predict the labels of the test set.
Compute and print the confusion matrix and classification report using the confusion_matrix() and classification_report() functions.

## Building a logistic regression model
100xp
Time to build your first logistic regression model! As Hugo showed in the video, scikit-learn makes it very easy to try different models, since the Train-Test-Split/Instantiate/Fit/Predict paradigm applies to all classifiers and regressors - which are known in scikit-learn as 'estimators'. You'll see this now for yourself as you train a logistic regression model on exactly the same data as in the previous exercise. Will it outperform k-NN? There's only one way to find out!
The feature and target variable arrays X and y have been pre-loaded, and train_test_split has been imported for you from sklearn.model_selection.
### Instructions
Import:
LogisticRegression from sklearn.linear_model.
confusion_matrix and classification_report from sklearn.metrics.
Create training and test sets with 40% (or 0.4) of the data used for testing. Use a random state of 42. This has been done for you.
Instantiate a LogisticRegression classifier called logreg.
Fit the classifier to the training data and predict the labels of the test set.
Compute and print the confusion matrix and classification report. This has been done for you, so hit 'Submit Answer' to see how logistic regression compares to k-NN!

## Plotting an ROC curve
100xp
Great job in the previous exercise - you now have a new addition to your toolbox of classifiers!
Classification reports and confusion matrices are great methods to quantitatively evaluate model performance, while ROC curves provide a way to visually evaluate models. As Hugo demonstrated in the video, most classifiers in scikit-learn have a .predict_proba() method which returns the probability of a given sample being in a particular class. Having built a logistic regression model, you'll now evaluate its performance by plotting an ROC curve. In doing so, you'll make use of the .predict_proba() method and become familiar with its functionality.
Here, you'll continue working with the PIMA Indians diabetes dataset. The classifier has already been fit to the training data and is available as logreg.
### Instructions
Import roc_curve from sklearn.metrics.
Using the logreg classifier, which has been fit to the training data, compute the predicted probabilities of the labels of the test set X_test. Save the result as y_pred_prob.
Use the roc_curve() function with y_test and y_pred_prob and unpack the result into the variables fpr, tpr, and thresholds.
Plot the ROC curve with fpr on the x-axis and tpr on the y-axis.


## AUC computation
100xp
Say you have a binary classifier that in fact is just randomly making guesses. It would be correct approximately 50% of the time, and the resulting ROC curve would be a diagonal line in which the True Positive Rate and False Positive Rate are always equal. The Area under this ROC curve would be 0.5. This is one way in which the AUC, which Hugo discussed in the video, is an informative metric to evaluate a model. If the AUC is greater than 0.5, the model is better than random guessing. Always a good sign!
In this exercise, you'll calculate AUC scores using the roc_auc_score() function from sklearn.metrics as well as by performing cross-validation on the diabetes dataset.
Training and test sets X_train, X_test, y_train, y_testhave been pre-loaded for you, and a logistic regression classifier logreg has been fit to the training data.
### Instructions
Import roc_auc_score from sklearn.metrics and cross_val_score from sklearn.model_selection.
Using the logreg classifier, which has been fit to the training data, compute the predicted probabilities of the labels of the test set X_test. Save the result as y_pred_prob.
Compute the AUC score using the roc_auc_score()function, the test set labels y_test, and the predicted probabilities y_pred_prob.
Compute the AUC scores by performing 5-fold cross-validation. Use the cross_val_score() function and specify the scoring parameter to be 'roc_auc'.


## Hyperparameter tuning with GridSearchCV
100xp
Hugo demonstrated how to use to tune the n_neighbors parameter of the KNeighborsClassifier() using GridSearchCV on the voting dataset. You will now practice this yourself, but by using logistic regression on the diabetes dataset instead!
Like the alpha parameter of lasso and ridge regularization that you saw earlier, logistic regression also has a regularization parameter: CC. CCcontrols the inverse of the regularization strength, and this is what you will tune in this exercise. A large CC can lead to an overfit model, while a small CC can lead to an underfit model.
The hyperparameter space for CC has been setup for you. Your job is to use GridSearchCV and logistic regression to find the optimal CC in this hyperparameter space. The feature array is available as X and target variable array is available as y.
You may be wondering why you aren't asked to split the data into training and test sets. Good observation! Here, we want you to focus on the process of setting up the hyperparameter grid and performing grid-search cross-validation. In practice, you will indeed want to hold out a portion of your data for evaluation purposes, and you will learn all about this in the next video!
### Instructions
Import LogisticRegression from sklearn.linear_model and GridSearchCV from sklearn.model_selection.
Setup the hyperparameter grid by using c_space as the grid of values to tune CC over.
Instantiate a logistic regression classifier called logreg.
Use GridSearchCV with 5-fold cross-validation to tune CC:
Inside GridSearchCV(), specify the classifier, parameter grid, and number of folds to use.
Use the .fit() method on the GridSearchCVobject to fit it to the data X and y.
Print the best parameter and best score obtained from GridSearchCV by accessing the best_params_ and best_score_ attributes of logreg_cv.


## Hyperparameter tuning with RandomizedSearchCV
100xp
GridSearchCV can be computationally expensive, especially if you are searching over a large hyperparameter space and dealing with multiple hyperparameters. A solution to this is to use RandomizedSearchCV, in which not all hyperparameter values are tried out. Instead, a fixed number of hyperparameter settings is sampled from specified probability distributions. You'll practice using RandomizedSearchCVin this exercise and see how this works.
Here, you'll also be introduced to a new model: the Decision Tree. Don't worry about the specifics of how this model works. Just like k-NN, linear regression, and logistic regression, decision trees in scikit-learn have .fit() and .predict() methods that you can use in exactly the same way as before. Decision trees have many parameters that can be tuned, such as max_features, max_depth, and min_samples_leaf: This makes it an ideal use case for RandomizedSearchCV.
As before, the feature array X and target variable array y of the diabetes dataset have been pre-loaded. The hyperparameter settings have been specified for you. Your goal is to use RandomizedSearchCV to find the optimal hyperparameters. Go for it!
### Instructions
Import DecisionTreeClassifier from sklearn.tree and RandomizedSearchCV from sklearn.model_selection.
Specify the parameters and distributions to sample from. This has been done for you.
Instantiate a DecisionTreeClassifier.
Use RandomizedSearchCV with 5-fold cross-validation to tune the hyperparameters:
Inside RandomizedSearchCV(), specify the classifier, parameter distribution, and number of folds to use.
Use the .fit() method on the RandomizedSearchCV object to fit it to the data X and y.
Print the best parameter and best score obtained from RandomizedSearchCV by accessing the best_params_ and best_score_ attributes of tree_cv.


## Hold-out set in practice I: Classification
100xp
You will now practice evaluating a model with tuned hyperparameters on a hold-out set. The feature array and target variable array from the diabetes dataset have been pre-loaded as X and y.
In addition to CC, logistic regression has a 'penalty'hyperparameter which specifies whether to use 'l1' or 'l2'regularization. Your job in this exercise is to create a hold-out set, tune the 'C' and 'penalty' hyperparameters of a logistic regression classifier using GridSearchCV on the training set, and then evaluate its performance against the hold-out set.
### Instructions
Create the hyperparameter grid:
Use the array c_space as the grid of values for 'C'.
For 'penalty', specify a list consisting of 'l1'and 'l2'.
Instantiate a logistic regression classifier.
Create training and test sets. Use a test_size of 0.4and random_state of 42. In practice, the test set here will function as the hold-out set.
Tune the hyperparameters on the training set using GridSearchCV with 5-folds. This involves first instantiating the GridSearchCV object with the correct parameters and then fitting it to the training data.
Print the best parameter and best score obtained from GridSearchCV by accessing the best_params_ and best_score_ attributes of logreg_cv.

## Hold-out set in practice II: Regression
100xp
Remember lasso and ridge regression from the previous chapter? Lasso used the L1L1 penalty to regularize, while ridge used the L2L2 penalty. There is another type of regularized regression known as the elastic net. In elastic net regularization, the penalty term is a linear combination of the L1L1 and L2L2 penalties:
a∗L1+b∗L2a∗L1+b∗L2
In scikit-learn, this term is represented by the 'l1_ratio'parameter: An 'l1_ratio' of 1 corresponds to an L1L1 penalty, and anything lower is a combination of L1L1 and L2L2.
In this exercise, you will GridSearchCV to tune the 'l1_ratio'of an elastic net model trained on the Gapminder data. As in the previous exercise, use a hold-out set to evaluate your model's performance.
### Instructions
Import the following modules:
ElasticNet from sklearn.linear_model.
mean_squared_error from sklearn.metrics.
GridSearchCV and train_test_split from sklearn.model_selection.
Create training and test sets, with 40% of the data used for the test set. Use a random state of 42.
Specify the hyperparameter grid for 'l1_ratio' using l1_space as the grid of values to search over.
Instantiate the ElasticNet regressor.
Use GridSearchCV with 5-fold cross-validation to tune 'l1_ratio' on the training data X_train and y_train. This involves first instantiating the GridSearchCV object with the correct parameters and then fitting it to the training data.
Predict on the test set and compute the R2R2 and mean squared error.

