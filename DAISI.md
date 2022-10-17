We will first load the PDF document, clean the text and then convert it into Spacy document object.
Use Data_Preprocessing.py to perform this task.
ow we also have to convert our keywords to Spacy’s document object, convert them into their equivalent vector form ((300, ) dimension) and then finding similar keywords using the cosine similarity.
Use Similar_Keywords.py to perform this task.
For searching, we would be using the PhraseMatcher class of Spacy’s Matcher class.
Use Search.py to perform this task.
The code will search for every keyword we have through the entire text and will return us the entire sentence wherever it has found a match.
