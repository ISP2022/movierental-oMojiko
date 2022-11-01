import csv

class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str, year: int, genre: list[str]):
        # Initialize a new movie.
        self.__title = title
        self.__year = year
        self.__genre = [ g.lower() for g in genre]

    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def year(self) -> int:
        return self.__year

    @property
    def genre(self):
        return self.__genre

    def is_genre(self, g: str) -> bool:
        return g.lower() in self.genre
        
    def get_title(self) -> str:
        return self.title

    def __str__(self) -> str:
        return f'{self.title} ({self.year})'


class MovieCatalog:

    def __init__(self):
        with open("movies.csv", 'r') as file:
            movies_lst = list(csv.reader(file))
            self.movies_collection = [Movie(title=movies[1],year=int(movies[2]), genre=movies[3].split("|")) for movies in movies_lst[2:]]
        
    def get_movie(self, title:str, year=0) -> Movie:
        for movie in self.movies_collection:
            if year == 0:
                if title == movie.title:
                    return movie
            elif year != 0:
                if title == movie.title and year == movie.year:
                    return movie
        

    
    