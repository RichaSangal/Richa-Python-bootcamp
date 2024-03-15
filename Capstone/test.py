
import pandas as pd
import spacy

from textblob import TextBlob

# reading the dataframe
df = pd.read_csv('amazon_data.csv', sep = ',', low_memory = False )

# understanding the data frame and 
#print(df.head())

#print(df.info())

# selecting relevant columns and removing missing values
df = df[['reviews.text']].dropna()

print(df.head())

# using spacy now for text processing and preparing the reviews
nlp = spacy.load('en_core_web_lg')

# function to preprocess the text
def process(text):
    doc = nlp(text)
    return ' '.join([token.lemma_.lower().strip() for token in doc if not token.is_stop and not token.is_punct])


def get_sent (review):
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    
    # calculating the sentiment

    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return (sentiment)


df = df.sample(5000, random_state=42)
df['review_processed'] = df['reviews.text'].apply(process)
print(df)
df['Sentiment'] = df['review_processed'].apply(get_sent)
print(df)



 


