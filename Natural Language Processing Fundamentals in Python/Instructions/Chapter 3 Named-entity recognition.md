# Chapter 3 Named-entity recognition
## NER with NLTK
100xp
You're now going to have some fun with named-entity recognition! A scraped news article has been pre-loaded into your workspace. Your task is to use nltk to find the named entities in this article.
What might the article be about, given the names you found?
Along with nltk, sent_tokenize and word_tokenize from nltk.tokenize have been pre-imported.
### Instructions
Tokenize article into sentences.
Tokenize each sentence in sentences into words using a list comprehension.
Inside a list comprehension, tag each tokenized sentence into parts of speech using nltk.pos_tag().
Chunk each tagged sentence into named-entity chunks using nltk.ne_chunk_sents(). Along with pos_sentences, specify the additional keyword argument binary=True.
Loop over each sentence and each chunk, and test whether it is a named-entity chunk by testing if it has the attribute label, and if the chunk.label() is equal to "NE". If so, print that chunk.

## Charting practice
100xp
In this exercise, you'll use some extracted named entities and their groupings from a series of newspaper articles to chart the diversity of named entity types in the articles.
You'll use a defaultdict called ner_categories, with keys representing every named entity group type, and values to count the number of each different named entity type. You have a chunked sentence list called chunked_sentences similar to the last exercise, but this time with non-binary category names.
You can use hasattr() to determine if each chunk has a 'label' and then simply use the chunk's .label() method as the dictionary key.
### Instructions
Create a defaultdict called ner_categories, with the default type set to int.
Fill up the dictionary with values for each of the keys. Remember, the keys will represent the label().
In the outer for loop, iterate over chunked_sentences, using sent as your iterator variable.
In the inner for loop, iterate over sent. If the condition is true, increment the value of each key by 1.
For the pie chart labels, create a list called labels from the keys of ner_categories, which can be accessed using .keys().
Use a list comprehension to create a list called values, using the .get() method on ner_categories to compute the values of each label l.
Use plt.pie() to create a pie chart for each of the NER categories. Along with values and labels=labels, pass the extra keyword arguments autopct='%1.1f%%' and startangle=140 to add percentages to the chart and rotate the initial start angle.
Display your pie chart. Was the distribution what you expected?

## Comparing NLTK with spaCy NER
100xp
Using the same text you used in the first exercise of this chapter, you'll now see the results using spaCy's NER annotator. How will they compare?
The article has been pre-loaded as article. To minimize execution times, you'll be asked to specify the keyword arguments tagger=False, parser=False, matcher=False when loading the spaCy model, because you only care about the entity in this exercise.
### Instructions
Import spacy.
Load the 'en' model using spacy.load(). Specify the additional keyword arguments tagger=False, parser=False, matcher=False.
Create a spacy document object by passing article into nlp().
Using ent as your iterator variable, iterate over the entities of doc and print out the labels (ent.label_) and text (ent.text).

## French NER with polyglot I
100xp
In this exercise and the next, you'll use the polyglot library to identify French entities. The library functions slightly differently than spacy, so you'll use a few of the new things you learned in the last video to display the named entity text and category.
You have access to the full article string in article. Additionally, the Text class of polyglot has been imported from polyglot.text.
### Instructions
Create a new Text object called txt.
Iterate over txt.entities and print each entity, ent.
Print the type of each entity.

## French NER with polyglot II
0xp
Here, you'll complete the work you began in the previous exercise. Your code from there has already been executed, as you can see from the output in the IPython Shell.
Your task is to use a list comprehension to create a list of tuples, in which the first element is the entity tag, and the second element is the full string of the entity text.
### Instructions
Use a list comprehension to create a list of tuples called entities.
The output expression of your list comprehension should be a tuple. Remember to use () to create the tuple.
The first element of each tuple is the entity tag, which you can access using its .tag attribute.
The second element is the full string of the entity text, which you can access using ' '.join(ent).
Your iterator variable should be ent, and you should iterate over all of the entities of the polyglot Textobject, txt.

## Spanish NER with polyglot
100xp
You'll continue your exploration of polyglot now with some Spanish annotation. This article is not written by a newspaper, so it is your first example of a more blog-like text. How do you think that might compare when finding entities?
The Text object has been created as txt, and each entity has been printed, as you can see in the IPython Shell.
Your specific task is to determine how many of the entities contain the words "Márquez" or "Gabo" - these refer to the same person in different ways!
### Instructions
Iterate over all of the entities of txt, using ent as your iterator variable.
Check whether the entity contains "Márquez" or "Gabo". If it does, increment count.
Hit 'Submit Answer' to see what percentage of entities refer to Gabriel García Márquez (aka Gabo).


## NER via ensemble model
100xp
In the final exercise of this NER chapter, you'll use the spacy and polyglot models to extract the best entities possible from English text. Here, you'll be using a long Medium post with a mixture of more formal article writing and informal. You'll find entities using both spacy and polyglot and choose only entities identified by both to create a sort of ensemble model.
In this exercise, you have access to the polyglotText class and the loaded english vectors for spacy in nlp. You also have the article text in article. The set of polyglot entities have been computed and are available in poly_ents. Your task is to compute the spacy entities and then find the intersection between the polyglotentities and the spacy entities.
Here, you'll be working with sets. A set comprehension looks exactly like a list comprehension, with the exception that it uses the set syntax markers {}.
### Instructions
Use a set comprehension to create a set of spacy entities, keeping only the text. The document object is available as doc. The text can be accessed using the .text attribute of each entity.
Use the set method .intersection() to find the entities that are in both spacy_ents andpoly_ents.
Calculate the number of entities notincluded in the new ensemble set of entities. You can do this by calculating the length of the union of spacy_ents and poly_ents(which can be computed using the .union() method) and then subtracting the length of ensemble_ents.

