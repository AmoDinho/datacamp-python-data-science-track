# Chapter 1 Regular expressions & word tokenization

![Link](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)
## Practicing regular expressions: re.split() and re.findall()
100xp
Now you'll get a chance to write some regular expressions to match digits, strings and non-alphanumeric characters. Take a look at my_string first by printing it in the IPython Shell, to determine how you might best match the different steps.
Note: It's important to prefix your regex patterns with r to ensure that your patterns are interpreted in the way you want them to. Else, you may encounter problems to do with escape sequences in strings. For example, "\n" in Python is used to indicate a new line, but if you use the rprefix, it will be interpreted as the raw string "\n" - that is, the character "\" followed by the character "n" - and not as a new line.
### Instructions
- Import the regular expression module re.
- Split my_string on each sentence ending. To do this:
- Write a pattern called sentence_endings to match sentence endings (., ?, and !).
- Use re.split() to split my_string on the pattern and print the result.
- Find all capitalized words in my_string by writing a pattern called capitalized_words and using re.findall(). Print the result.
- Write a pattern called spaces to match spaces ("\s") and then use re.split() to split my_string on this pattern, keeping all punctuation intact. Print the result.
- Find all digits in my_string by writing a pattern called digits ("\d") and using re.findall(). Print the result.


## Word tokenization with NLTK
100xp
Here, you'll be using the first scene of Monty Python's Holy Grail, which has been pre-loaded as scene_one. Feel free to check it out in the IPython Shell!
Your job in this exercise is to utilize word_tokenize and sent_tokenize from nltk.tokenize to tokenize both words and sentences from Python strings - in this case, the first scene of Monty Python's Holy Grail.
### Instructions
- Import the sent_tokenize and word_tokenize functions from nltk.tokenize.
- Tokenize all the sentences in scene_one using the sent_tokenize() function.
- Tokenize the fourth sentence in sentences, which you can access as sentences[3], using the word_tokenize()function.
- Find the unique tokens in the entire scene by using word_tokenize() on scene_one and then converting it into a set using set().
- Print the unique tokens found. This has been done for you, so hit 'Submit Answer' to see the results!


## More regex with re.search()
0xp
In this exercise, you'll utilize re.search() and re.match() to find specific tokens. Both search and match expect regex patterns, similar to those you defined in an earlier exercise. You'll apply these regex library methods to the same Monty Python text from the nltk corpora.
You have both scene_one and sentences available from the last exercise; now you can use them with re.search() and re.match() to extract and match more text.
### Instructions
- Use re.search() to search for the first occurance of the word "coconuts" in scene_one. Store the result in match.
- Print the start and end indexes of match using its .start()and .end() methods, respectively.
- Write a regular expression called pattern1 to find anything in square brackets.
- Use re.search() with the previous pattern to find the first text in square brackets in the scene. Print the result.
- Use re.match() to match the script notation in the fourthline (ARTHUR:) and print the result. The tokenized sentences of scene_one are available in your namespace as sentences.

## Choosing a tokenizer
50xp
Given the following string, which is the best tokenizer? If possible, you want to retain sentence punctuation as separate tokens, but have '#1' remain a single token.
my_string = "SOLDIER #1: Found them? In Mercea? The coconut's tropical!"
Answer  ===    r"(#\d\w+\?!)"


## Regex with NLTK tokenization
100xp
Twitter is a frequently used source for NLP text and tasks. In this exercise, you'll build a more complex tokenizer for tweets with hashtags and mentions using nltk and regex. The nltk.tokenize.TweetTokenizer class gives you some extra methods and attributes for parsing tweets.
Here, you're given some example tweets to parse using both TweetTokenizer and regexp_tokenize from the nltk.tokenizemodule. These example tweets have been pre-loaded into the variable tweets. Feel free to explore it in the IPython Shell!
Remember: | is like an "or" statement in regex and square brackets can be used to create groups.
### Instructions
- Import the regexp_tokenize and TweetTokenizer from nltk.tokenize.
- A regex pattern to define hashtags called pattern1 has been defined for you. Call regexp_tokenize() with this hashtag pattern on the first tweet in tweets.
- Write a new pattern called pattern2 to match mentions orhashtags. A mention is something like @DataCamp. Then, call regexp_tokenize() with your new hashtag pattern on the last tweet in tweets. You can access the last element of a list using -1 as the index, for example, tweets[-1].
- Create an instance of TweetTokenizer called tknzr and use it inside a list comprehension to tokenize each tweet into a new list called all_tokens. To do this, use the .tokenize() method of tknzr, with t as your iterator variable.
## Non-ascii tokenization
0xp
In this exercise, you'll practice advanced tokenization by tokenizing some non-ascii based text. You'll be using German with emoji!
Here, you have access to a string called german_text, which has been printed for you in the Shell. Notice the emoji and the German characters!
The following modules have been pre-imported from nltk.tokenize: regexp_tokenize and word_tokenize.
Unicode ranges for emoji are:
('\U0001F300'-'\U0001F5FF'), ('\U0001F600-\U0001F64F'), ('\U0001F680-\U0001F6FF'), and ('\u2600'-\u26FF-\u2700-\u27BF').
### Instructions
- Tokenize all the words in german_text using word_tokenize(), and print the result.
- Tokenize only the capital words in german_text.
- First, write a pattern called capital_words to match only capital words. Make sure to check for the German Ü!
- Then, tokenize it using regexp_tokenize().
- Tokenize only the emoji in german_text. The pattern using the unicode ranges for emoji given in the assignment text has been written for you. Your job is to use regexp_tokenize()to tokenize the emoji.
## Charting practice
100xp
Try using your new skills to find and chart the number of words per line in the script using matplotlib. The Holy Grail script is loaded for you, and you need to use regex to find the words per line.
Using list comprehensions here will speed up your computations. For example: my_lines = [tokenize(l) for l in lines] will call a function tokenize on each line in the list lines. The new transformed list will be saved in the my_lines variable.
You have access to the entire script in the variable holy_grail. Go for it!
### Instructions
- Split the script into lines using the newline ('\n') character.
- Use re.sub() inside a list comprehension to replace the prompts such as ARTHUR: and SOLDIER #1. The pattern has been written for you.
- Use a list comprehension to tokenize lines with regexp_tokenize(), keeping only words. Recall that the pattern for words is "\w+".
- Use a list comprehension to create a list of line lengths called line_num_words.
- Use t_line as your iterator variable to iterate over tokenized_lines, and then len() function to compute line lengths.
- Plot a histogram of line_num_words using plt.hist(). Don't forgot to use plt.show() as well to display the plot.


