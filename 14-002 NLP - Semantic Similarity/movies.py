# movie recommedation system 
# importing spacy and specifying the model to use
import pandas as pd
import numpy as np
import spacy

nlp = spacy.load('en_core_web_md')

# reading the movies dataframe
df = pd.read_csv('movies.txt', sep = ':', 
                 names = ["movie", "descriptions"])

# defining a function to suggest a similar new movie based on current movie choice
def movie_recommendation(description): 
    doc_ = nlp(description)
    ' '.join( i.lemma_.lower() for i in doc_ if not i.is_stop and not i.is_punct )
    
    # making an empty list to store similarity scores 
    similarity_scores = [] 

    # iterating through each description and calculating similarity and adding to a list
    for desc in df['descriptions']:
        doc = nlp(desc)
        ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])
        similarity_scores.append(doc.similarity(doc_))
    
    # adding the list to the data frame
    df['similarity_score'] = similarity_scores
    
    # finding the movie with max similarity role
    max_similarity_score = max(similarity_scores)
    recommended_movie = df[df['similarity_score'] == max_similarity_score]
    return recommended_movie
    

description = '''Willhe save their world or destroy it? When 
               the hulk becomes too dangerous for the earth, the Illuminati 
               trick Hulk into a shuttle and launch him into space to a planet
               where the Hulk can live in peace. Unfortunately, Hulk lands on 
               the planet Sakaar where is sold into slavery and trained as 
               as a gladiator.'''



print (df)
print("\t")
print (movie_recommendation(nlp(description)))





