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

from os import listdir
import os
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/newswatch')
solr.delete(q='*:*')
data_dir = "/Users/teacher/repos/f20_adv_nlp/sample_data/news_data"

index_files = [file for file in listdir(data_dir)]
index_contents = []

counter = 0
for index_file in index_files:
    text = open(os.path.join(data_dir, index_file), "r")
    content = text.read()

    doc = nlp(content)
    entities = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            if ent.text not in entities:
                entities.append(ent.text)

    temp_document = {}
    temp_document["content_txt"] = content
    temp_document["entities_ss"] = entities #" - ".join(entities)
    text.close()
    #print(temp_document["entities_txt"])
    index_contents.append(temp_document)
    counter += 1
    # if counter == 5:
    #     break

solr.add(index_contents)
solr.commit()