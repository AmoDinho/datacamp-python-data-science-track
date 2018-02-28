# Chapter 2 Simple topic identification

### Building a Counter with bag-of-words
100xp
In this exercise, you'll build your first (in this course) bag-of-words counter using a Wikipedia article, which has been pre-loaded as article. Try doing the bag-of-words without looking at the full article text, and guessing what the topic is! If you'd like to peek at the title at the end, we've included it as article_title. Note that this article text has had very little preprocessing from the raw Wikipedia database entry.
word_tokenize has been imported for you.
### Instructions
Import Counter from collections.
Use word_tokenize() to split the article into tokens.
Use a list comprehension with t as the iterator variable to convert all the tokens into lowercase. The .lower() method converts text into lowercase.
Create a bag-of-words counter called bow_simple by using Counter() with lower_tokens as the argument.
Use the .most_common() method of bow_simple to print the 10 most common tokens.

## Text preprocessing practice
100xp
Now, it's your turn to apply the techniques you've learned to help clean up text for better NLP results. You'll need to remove stop words and non-alphabetic characters, lemmatize, and perform a new bag-of-words on your cleaned text.
You start with the same tokens you created in the last exercise: lower_tokens. You also have the Counter class imported.
### Instructions
Import the WordNetLemmatizer class from nltk.stem.
Create a list called alpha_only that iterates through lower_tokens and retains only alphabetical characters. You can use the .isalpha() method to check for this.
Create another list called no_stops in which you remove all stop words, which are held in a list called english_stops.
Initialize a WordNetLemmatizer object called wordnet_lemmatizer and use its .lemmatize() method on the tokens in no_stops to create a new list called lemmatized.
Finally, create a new Counter called bow with the lemmatized words and show the 10 most common tokens.


## Creating and querying a corpus with gensim
100xp
It's time to apply the methods you learned in the previous video to create your first gensim dictionary and corpus!
You'll use these data structures to investigate word trends and potential interesting topics in your document set. To get started, we have imported a few additional messy articles from Wikipedia, which were preprocessed by lowercasing all words, tokenizing them, and removing stop words and punctuation. These were then stored in a list of document tokens called articles. You'll need to do some light preprocessing and then generate the gensim dictionary and corpus.
### Instructions
Import Dictionary from gensim.corpora.dictionary.
Initialize a gensim Dictionary with the tokens in articles.
Obtain the id for "computer" from dictionary. To do this, use its .token2id method which returns ids from text, and then chain .get() which returns tokens from ids. Pass in "computer" as an argument to .get().
Use a list comprehension in which you iterate over articlesto create a gensim MmCorpus from dictionary.
In the output expression, use the .doc2bow() method on dictionary with article as the argument.
Print the first 10 word ids with their frequency counts from the fifth document. This has been done for you, so hit 'Submit Answer' to see the results!

## Gensim bag-of-words
100xp
Now, you'll use your new gensim corpus and dictionary to see the most common terms per document and across all documents. You can use your dictionary to look up the terms. Take a guess at what the topics are and feel free to explore more documents in the IPython Shell!
You have access to the dictionary and corpus objects you created in the previous exercise, as well as the Python defaultdict and itertools to help with the creation of intermediate data structures for analysis.
The fifth document from corpus is stored in the variable doc, which has been sorted in descending order.
### Instructions
Print the top five words of bow_doc using each word_idwith the dictionary alongside word_count. The word_id can be accessed using the .get() method of dictionary.
Create a defaultdict called total_word_count in which the keys are all the token ids (word_id) and the values are the sum of their occurrence across all documents (word_count). Remember to specify int when creating the defaultdict, and inside the for loop, increment each word_id of total_word_count by word_count.
Create a sorted list from the defaultdict, using words across the entire corpus. To achieve this, use the .items() method on total_word_count inside sorted().
Similar to how you printed the top five words of bow_docearlier, print the top five words of sorted_word_count as well as the number of occurrences of each word across all the documents.

## Tf-iDf with Wikipedia


Now it's your turn to determine new significant terms for your corpus by applying gensim's tf-idf. You will again have access to the same corpus and dictionary objects you created in the previous exercises - dictionary, corpus, and doc. Will tf-idf make for more interesting results on the document level?
### Instructions
Import TfidfModel from gensim.models.tfidfmodel.
Initialize a new TfidfModel called tfidf using corpus.
Use doc to calculate the weights. You can do this by passing [doc] to tfidf.
Print the first five term ids with weights.
Sort the term ids and weights in a new list from highest to lowest weight. This has been done for you.
Print the top five weighted words (term_id) from sorted_tfidf_weights along with their weighted score (weight).


