# Chapter 4 - Learning from the experts

## How many tokens?
Recall from previous chapters that how you tokenize text affects the n-gram statistics used in your model.
Going forward, you'll use alpha-numeric sequences, and only alpha-numeric sequences, as tokens. Alpha-numeric tokens contain only letters a-z and numbers 0-9 (no other characters). In other words, you'll tokenize on punctuation to generate n-gram statistics.
In this exercise, you'll make sure you remember how to tokenize on punctuation.
Assuming we tokenize on punctuation, accepting only alpha-numeric sequences as tokens, how many tokens are in the following string from the main dataset?
'PLANNING,RES,DEV,& EVAL      '


If you want, we've loaded this string into the workspace as SAMPLE_STRING, but you may not need it to answer the question.

4, because , and & are not tokens


## Deciding what's a word
Before you build up to the winning pipeline, it will be useful to look a little deeper into how the text features will be processed.
In this exercise, you will use CountVectorizer on the training data X_train (preloaded into the workspace) to see the effect of tokenization on punctuation.
Remember, since CountVectorizer expects a vector, you'll need to use the preloaded function, combine_text_columns before fitting to the training data.
### INSTRUCTIONS
100XP
Create text_vector by preprocessing X_train using combine_text_columns. This is important, or else you won't get any tokens!
Instantiate CountVectorizer as text_features. Specify the keyword argument token_pattern=TOKENS_ALPHANUMERIC.
Fit text_features to the text_vector.
Hit 'Submit Answer' to print the first 10 tokens.
## N-gram range in scikit-learn
In this exercise you'll insert a CountVectorizer instance into your pipeline for the main dataset, and compute multiple n-gram features to be used in the model.
In order to look for ngram relationships at multiple scales, you will use the ngram_range parameter as Peter discussed in the video.
Special functions: You'll notice a couple of new steps provided in the pipeline in this and many of the remaining exercises. Specifically, the dim_red step following the vectorizer step , and the scale step preceeding the clf (classification) step.
These have been added in order to account for the fact that you're using a reduced-size sample of the full dataset in this course. To make sure the models perform as the expert competition winner intended, we have to apply a dimensionality reduction technique, which is what the dim_red step does, and we have to scale the features to lie between -1 and 1, which is what the scale step does.
The dim_red step uses a scikit-learn function called SelectKBest(), applying something called the chi-squared testto select the K "best" features. The scale step uses a scikit-learn function called MaxAbsScaler() in order to squash the relevant features into the interval -1 to 1.
You won't need to do anything extra with these functions here, just complete the vectorizing pipeline steps below. However, notice how easy it was to add more processing steps to our pipeline!
### INSTRUCTIONS
100XP
Import CountVectorizer from sklearn.feature_extraction.text.
Add a CountVectorizer step to the pipeline with the name 'vectorizer'.
Set the token pattern to be TOKENS_ALPHANUMERIC.
Set the ngram_range to be (1, 2).


## Which models of the data include interaction terms?
Recall from the video that interaction terms involve products of features.
Suppose we have two features x and y, and we use models that process the features as follows:
βx + βy + ββ
βxy + βx + βy
βx + βy + βx^2 + βy^2
where β is a coefficient in your model (not a feature).
Which expression(s) include interaction terms?

The second expression


## Implement interaction modeling in scikit-learn
It's time to add interaction features to your model. The PolynomialFeatures object in scikit-learn does just that, but here you're going to a custom interaction object, SparseInteractions. Interaction terms are a statistical tool that lets your model express what happens if two features appear together in the same row.
SparseInteractions does the same thing as PolynomialFeatures, but it uses sparse matrices to do so. You can get the code for SparseInteractions at this GitHub Gist.
PolynomialFeatures and SparseInteractions both take the argument degree, which tells them what polynomia degree of interactions to compute.
You're going to consider interaction terms of degree=2 in your pipeline. You will insert these steps after the preprocessing steps you've built out so far, but before the classifier steps.
Pipelines with interaction terms take a while to train (since you're making n features into n-squared features!), so as long as you set it up right, we'll do the heavy lifting and tell you what your score is!
### INSTRUCTIONS
100XP
Add the interaction terms step using SparseInteractions()with degree=2. Give it a name of 'int', and make sure it is after the preprocessing step but before scaling.
## Why is hashing a useful trick?
In the video, Peter explained that a hash function takes an input, in your case a token, and outputs a hash value. For example, the input may be a string and the hash value may be an integer.
We've loaded a familiar python datatype, a dictionary called hash_dict, that makes this mapping concept a bit more explicit. In fact, python dictionaries ARE hash tables!
Print hash_dict in the IPython Shell to get a sense of how strings can be mapped to integers.
By explicitly stating how many possible outputs the hashing function may have, we limit the size of the objects that need to be processed. With these limits known, computation can be made more efficient and we can get results faster, even on large datasets.
Using the above information, answer the following:
Why is hashing a useful trick?

Some problems are memory-bound and not easily parallelizable, and hashing enforces a fixed length computation instead of using a mutable datatype (like a dictionary).


## Implementing the hashing trick in scikit-learn
In this exercise you will check out the scikit-learn implementation of HashingVectorizer before adding it to your pipeline later.
As you saw in the video, HashingVectorizer acts just like CountVectorizer in that it can accept token_pattern and ngram_range parameters. The important difference is that it creates hash values from the text, so that we get all the computational advantages of hashing!
### INSTRUCTIONS
100XP
Import HashingVectorizer from sklearn.feature_extraction.text.
Instantiate the HashingVectorizer as hashing_vec using the TOKENS_ALPHANUMERIC pattern.
Fit and transform hashing_vec using text_data. Save the result as hashed_text.
Hit 'Submit Answer' to see some of the resulting hash values.

## uild the winning model
You have arrived! This is where all of your hard work pays off. It's time to build the model that won DrivenData's competition.
You've constructed a robust, powerful pipeline capable of processing training and testing data. Now that you understand the data and know all of the tools you need, you can essentially solve the whole problem in a relatively small number of lines of code. Wow!
All you need to do is add the HashingVectorizer step to the pipeline to replace the CountVectorizer step.
The parameters non_negative=True, norm=None, andbinary=False make the HashingVectorizer perform similarly to the default settings on the CountVectorizer so you can just replace one with the other.
### INSTRUCTIONS
100XP
Import HashingVectorizer from sklearn.feature_extraction.text.
Add a HashingVectorizer step to the pipeline.
Name the step 'vectorizer'.
Use the TOKENS_ALPHANUMERIC token pattern.
Specify the ngram_range to be (1, 2)
