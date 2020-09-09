# Can we build out a to search for things and analyze them for us?

# basic plan:
# we need to find documents about:
#   Tony Blair
#   Gordon Brown
#   Michael Howard
#   NHS
#   UKIP

# once we have found these we want to scan threw them for other people and organizations

# how might we do this?
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/newswatch')

query_base = ["tony blair"]

for query in query_base:
    results = solr.search(q="content_txt:" + query)
    for result in results:
        print(result)
    