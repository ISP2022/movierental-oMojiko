import unittest
from rental import Rental
from movie import MovieCatalog


class RentalTest(unittest.TestCase):

    def setUp(self):
        catalog = MovieCatalog()
        self.new_movie = catalog.get_movie("Top Gun: Maverick")
        self.regular_movie = catalog.get_movie("Almost Holy")
        self.childrens_movie = catalog.get_movie("Cinderella")

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        self.assertEqual("Top Gun: Maverick", self.new_movie.get_title())
        self.assertEqual(2022, self.new_movie.year)
        self.assertEqual(['action', 'drama'], self.new_movie.genre)

    def test_rental_price(self):
        """test to check the rental price that implement correctly."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_price(), 5.0)
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.childrens_movie, 2)
        

    def test_rental_points(self):
        """test to check the rental points that implement correctly."""
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(self.childrens_movie, 10)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 99)
        self.assertEqual(rental.get_rental_points(), 1)
