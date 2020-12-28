# Introduction
This was a simple and quick coding exercise to implement search on the top IMDb movies listed here: http://www.imdb.com/search/title?groups=top_1000&amp;sort=user_rating&amp;view=simple. It's a dabble into web crawling, indexing, and search using prebuilt modules in Python.

# Setup
```bash
git clone https://github.com/phch/imdb-basic-search.git imdb-basic-search
cd imdb-basic-search
python3 setup.py install
```

# Usage
## Start Local Server
The following command will scrape the URL for top IMDb movies, index them, and start a local server on port 5000 so you can execute queries.
```bash
cd imdb_search
flask run
```

## Querying the Index
You can query the index based on a URL-encoded search term. This search term comes after the "q=" portion.
```bash
curl "localhost:5000/search?q=patrick%20stewart"
curl "localhost:5000/search?q=future"
```
