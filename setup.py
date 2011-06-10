from setuptools import setup

setup(
    name = 'rdflib-nquads',
    version = '0.1',
    description = "rdflib extension for parsing NQuad into an rdf store, via a given Graph",
    author = "Ben O'Steen",
    author_email = "bosteen@gmail.com",
    url = "http://github.com/benosteen/rdflib-nquads",
    py_modules = ["rdflib_nquads"],
    test_suite = "test",
    install_requires = ["rdflib>=3.0"],
)
