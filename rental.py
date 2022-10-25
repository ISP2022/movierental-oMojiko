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

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        """Get the movie name."""
        return self.movie

    def get_days_rented(self):
        """Get the days that customer rent"""
        return self.days_rented

    def get_price(self):
        """Get the total price of the movie."""
        try:
            amount = self.movie.get_price(days=self.days_rented)
        except:
            log = logging.getLogger()
            log.error(
                f"Movie {self.get_movie()} has unrecognized priceCode {self.get_movie().get_price_code()}")
        return amount

    def get_rental_points(self):
        """Get the total rental points of the movie."""
        return self.movie.get_rental_points(days=self.days_rented)
