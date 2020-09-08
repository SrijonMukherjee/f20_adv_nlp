import pysolr

#solr = pysolr.Solr('http://localhost:8983/solr/', always_commit=True, [timeout=10], [auth=<type of authentication>])

solr = pysolr.Solr('http://localhost:8983/solr/newswatch')

solr.ping()

solr.delete(q='*:*')

# solr.add([
#     {
#         "id": "doc_1",
#         "title": "A test document",
#     },
#     {
#         "id": "doc_2",
#         "title": "The Banana: Tasty or Dangerous?",
#         "_doc": [
#             { "id": "child_doc_1", "title": "peel" },
#             { "id": "child_doc_2", "title": "seed" },
#         ]
#     },
# ])

solr.commit()