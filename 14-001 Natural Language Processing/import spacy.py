import spacy
nlp = spacy.load ('en_core_web_sm')
doc = nlp ("This is a toekn string")

"""
for token in doc:
   print(token.text, token.pos_)
   """
   
print([(w.text,w.pos_) for w in doc])


 

