import scrapy
from imdb_scrapy.items import IMDbMovie

# Adapted based on https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3
class IMDbTop1000Spider(scrapy.Spider):
    name = "imdb_top_1000_spider"
    start_urls = ['https://www.imdb.com/search/title/?groups=top_1000&amp&sort=user_rating&amp&view=simple']

    def parse(self, response):
        MOVIE_LISTING_SELECTOR = '.lister-item .lister-item-content'
        for movie_listing in response.css(MOVIE_LISTING_SELECTOR):
            MOVIE_RANK = '.lister-item-index ::text'
            MOVIE_TITLE_SELECTOR = 'a ::text'
            MOVIE_YEAR_SELECTOR = '.lister-item-year ::text'
            MOVIE_MAIN_PEOPLE_SELECTOR = 'span ::attr("title")'
            MOVIE_RATING = '.col-imdb-rating strong ::attr("title")'

            movie = IMDbMovie()
            movie['rank'] = movie_listing.css(MOVIE_RANK).extract_first().rstrip('.')
            movie['title'] = movie_listing.css(MOVIE_TITLE_SELECTOR).extract_first()
            movie['year'] = movie_listing.css(MOVIE_YEAR_SELECTOR).extract_first()
            movie['main_people'] = [x.strip() for x in movie_listing.css(MOVIE_MAIN_PEOPLE_SELECTOR).extract_first().replace('(dir.)', '').split(',')]
            movie['rating'] = movie_listing.css(MOVIE_RATING).extract_first()
            yield movie # Sends the scrapy item to pipeline
            
        NEXT_PAGE_SELECTOR = '.lister-page-next ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )