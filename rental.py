from datetime import datetime
from pricing import *
from movie import Movie
import logging


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrensPrice()

    def __init__(self, movie: Movie, days_rented: int):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

        price_code = self.price_code_for_movie()
        self.price_code = price_code
    
    def price_code_for_movie(self) -> PriceStrategy:
        """Calculate price code for movie."""
        if self.movie.year == datetime.now().year:
            return self.NEW_RELEASE
        elif self.movie.is_genre("Children") or self.movie.is_genre("Childrens"):
            return self.CHILDRENS
        else:
            return self.REGULAR
    

    def get_movie(self) -> Movie:
        """Get the movie name."""
        return self.movie.title

    def get_price_code(self) -> PriceStrategy:
        return self.price_code

    def get_days_rented(self):
        """Get the days that customer rent"""
        return self.days_rented

    def get_price(self):
        """Get the total price of the movie."""
        amount = 0
        try:
            amount += self.get_price_code().get_price(self.get_days_rented())
        except AttributeError:
            log = logging.getLogger()
            log.error(f"Movie {self.get_movie()} has unrecognized priceCode {self.get_price_code()}")
        return amount

    def get_rental_points(self):
        """Get the total rental points of the movie."""
        return self.get_price_code().get_rental_points(self.get_days_rented())
    
