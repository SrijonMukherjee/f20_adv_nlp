# Can we build out a script to index documents?

# basic plan:
# List documents in directory
# loop through documents
# read document contents
# structure document for insertion
# insert
# occasional force commits

from os import listdir
import os
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/newswatch')

data_dir = "/Users/teacher/repos/f20_adv_nlp/sample_data/news_data"

index_files = [file for file in listdir(data_dir)]
index_contents = []

for index_file in index_files:
    text = open(os.path.join(data_dir, index_file), "r")
    content = text.read()
    temp_document = {}
    temp_document["content_txt"] = content
    text.close()
    index_contents.append(temp_document)

solr.add(index_contents)
solr.commit()

