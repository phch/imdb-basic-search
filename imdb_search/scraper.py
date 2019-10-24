import scrapy

class IMDbMovie(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    main_people = scrapy.Field()

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
            MOVIE_RATING = '.col-imdb-rating strong ::attr("title")'
            MOVIE_MAIN_PEOPLE_SELECTOR = 'span ::attr("title")'

            movie = IMDbMovie()
            movie['rank'] = movie_listing.css(MOVIE_RANK).extract_first().rstrip('.')
            movie['title'] = movie_listing.css(MOVIE_TITLE_SELECTOR).extract_first()
            movie['year'] = movie_listing.css(MOVIE_YEAR_SELECTOR).extract_first()
            movie['rating'] = movie_listing.css(MOVIE_RATING).extract_first()
            movie['main_people'] = movie_listing.css(MOVIE_MAIN_PEOPLE_SELECTOR).extract_first()
            yield movie
            
        NEXT_PAGE_SELECTOR = '.lister-page-next ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )