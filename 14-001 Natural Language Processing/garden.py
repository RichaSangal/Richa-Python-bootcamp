
import spacy

#process text using the model
nlp = spacy.load('en_core_web_sm')
gardenpathsentences = ["The old man the boat.", 
                       "The horse raced past the barn fell.", 
                       "Mary gave the child a band-aid.", 
                       "That Jill is never here hurts.", 
                       "the cotton clothing is made of grows in Mississippi."]

# using forloop to interate each sentence in the list 
# And process each sentence using the model
for sentence in range (0,len(gardenpathsentences)):
    doc = nlp(gardenpathsentences[sentence])
    
    #using for loop to iterate each token and getting labels and entities
    print([(token.text,token.label_,token.label) for token in doc.ents])

# Get explanation of entities and printing
print(f'PERSON:{spacy.explain("PERSON")}')
print(f'GPE:{spacy.explain("GPE")}')





