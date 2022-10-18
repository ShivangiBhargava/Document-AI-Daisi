# Document-AI-Daisi
Extract useful information from text using Python and Machine Learning.
Searching through text is one of the key focus areas of Machine Learning Applications in the field of Natural Language.

But what if we have to search for multiple keywords from a large document (100+ pages). Also, what if we have do a contextual search (searching for similar meaning keywords) with in our document! — The conventional ‘CTRL + F’ solution would either take long long hours to accomplish this task (or in case of contextual search, it will not be able to find any meaning text).

So this daisi will help you for performing search through any text.

# STEPS:

1) First load the PDF document, then it will clean the text and then convert it into Spacy document object by using "Data_Preprocessing.py" to perform this task. 
2) Now we also have to convert our keywords to Spacy’s document object, convert them into their equivalent vector form ((300, ) dimension) and then finding similar keywords using the cosine similarity. Use "Similar_Keywords.py" to perform this task. 
3) For searching, we would be using the PhraseMatcher class of Spacy’s Matcher class. Use "Search.py" to perform this task. The code will search for every keyword we have through the entire text and will return us the entire sentence wherever it has found a match.
