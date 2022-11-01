import unittest
from movie import MovieCatalog
from rental import Rental
import datetime
from pricing import PriceStrategy


class PricingTest(unittest.TestCase):
    def setUp(self):
        self.new_movie = MovieCatalog().get_movie("The Batman")
        self.regular_movie = MovieCatalog().get_movie("No Time to Die")
        self.children_movie = MovieCatalog().get_movie("Mulan")

    def test_price_code_new_releases(self):

        rental = Rental(self.new_movie, 1)
        self.assertEqual(Rental.NEW_RELEASE, rental.price_code_for_movie())

    def test_price_code_childrens(self):

        rental = Rental(self.children_movie, 1)
        self.assertEqual(Rental.CHILDRENS, rental.price_code_for_movie())

    def test_price_code_regular(self):

        rental = Rental(self.regular_movie, 1)
        self.assertEqual(Rental.REGULAR, rental.price_code_for_movie())

    def test_price_code_attribute(self):
        rental_new_movie = Rental(self.new_movie, 3)
        self.assertEqual(Rental.NEW_RELEASE, rental_new_movie.get_price_code())
        rental_children_movie = Rental(self.children_movie, 5)
        self.assertEqual(Rental.CHILDRENS, rental_children_movie.get_price_code())
        rental_regular_movie = Rental(self.regular_movie, 7)
        self.assertEqual(Rental.REGULAR, rental_regular_movie.get_price_code())