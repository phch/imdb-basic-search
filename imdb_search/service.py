import requests
from bs4 import BeautifulSoup

class Movie:
    def __init__(self, title, director, stars, year):
        self.title = title
        self.director = director
        self.stars = stars
        self.year = year

def scrape(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def process(soup):
    movies_metadata = soup.find_all('div', {'class': 'col-title'})
    print(movies_metadata)

if __name__ == '__main__':
    soup = scrape('https://www.imdb.com/search/title/?groups=top_1000&amp&sort=user_rating&amp&view=simple')
    process(soup)