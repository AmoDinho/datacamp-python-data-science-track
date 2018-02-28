# Chapter 1 - Exploring the raw data

## What category of problem is this?
You're no novice to data science, but let's make sure we agree on the basics.
As Peter from DrivenData explained in the video, you're going to be working with school district budget data. This data can be classified in many ways according to certain labels, e.g. Function: Career & Academic Counseling, or Position_Type: Librarian.
Your goal is to develop a model that predicts the probability for each possible label by relying on some correctly labeled examples.
What type of machine learning problem is this?
ANSWER THE QUESTION
50XP
### Possible Answers
Reinforcement Learning, because the model is learning from the data through a system of rewards and punishments.

## What is the goal of the algorithm?
As you know from previous courses, there are different types of supervised machine learning problems. In this exercise you will tell us what type of supervised machine learning problem this is, and why you think so.
Remember, your goal is to correctly label budget line items by training a supervised model to predict the probability of each possible label, taking most probable label as the correct label.


Classification, because predicted probabilities will be used to select a label class.


## Loading the data
Now it's time to check out the dataset! You'll use pandas (which has been pre-imported as pd) to load your data into a DataFrame and then do some Exploratory Data Analysis (EDA) of it.
The training data is available as TrainingData.csv. Your first task is to load it into a DataFrame in the IPython Shell using pd.read_csv() along with the keyword argument index_col=0.
Use methods such as .info(), .head(), and .tail() to explore the budget data and the properties of the features and labels.
Some of the column names correspond to features - descriptions of the budget items - such as the Job_Title_Description column. The values in this column tell us if a budget item is for a teacher, custodian, or other employee.
Some columns correspond to the budget item labels you will be trying to predict with your model. For example, the Object_Type column describes whether the budget item is related classroom supplies, salary, travel expenses, etc.
Use df.info() in the IPython Shell to answer the following questions:
How many rows are there in the training data?
How many columns are there in the training data?
How many non-null entries are in the Job_Title_Description column?


1560 rows, 25 columns, 1131 non-null entries in Job_Title_Description.


## Summarizing the data
You'll continue your EDA in this exercise by computing summary statistics for the numeric data in the dataset. The data has been pre-loaded into a DataFrame called df.
You can use df.info() in the IPython Shell to determine which columns of the data are numeric, specifically type float64. You'll notice that there are two numeric columns, called FTEand Total.
FTE: Stands for "full-time equivalent". If the budget item is associated to an employee, this number tells us the percentage of full-time that the employee works. A value of 1 means the associated employee works for the schooll full-time. A value close to 0 means the item is associated to a part-time or contracted employee.
Total: Stands for the total cost of the expenditure. This number tells us how much the budget item cost.
After printing summary statistics for the numeric data, your job is to plot a histogram of the non-null FTE column to see the distribution of part-time and full-time employees in the dataset.
### INSTRUCTIONS
100XP
Print summary statistics of the numeric columns in the DataFrame df using the .describe() method.
Import matplotlib.pyplot as plt.
Create a histogram of the non-null 'FTE' column. You can do this by passing df['FTE'].dropna() to plt.hist().
The title has been specified and axes have been labeled, so hit 'Submit Answer' to see how often school employees work full-time!

## Exploring datatypes in pandas
It's always good to know what datatypes you're working with, especially when the inefficient pandas type object may be involved. Towards that end, let's explore what we have.
The data has been loaded into the workspace as df. Your job is to look at the DataFrame attribute .dtypes in the IPython Shell, and call its .value_counts()method in order to answer the question below.
Make sure to call df.dtypes.value_counts(), and not df.value_counts()! Check out the difference in the Shell. df.value_counts() will return an error, because it is a Series method, not a DataFrame method.

### How many columns with dtype object are in the data?


## Encode the labels as categorical variables
Remember, your ultimate goal is to predict the probability that a certain label is attached to a budget line item. You just saw that many columns in your data are the inefficient object type. Does this include the labels you're trying to predict? Let's find out!
There are 9 columns of labels in the dataset. Each of these columns is a category that has many possible values it can take). The 9 labels have been loaded into a list called LABELS. In the Shell, check out the type for these labels using df[LABELS].dtypes.
You will notice that every label is encoded as an object datatype. Because category datatypes are much more efficient your task is to convert the labels to category types using the .astype()method.
Note: .astype() only works on a pandas Series. Since you are working with a pandas DataFrame, you'll need to use the .apply() method and provide a lambda function called categorize_label that applies .astype() to each column, x.
### INSTRUCTIONS
100XP
Define the lambda function categorize_label to convert column x into x.astype('category').
Use the LABELS list provided to convert the subset of data df[LABELS] to categorical types using the .apply() method and categorize_label. Don't forget axis=0.
Print the converted .dtypes attribute of df[LABELS].

## Counting unique labels
As Peter mentioned in the video, there are over 100 unique labels. In this exercise, you will explore this fact by counting and plotting the number of unique values for each category of label.
The dataframe df and the LABELS list have been loaded into the workspace; the LABELS columns of df have been converted to category types.
pandas, which has been pre-imported as pd, provides a pd.Series.nunique method for counting the number of unique values in a Series.
### INSTRUCTIONS
100XP
Create the DataFrame num_unique_labels by using the .apply() method on df[LABELS] with pd.Series.nuniqueas the argument.
Create a bar plot of num_unique_labels using pandas' .plot(kind='bar') method.
The axes have been labeled for you, so hit 'Submit Answer' to see the number of unique values for each label.
## Penalizing highly confident wrong answers
As Peter explained in the video, log loss provides a steep penalty for predictions that are both wrong and confident, i.e., a high probability is assigned to the incorrect class.
Suppose you have the following 3 examples:
A:y=1,p=0.85A:y=1,p=0.85
B:y=0,p=0.99B:y=0,p=0.99
C:y=0,p=0.51C:y=0,p=0.51
Select the ordering of the examples which corresponds to the lowest to highest log loss scores. y is an indicator of whether the example was classified correctly. You shouldn't need to crunch any numbers!
Lowest: A, Middle: C, Highest: B.

## Computing log loss with NumPy
To see how the log loss metric handles the trade-off between accuracy and confidence, we will use some sample data generated with NumPy and compute the log loss using the provided function compute_log_loss(), which Peter showed you in the video.
5 one-dimensional numeric arrays simulating different types of predictions have been pre-loaded: actual_labels, correct_confident, correct_not_confident, wrong_not_confident, and wrong_confident.
Your job is to compute the log loss for each sample set provided using the compute_log_loss(predicted_values, actual_values). It takes the predicted values as the first argument and the actual values as the second argument.
### INSTRUCTIONS
100XP
Using the compute_log_loss() function, compute the log loss for the following predicted values (in each case, the actual values are contained in actual_labels):
correct_confident.
correct_not_confident.
wrong_not_confident.
wrong_confident.
actual_labels.


