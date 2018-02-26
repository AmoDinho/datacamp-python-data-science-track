# Chapter 1 - Importing data from the Internet


## Importing flat files from the web: your turn!
100xp
You are about to import your first file from the web! The flat file you will import will be 'winequality-red.csv' from the University of California, Irvine's Machine Learning repository. The flat file contains tabular data of physiochemical properties of red wine, such as pH, alcohol content and citric acid content, along with wine quality rating.
The URL of the file is
'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'


After you import it, you'll check your working directory to confirm that it is there and then you'll load it into a pandas DataFrame.
### Instructions
Import the function urlretrieve from the subpackage urllib.request.
Assign the URL of the file to the variable url.
Use the function urlretrieve() to save the file locally as 'winequality-red.csv'.
Execute the remaining code to load 'winequality-red.csv'in a pandas DataFrame and to print its head to the shell.


## Opening and reading flat files from the web
100xp
You have just imported a file from the web, saved it locally and loaded it into a DataFrame. If you just wanted to load a file from the web into a DataFrame without first saving it locally, you can do that easily using pandas. In particular, you can use the function pd.read_csv() with the URL as the first argument and the separator sep as the second argument.
The URL of the file, once again, is
'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'


### Instructions
Assign the URL of the file to the variable url.
Read file into a DataFrame df using pd.read_csv(), recalling that the separator in the file is ';'.
Print the head of the DataFrame df.
Execute the rest of the code to plot histogram of the first feature in the DataFrame df.


## Importing non-flat files from the web
100xp
Congrats! You've just loaded a flat file from the web into a DataFrame without first saving it locally using the pandas function pd.read_csv(). This function is super cool because it has close relatives that allow you to load all types of files, not only flat ones. In this interactive exercise, you'll use pd.read_excel() to import an Excel spreadsheet.
The URL of the spreadsheet is
'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'


Your job is to use pd.read_excel() to read in all of its sheets, print the sheet names and then print the head of the first sheet using its name, not its index.
Note that the output of pd.read_excel() is a Python dictionary with sheet names as keys and corresponding DataFrames as corresponding values.

### Instructions
Assign the URL of the file to the variable url.
Read the file in url into a dictionary xl using pd.read_excel() recalling that, in order to import all sheets you need to pass None to the argument sheetname.
Print the names of the sheets in the Excel spreadsheet; these will be the keys of the dictionary xl.
Print the head of the first sheet using the sheet name, not the index of the sheet! The sheet name is '1700'


## Performing HTTP requests in Python using urllib
100xp
Now that you know the basics behind HTTP GET requests, it's time to perform some of your own. In this interactive exercise, you will ping our very own DataCamp servers to perform a GET request to extract information from our teach page, "http://www.datacamp.com/teach/documentation".
In the next exercise, you'll extract the HTML itself. Right now, however, you are going to package and send the request and then catch the response.

### Instructions
Import the functions urlopen and Request from the subpackage urllib.request.
Package the request to the url "http://www.datacamp.com/teach/documentation"using the function Request() and assign it to request.
Send the request and catch the response in the variable response with the function urlopen().
Run the rest of the code to see the datatype of response and to close the connection!

## Printing HTTP request results in Python using urllib
100xp
You have just packaged and sent a GET request to "http://www.datacamp.com/teach/documentation"and then caught the response. You saw that such a response is a http.client.HTTPResponseobject. The question remains: what can you do with this response?
Well, as it came from an HTML page, you could readit to extract the HTML and, in fact, such a http.client.HTTPResponse object has an associated read() method. In this exercise, you'll build on your previous great work to extract the response and print the HTML.

### Instructions
Send the request and catch the response in the variable response with the function urlopen(), as in the previous exercise.
Extract the response using the read()method and store the result in the variable html.
Print the string html.
Hit submit to perform all of the above and to close the response: be tidy!

## Performing HTTP requests in Python using requests
100xp
Now that you've got your head and hands around making HTTP requests using the urllib package, you're going to figure out how to do the same using the higher-level requests library. You'll once again be pinging DataCamp servers for their "http://www.datacamp.com/teach/documentation"page.
Note that unlike in the previous exercises using urllib, you don't have to close the connection when using requests!

### Instructions
Import the package requests.
Assign the URL of interest to the variable url.
Package the request to the URL, send the request and catch the response with a single function requests.get(), assigning the response to the variable r.
Use the text attribute of the object r to return the HTML of the webpage as a string; store the result in a variable text.
Hit submit to print the HTML of the webpage.

## Parsing HTML with BeautifulSoup
100xp
In this interactive exercise, you'll learn how to use the BeautifulSoup package to parse, prettify and extract information from HTML. You'll scrape the data from the webpage of Guido van Rossum, Python's very own Benevolent Dictator for Life. In the following exercises, you'll prettify the HTML and then extract the text and the hyperlinks.
The URL of interest is url = 'https://www.python.org/~guido/'.

### Instructions
Import the function BeautifulSoupfrom the package bs4.
Assign the URL of interest to the variable url.
Package the request to the URL, send the request and catch the response with a single function requests.get(), assigning the response to the variable r.
Use the text attribute of the object r to return the HTML of the webpage as a string; store the result in a variable html_doc.
Create a BeautifulSoup object soupfrom the resulting HTML using the function BeautifulSoup().
Use the method prettify() on soup and assign the result to pretty_soup.
Hit submit to print to prettified HTML to your shell!


## Turning a webpage into data using BeautifulSoup: getting the text
100xp
As promised, in the following exercises, you'll learn the basics of extracting information from HTML soup. In this exercise, you'll figure out how to extract the text from the BDFL's webpage, along with printing the webpage's title.

### Instructions
In the sample code, the HTML response object html_doc has already been created: your first task is to Soupify it using the function BeatifulSoup()and to assign the resulting soup to the variable soup.
Extract the title from the HTML soup soup using the attribute title and assign the result to guido_title.
Print the title of Guido's webpage to the shell using the print() function.
Extract the text from the HTML soup soup using the method get_text() and assign to guido_text.
Hit submit to print the text from Guido's webpage to the shell.


## Turning a webpage into data using BeautifulSoup: getting the hyperlinks
100xp
In this exercise, you'll figure out how to extract the URLs of the hyperlinks from the BDFL's webpage. In the process, you'll become close friends with the soup method find_all().

### Instructions
Use the method find_all() to find all hyperlinks in soup, remembering that hyperlinks are defined by the HTML tag <a>; store the result in the variable a_tags.
The variable a_tags is a results set: your job now is to enumerate over it, using a for loop and to print the actual URLs of the hyperlinks; to do this, for every element link in a_tags, you want to print()link.get('href').

