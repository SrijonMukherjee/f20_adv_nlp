# Can we build out a script to index documents along with the entities?

# basic plan:
# List documents in directory
# loop through documents
# read document contents
# -> process document entities
# structure document for insertion
# insert
# occasional force commits


import spacy
nlp = spacy.load("en_core_web_sm")
