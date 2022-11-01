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
        """Get the price of regular movies."""
        if days > 2:
            return 2 + (1.5*(days-2))
        return 2

class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children movies."""

    def get_rental_points(self, days):
        """Children movies rentals get 1 point."""
        return 1
    
    def get_price(self, days):
        """Get the price of children movies."""
        if days > 3:
            return 1.5 + (1.5*(days-3))
        return 1.5