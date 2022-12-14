import unittest
from movie import MovieCatalog
from rental import Rental
from customer import Customer
import re


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        catalog = MovieCatalog()
        self.new_movie = catalog.get_movie("Top Gun: Maverick")
        self.regular_movie = catalog.get_movie("Mulan")
        self.childrens_movie = catalog.get_movie("Frozen")

    @unittest.skip("No convenient way to test")
    def test_billing():
        # no convenient way to test billing since its buried in the statement() method.
        pass

    def test_statement(self):
        """Test to check the statement of customer."""
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertEqual(0.0 , self.c.get_total_charge())
        self.assertEqual(0, self.c.get_total_rental_points())
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertEqual(12.0 , self.c.get_total_charge())
        self.assertEqual(4, self.c.get_total_rental_points())
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
