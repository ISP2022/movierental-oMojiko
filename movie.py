from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class (interface) for rental pricing."""

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals get 1 point per day rented."""
        return days
    
    def get_price(self, days):
        return 3*days
    
class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_rental_points(self, days):
        """Regular movies rentals get 1 point."""
        return 1
    
    def get_price(self, days):
        if days > 2:
            return 2 + (1.5*(days-2))
        return 2

class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children movies."""

    def get_rental_points(self, days):
        """Children movies rentals get 1 point."""
        return 1
    
    def get_price(self, days):
        if days > 3:
            return 1.5 + (1.5*(days-3))
        return 1.5

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrensPrice()

    def __init__(self, title, price_code):
           # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    
    def get_price(self, days):
        return self.price_code.get_price(days)

    
    def get_rental_points(self, days):
        return self.price_code.get_rental_points(days)

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title

