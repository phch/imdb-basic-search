from scrapy import signals
from scrapy.crawler import Crawler, CrawlerProcess
from scraper import IMDbTop1000Spider
from index import IMDbIndex
from flask import Flask, request

app = Flask(__name__)

# Crawl the service using our spider and store it in a list 
movies = []
def collect_items(item, response, spider):
    movies.append(item)

crawler = Crawler(IMDbTop1000Spider)
crawler.signals.connect(collect_items, signals.item_scraped)
process = CrawlerProcess()
process.crawl(crawler)
process.start() # block until finished

# Index this data to Whoosh
imdb_index = IMDbIndex()
imdb_index.bulk_index(movies)

@app.route('/search', methods=['GET'])
def index():
    search_term = request.args.get('q', type=str)
    return imdb_index.search(search_term)