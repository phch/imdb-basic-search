from setuptools import setup

setup(
    name='imdb_search',
    version='0.1',
    install_requires=[
        'service_identity',
        'scrapy', # used to crawl website and parse data
        'whoosh', # used to index documents and search
        'flask'   # used to host development server
    ]
)