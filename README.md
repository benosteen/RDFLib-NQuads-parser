This is a rdflib plugin for parsing NQuad files into (Conjunctive) graphs that can be used and
queried. The store that backs the graph *must* be able to handle contexts.

```python
>>> import rdflib
>>> import rdflib_nquads
>>> g = rdflib.ConjunctiveGraph()
>>> g.parse("https://raw.github.com/benosteen/master/example.nquads", format="nquads")
>>> for ctx in g.contexts():
...   print ctx
... 
http://bibliographica.org/entry/BB2682260
http://bibliographica.org/entity/E10003
http://bibliographica.org/entity/E10009
http://bibliographica.org/entity/E10007
http://bibliographica.org/entry/BB2682253
http://bibliographica.org/entity/E10006
http://bibliographica.org/entity/E10002
http://bibliographica.org/entity/E10008
http://bibliographica.org/entity/E10004
http://bibliographica.org/entity/E10001
http://bibliographica.org/entity/E10005
http://bibliographica.org/entry/BB2682251
http://bibliographica.org/entity/E10000
http://bibliographica.org/entry/BB2682246
http://bibliographica.org/entry/BB2682258
http://bibliographica.org/entry/BB2682255

# Use the context of the last one in the list
>>> for s,p,o in g.triples((None, None, None), context = ctx):
...   print s,p,o
... 
jEOnxGKk47 http://www.w3.org/2004/02/skos/core#prefLabel South African fiction (English)
jEOnxGKk47 http://www.w3.org/2004/02/skos/core#inScheme http://id.loc.gov/authorities#conceptScheme
jEOnxGKk47 http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2004/02/skos/core#Concept
http://bibliographica.org/entity/E10007 http://www.w3.org/2004/02/skos/core#prefLabel Penguin
http://bibliographica.org/entity/E10007 http://xmlns.com/foaf/0.1/name Penguin
http://bibliographica.org/entity/E10007 http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://xmlns.com/foaf/0.1/Agent
jEOnxGKk44 http://www.w3.org/2000/01/rdf-schema#label London
http://bibliographica.org/entity/E10006 http://www.w3.org/2004/02/skos/core#prefLabel Burgess, Yvonne.
http://bibliographica.org/entity/E10006 http://xmlns.com/foaf/0.1/name Burgess, Yvonne.
http://bibliographica.org/entity/E10006 http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://xmlns.com/foaf/0.1/Agent
http://bibliographica.org/entry/BB2682255.ttl http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://xmlns.com/foaf/0.1/Document
http://bibliographica.org/entry/BB2682255.ttl http://xmlns.com/foaf/0.1/primaryTopic http://bibliographica.org/entry/BB2682255
http://bibliographica.org/entry/BB2682255.rdf http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://xmlns.com/foaf/0.1/Document
http://bibliographica.org/entry/BB2682255.rdf http://xmlns.com/foaf/0.1/primaryTopic http://bibliographica.org/entry/BB2682255
jEOnxGKk46 http://www.w3.org/2000/01/rdf-schema#label 197 p
http://bibliographica.org/entry/BB2682255.n3 http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://xmlns.com/foaf/0.1/Document
http://bibliographica.org/entry/BB2682255.n3 http://xmlns.com/foaf/0.1/primaryTopic http://bibliographica.org/entry/BB2682255
http://bibliographica.org/entry/BB2682255.html http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://xmlns.com/foaf/0.1/Document
http://bibliographica.org/entry/BB2682255.html http://xmlns.com/foaf/0.1/primaryTopic http://bibliographica.org/entry/BB2682255
http://bibliographica.org/entry/BB2682255.nt http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://xmlns.com/foaf/0.1/Document
http://bibliographica.org/entry/BB2682255.nt http://xmlns.com/foaf/0.1/primaryTopic http://bibliographica.org/entry/BB2682255
jEOnxGKk45 http://www.w3.org/1999/02/22-rdf-syntax-ns#value eng
jEOnxGKk48 http://www.w3.org/2004/02/skos/core#inScheme http://dewey.info/scheme/e22

...

etc

```
