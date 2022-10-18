import streamlit as st 
from datetime import datetime
st.write("# Welcome to Intelligent Document Search App! 👋")
st.sidebar.success("Select a pdf to perform operation.")
st.markdown(
        """
        Intelligent Document Search App is related to Natural Language Processing: 
        Intelligent Search through text using Spacy and Python.
        
       ➔ Extract useful information from text using Python and Machine Learning

       **👈Searching through text is one of the key focus area of Machine Learning Applications in the field of Natural Language..!

       ### ➔ But what if we have to search for multiple keywords from a large document (100+ pages).💡💭
       ### ➔ Also, what if we have do a contextual search (searching for similar meaning keywords) with in our document!🤔


       ##- The conventional ‘CTRL + F’ solution would either 
       take long long hours to accomplish this task 
       (or in case of contextual search, it will not be able to find any meaning text)..
     
       ### That’s why this project will be very useful❤️!!
   """
   )
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    df = extract_data(uploaded_file)
def extract_data(feed):
    data = []
    with pdfplumber.load(feed) as pdf:
        pages = pdf.pages
        for p in pages:
            data.append(p.extract_tables())
    return None
from spacy.matcher import PhraseMatcher
from scipy import spatial

# method for searching keyword from the text
def search_for_keyword(keyword, doc_obj, nlp):
    phrase_matcher = PhraseMatcher(nlp.vocab)
    phrase_list = [nlp(keyword)]
    phrase_matcher.add("Text Extractor", None, *phrase_list)

    matched_items = phrase_matcher(doc_obj)

    matched_text = []
    for match_id, start, end in matched_items:
        text = nlp.vocab.strings[match_id]
        span = doc_obj[start: end]
        matched_text.append(span.sent.text)

choice = st.radio(
    "What's your file format?",
    ('PDF', 'Doc', 'Excel'))

if choice == 'PDF':
    st.write('You selected PDF.')
else:
    st.write("You didn't selected PDF🥺. Kindly select pdf because it only supports pdf format.")


st.success("Built with Streamlit😊")
st.info(" 🎉 @Shivangi on Daisi platform")
st.text("By Shivangi Bhargava")
