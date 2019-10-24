# IMDbSearch
Coding exercise to implement IMDb search for the top 1000 IMDb movies listed at http://www.imdb.com/search/title?groups=top_1000&amp;sort=user_rating&amp;view=simple.

# Usage
## Installing Dependencies
```bash
python3 setup.py install
```
## Crawl IMDb Top 1000
Navigate to IMDbSearch/imdb_scrapy and run the command:
```bash
scrapy crawl imdb_top_1000_spider -o items.json -t json
```

Now, the data is loaded into an "items.json" which you will now need to index.

## Index Movie Listing
TODO