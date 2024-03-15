# importing spacy and specifying the model to use
import pandas as pd
import numpy as np
import spacy

nlp = spacy.load('en_core_web_md')

# reading the dataframe
df_movies = pd.read_csv('movies.txt',sep=':', names=['movie', 'description'])

# converting dataframe to dictionary to help iterate each description
df_movies_dict = df_movies.set_index('movie')['description'].to_dict()

# adding the movie and desc to dictionary
movie_check = {'Planet Hulk': '''Willhe save their world or destroy it? When 
               the hulk becomes too dangerous for the earth, the Illuminati 
               trick Hulk into a shuttle and launch him into space to a planet
               where the Hulk can live in peace. Unfortunately, Hulk lands on 
               the planet Sakaar where is sold into slavery and trained as 
               as a gladiator.'''}

# processing the description using the model
movie_check = nlp( movie_check['Planet Hulk'])

print (movie_check)

list_similarity = []
dic_similarity = {}

for movie, desc in df_movies_dict.items():
    doc = nlp (desc)
    similarity = doc.similarity(movie_check)
    list_similarity.append(similarity)
    dic_similarity[movie] = similarity
    print( movie, desc, similarity)

max_similarity = max(list_similarity)

for key, value in dic_similarity.items():
    if value == max_similarity:
       print(f"The recommended movie is {key} with similarity score of {value}")
       



   