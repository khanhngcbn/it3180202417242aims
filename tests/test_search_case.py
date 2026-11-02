
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearchCase(unittest.TestCase):

    def test_search_case_insensitive(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("The Lion King"))

        results = search_by_title(cart, "lion")

        self.assertEqual(
            [dvd.title for dvd in results],
            ["The Lion King"]
        )


if __name__ == "__main__":
    unittest.main()
