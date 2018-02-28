#---------------------------------------------------------------------------------------------------------------#
#Chapter 3 Named-entity recognition



#---------------------------------------------------------------------------------------------------------------#
#NER with NLTK
# Tokenize the article into sentences: sentences
sentences = nltk.sent_tokenize(article)

# Tokenize each sentence into words: token_sentences
token_sentences = [nltk.word_tokenize(sent) for sent in sentences]

# Tag each tokenized sentence into parts of speech: pos_sentences
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences] 

# Create the named entity chunks: chunked_sentences
chunked_sentences = nltk.ne_chunk_sents(pos_sentences, binary=True)

# Test for stems of the tree with 'NE' tags
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, "label") and chunk.label() == "NE":
            print(chunk)

#---------------------------------------------------------------------------------------------------------------#
#Charting practice
# Create the defaultdict: ner_categories
ner_categories = defaultdict(int)

# Create the nested for loop
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, 'label'):
            ner_categories[chunk.label()] += 1
            
# Create a list from the dictionary keys for the chart labels: labels
labels = list(ner_categories.keys())

# Create a list of the values: values
values = [ner_categories.get(l) for l in labels]

# Create the pie chart
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

# Display the chart
plt.show()


#---------------------------------------------------------------------------------------------------------------#

#Comparing NLTK with spaCy NER

# Import spacy
import spacy

# Instantiate the English model: nlp
nlp = spacy.load('en', tagger=False, parser=False, matcher=False)

# Create a new document: doc
doc = nlp(article)

# Print all of the found entities and their labels
for ent in doc.ents:
    print(ent.label_, ent.text)

#---------------------------------------------------------------------------------------------------------------#
#French NER with polyglot I
# Create a new text object using Polyglot's Text class: txt
txt = Text(article)

# Print each of the entities found
for ent in txt.entities:
    print(ent)
    
# Print the type of each entity
print(type(ent))


#---------------------------------------------------------------------------------------------------------------#
#French NER with polyglot II
# Create the list of tuples: entities
entities = [(ent.tag, ' '.join(ent)) for ent in txt.entities]

# Print the entities
print(entities)



#---------------------------------------------------------------------------------------------------------------#

#Spanish NER with polyglot
# Initialize the count variable: count
count = 0

# Iterate over all the entities
for ent in txt.entities:
    # Check whether the entity contains 'Márquez' or 'Gabo'
    if "Márquez" in ent or "Gabo" in ent:
        # Increment count
        count += 1

# Print count
print(count)

# Calculate the percentage of entities that refer to "Gabo": percentage
percentage = count * 1.0 / len(txt.entities)
print(percentage)


#---------------------------------------------------------------------------------------------------------------#
#NER via ensemble model
# Create a set of spaCy entities keeping only their text: spacy_ents
spacy_ents = {e.text for e in doc.ents} 

# Create a set of the intersection between the spacy and polyglot entities: ensemble_ents
ensemble_ents = spacy_ents.intersection(poly_ents)

# Print the common entities
print(ensemble_ents)

# Calculate the number of entities not included in the new ensemble set of entities: num_left_out
num_left_out = len(spacy_ents.union(poly_ents)) - len(ensemble_ents)
print(num_left_out)



#---------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------#
