# capstone project
# importing required libraries
import pandas as pd
import spacy
from textblob import TextBlob

# Now we are going to understand the customer sentiments using sentiment analysis for some of amazon products. 
# We will look into the amazon data downloaded from Kaggle.
# We want to understand if the sentiment is postive, negative or neutral.

# Reading the dataframe
df = pd.read_csv('amazon_data.csv', sep = ',', low_memory = False )

# Understanding the data frame 
print(df.head())
print(df.info())

# Selecting relevant columns and removing missing values
df = df[['reviews.text']].dropna()

print(df.head())

# Selecting the large model from spacy for text processing
nlp = spacy.load('en_core_web_lg')

# Function to preprocess the text and remove stop words and punctuation
def process(text):
    doc = nlp(text)
    return ' '.join([token.lemma_.lower().strip() for token in doc if not token.is_stop and not token.is_punct])

# Function to analyse the sentiment with textblob
def get_sent (dataframe, column, index):
    review = dataframe[column][index]
    review_ = process(review)
    blob = TextBlob(review_)
    polarity = blob.sentiment.polarity
    
    # calculating the sentiment
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return (sentiment)

#Using the function for analysing sentiment on sample reviews
print( f"Review: \t{df['reviews.text'][1]} \nSentiment:\t{get_sent(df, 'reviews.text', 1)}")
print()
print( f"Review: \t{df['reviews.text'][50]} \nSentiment:\t{get_sent(df, 'reviews.text', 50)}")
print()
print( f"Review: \t{df['reviews.text'][10]} \nSentiment:\t{get_sent(df, 'reviews.text', 10)}")


# checking similarity between two reviews
print ("-----------checking similarity between two reviews----------")

# defining a function to convert text to spacy doc
def get_doc(text_):
    doc_ = nlp(text_)
    return doc_

# selecting sample dataset of 50 to reduce processing time 
df = df.sample(50, random_state=42)

# adding another column to the dataset with processed text
df['preprocessed_reviews'] = df['reviews.text'].apply(process)

# adding another column to sample dataset with data conveted to spacy doc
df['doc_reviews'] = df['preprocessed_reviews'].apply(get_doc)

print(df.head())
print()
print(f"Reviews selected for analysis are as below:\n1.{df['doc_reviews'][6127]}\n2.{df['doc_reviews'][1118]}")
print()
print(f"The similarity score between above two reviews is {(df['doc_reviews'][6127]).similarity(df['doc_reviews'][1118])}")


    





 


