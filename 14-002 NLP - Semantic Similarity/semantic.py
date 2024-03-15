import spacy

# Running the programs in the dropbox pdf and my own example using different models and evaluating results.
print('---------Program using md version of the language model------')

nlp = spacy.load('en_core_web_md')
tokens = nlp('cat apple monkey banana')

# Iterating through each token and calculating similarity
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print('''\nThe medium version works well in this case as it calculates the similarity accurately as explained below.\n
It's calculating highest similarity in cat, monkey which is accurate as they are both animals.\n
The second highest similarity is in monkey and banana which is also accurate.\n
There is least similarity between Cat and banana.''')
        
print()
print('---------Program using sm version of the language model------')

nlp = spacy.load('en_core_web_sm')
tokens = nlp('cat apple monkey banana')

# Iterating through each token and calculating similarity
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print('''\nThe small version of the NLP model is less accurate than the medium version.\n
It's calculating higher similarity between apple and monkey versus monkey and cat which is inaccurate\n
Also the score of apple and monkey is higher than banana and monkey which is also inaccurate.''')
        

# Running my own example using different models and evaluating results.
# Running my own example using md model.
print()
print('------Program using own example with md version of the model------')

nlp = spacy.load('en_core_web_md')
tokens = nlp('pen eraser ink pencil')

# Iterating through each token and calculating similarity
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print('''\nThe md model seems to be working in most cases however it has limitations as explained below.\n
The highest similarity score is between pencil and pen which is correct as they serve the same purpose.\n
However ink and pencil score higher than ink and pen which does not make sense.\n''')

# Running my own example using sm model.
print()
print('------Program using own example with sm version of the model------')

nlp = spacy.load('en_core_web_sm')
tokens = nlp('pen eraser ink pencil')

# Iterating through each token and calculating similarity
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print('''\nThe sm model is not working correctly in my example as explained below.\n
The highest similarity score is between ink and eraser which is incorrect.\n
Pen and pencil have scored the least in similarity which is also inaccurate.\n''') 