# Chapter 3 -Diving deep into the Twitter API

## API Authentication
100xp
The package tweepy is great at handling all the Twitter API OAuth Authentication details for you. All you need to do is pass it your authentication credentials. In this interactive exercise, we have created some mock authentication credentials (if you wanted to replicate this at home, you would need to create a Twitter App as Hugo detailed in the video). Your task is to pass these credentials to tweepy's OAuth handler.
### Instructions
Import the package tweepy.
Pass the parameters consumer_keyand consumer_secret to the function tweepy.OAuthHandler().
Complete the passing of OAuth credentials to the OAuth handler authby applying to it the method set_access_token(), along with arguments access_token and access_token_secret.

## Streaming tweets
100xp
Now that you have set up your authentication credentials, it is time to stream some tweets! We have already defined the tweet stream listener class, MyStreamListener, just as Hugo did in the introductory video. You can find the code for the tweet stream listener class here.
Your task is to create the Streamobject and to filter tweets according to particular keywords.
### Instructions
Create your Stream object with authentication by passing tweepy.Stream() the authentication handler auth and the Stream listener l;
To filter Twitter streams, pass to the track argument in stream.filter() a list containing the desired keywords 'clinton', 'trump', 'sanders', and 'cruz'.
## Load and explore your Twitter data
100xp
Now that you've got your Twitter data sitting locally in a text file, it's time to explore it! This is what you'll do in the next few interactive exercises. In this exercise, you'll read the Twitter data into a list: tweets_data.
### Instructions
Assign the filename 'tweets.txt' to the variable tweets_data_path.
Initialize tweets_data as an empty list to store the tweets in.
Within the for loop initiated by for line in tweets_file:, load each tweet into a variable, tweet, using json.loads(), then append tweet to tweets_data using the append() method.
Hit submit and check out the keys of the first tweet dictionary printed to the shell


## Twitter data to DataFrame
100xp
Now you have the Twitter data in a list of dictionaries, tweets_data, where each dictionary corresponds to a single tweet. Next, you're going to extract the text and language of each tweet. The text in a tweet, t1, is stored as the value t1['text']; similarly, the language is stored in t1['lang']. Your task is to build a DataFrame in which each row is a tweet and the columns are 'text' and 'lang'.
### Instructions
Use pd.DataFrame() to construct a DataFrame of tweet texts and languages; to do so, the first argument should be tweets_data, a list of dictionaries. The second argument to pd.DataFrame() is a list of the keys you wish to have as columns. Assign the result of the pd.DataFrame() call to df.
Print the head of the DataFrame.

## A little bit of Twitter text analysis
100xp
Now that you have your DataFrame of tweets set up, you're going to do a bit of text analysis to count how many tweets contain the words 'clinton', 'trump', 'sanders' and 'cruz'. In the pre-exercise code, we have defined the following function word_in_text(), which will tell you whether the first argument (a word) occurs within the 2nd argument (a tweet).
import re

def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False


You're going to iterate over the rows of the DataFrame and calculate how many tweets contain each of our keywords! The list of objects for each candidate has been initialized to 0.
### Instructions
Within the for loop for index, row in df.iterrows():, the code currently increases the value of clinton by 1 each time a tweet mentioning 'Clinton' is encountered; complete the code so that the same happens for trump, sanders and cruz.

## Plotting your Twitter data
100xp
Now that you have the number of tweets that each candidate was mentioned in, you can plot a bar chart of this data. You'll use the statistical data visualization library seaborn, which you may not have seen before, but we'll guide you through. You'll first import seaborn as sns. You'll then construct a barplot of the data using sns.barplot, passing it two arguments:
a list of labels and
a list containing the variables you wish to plot (clinton, trump and so on.)
Hopefully, you'll see that Trump was unreasonably represented! We have already run the previous exercise solutions in your environment.
### Instructions
Import both matplotlib.pyplot and seaborn using the aliases plt and sns, respectively.
Complete the arguments of sns.barplot: the first argument should be the labels to appear on the x-axis; the second argument should be the list of the variables you wish to plot, as produced in the previous exercise.


