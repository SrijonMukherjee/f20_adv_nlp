# Can we build out a script to index documents along with the entities?
"""EDIT BY MATT WILCHEK FOR HOMEWORK 1 SUBMISSION"""
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

from os import listdir
import os
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/newswatch')
solr.delete(q='*:*')
os.chdir(r'C:\Users\chels\OneDrive\Documents\Matt_NLP\f20_adv_nlp\sample_data\news_data')
data_dir = os.getcwd()

index_files = [file for file in listdir(data_dir)]
index_contents = []

counter = 0
for index_file in index_files:
    text = open(os.path.join(data_dir, index_file), "r")
    content = text.read()

    doc = nlp(content)

    # Add organization and location entity lists
    person_entities = []
    org_entities = []
    loc_entities = []

    # Add conditions if entity equals organization or location, then add if unique
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            if ent.text not in person_entities:
                person_entities.append(ent.text)
        if ent.label_ == "ORG":
            if ent.text not in org_entities:
                org_entities.append(ent.text)
        if ent.label_ == "LOC":
            if ent.text not in loc_entities:
                loc_entities.append(ent.text)

    # Add lists to temporary document dictionary
    temp_document = {"content_txt": content, "people_ss": person_entities, "organizations_ss": org_entities,
                     "locations_ss": loc_entities}

    # Close documnt
    text.close()
    # print(temp_document["entities_txt"])
    # Add document dictionary to list of parsed documents
    index_contents.append(temp_document)
    counter += 1
    # if counter == 5:
    #     break

# Solr add all parsed documents
solr.add(index_contents)
# Solr save commit of parsed documents
solr.commit()
