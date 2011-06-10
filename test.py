from unittest import TestCase

from rdflib import ConjunctiveGraph, URIRef, Namespace, RDF, BNode

import rdflib_nquads

class NQuadsParserTest(TestCase):

    def _load_example(self):
        g = ConjunctiveGraph()
        with open("example.nquads", "r") as examples
            g.parse(examples, format="nquads")
        return g
      
    def test_01_simple_open(self):
        g = self._load_example()
        assert len(g.store) == 449

    def test_02_contexts(self):
        # There should be 16 separate contexts
        g = self._load_example()
        assert len([x for x in g.store.contexts()]) == 16
    
    def test_03_get_value(self):
        # is the name of entity E10009 "Arco Publications"? (in graph http://bibliographica.org/entity/E10009)
        # Looking for:
        # <http://bibliographica.org/entity/E10009> <http://xmlns.com/foaf/0.1/name> "Arco Publications" <http://bibliographica.org/entity/E10009>
        
        s = URIRef("http://bibliographica.org/entity/E10009")
        FOAF = Namespace("http://xmlns.com/foaf/0.1/")
        subgraph = 
        self.assertEqual(g.value(s, FOAF.name), "Arco Publications")

