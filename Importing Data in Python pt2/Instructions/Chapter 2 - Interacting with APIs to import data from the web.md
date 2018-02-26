# Chapter 2 - Interacting with APIs to import data from the web

## Loading and exploring a JSON
0xp
Now that you know what a JSON is, you'll load one into your Python environment and explore it yourself. Here, you'll load the JSON'a_movie.json' into the variable json_data, which will be a dictionary. You'll then explore the JSON contents by printing the key-value pairs of json_data to the shell.

### Instructions
Load the JSON 'a_movie.json' into the variable json_data within the context provided by the withstatement. To do so, use the function json.load() within the context manager.
Use a for loop to print all key-value pairs in the dictionary json_data. Recall that you can access a value in a dictionary using the syntax: dictionary[key].

## API requests
100xp
Now it's your turn to pull some movie data down from the Open Movie Database (OMDB) using their API. The movie you'll query the API about is The Social Network. Recall that, in the video, to query the API about the movie Hackers, Hugo's query string was 'http://www.omdbapi.com/?t=hackers' and had a single argument t=hackers.
Note: recently, OMDB has changed their API: you now also have to specify an API key. This means you'll have to add another argument to the URL: apikey=ff21610b.

### Instructions
Import the requests package.
Assign to the variable url the URL of interest in order to query 'http://www.omdbapi.com' for the data corresponding to the movie The Social Network. The query string should have two arguments: apikey=ff21610b and t=social+network. You can combine them as follows: apikey=ff21610b&t=social+network.
Print the text of the reponse object r by using its textattribute and passing the result to the print() function.

## JSON–from the web to Python
100xp
Wow, congrats! You've just queried your first API programmatically in Python and printed the text of the response to the shell. However, as you know, your response is actually a JSON, so you can do one step better and decode the JSON. You can then print the key-value pairs of the resulting dictionary. That's what you're going to do now!

### Instructions
Pass the variable url to the requests.get() function in order to send the relevant request and catch the response, assigning the resultant response message to the variable r.
Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
Hit Submit Answer to print the key-value pairs of the dictionary json_data to the shell.

## Checking out the Wikipedia API
100xp
You're doing so well and having so much fun that we're going to throw one more API at you: the Wikipedia API (documented here). You'll figure out how to find and extract information from the Wikipedia page for Pizza. What gets a bit wild here is that your query will return nested JSONs, that is, JSONs with JSONs, but Python can handle that because it will translate them into dictionaries within dictionaries.
The URL that requests the relevant query from the Wikipedia API is
https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza


### Instructions
Assign the relevant URL to the variable url.
Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
The variable pizza_extract holds the HTML of an extract from Wikipedia's Pizza page as a string; use the function print() to print this string to the shell.
