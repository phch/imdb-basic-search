from whoosh.fields import SchemaClass, ID, TEXT
from whoosh.index import create_in
from whoosh.qparser import MultifieldParser
import os

class IMDbIndexSchema(SchemaClass):
    rank = ID(stored=True)
    title = TEXT(stored=True)
    year = TEXT(stored=True)
    rating = TEXT(stored=True)
    main_people = TEXT(stored=True)

class IMDbIndex:
    def __init__(self):
        if not os.path.exists('indexdir'):
            os.mkdir('indexdir')
        self.schema = IMDbIndexSchema()
        self.index = create_in('indexdir', self.schema)
        self.parser = MultifieldParser(['rank', 'title', 'year', 'main_people'], schema=self.schema)
    
    def bulk_index(self, movies):
        writer = self.index.writer()
        for movie in movies:
            writer.add_document(rank=movie['rank'], title=movie['title'], year=movie['year'], rating=movie['rating'], main_people=movie['main_people'])
        writer.commit()

    def search(self, search_term, result_limit=10):
        query = self.parser.parse(search_term)
        with self.index.searcher() as searcher:
            search_result = {'search_term': str(search_term), 'matches': list()}
            results = searcher.search(query, limit=result_limit)
            for i in range(len(results)):
                search_result['matches'].append(dict(results[i]))

            return search_result