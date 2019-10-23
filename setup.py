from setuptools import setup

setup(
    name='imdb_search',
    version='0.1',
    packages=['imdb_search'],
    install_requires=[
        'requests',
        'beautifulsoup4'
    ]
)