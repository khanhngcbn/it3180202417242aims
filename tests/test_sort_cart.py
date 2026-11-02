
import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSortCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(
            DigitalVideoDisc("Zootopia", cost=30.0)
        )
        self.cart.add_dvd(
            DigitalVideoDisc("Avatar", cost=20.0)
        )
        self.cart.add_dvd(
            DigitalVideoDisc("Batman", cost=10.0)
        )

    def test_sort_by_title(self):
        self.cart.sort_by_title()

        titles = [dvd.title for dvd in self.cart.items]

        self.assertEqual(
            titles,
            ["Avatar", "Batman", "Zootopia"]
        )

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()

        costs = [dvd.cost for dvd in self.cart.items]

        self.assertEqual(costs, [10.0, 20.0, 30.0])


if __name__ == "__main__":
    unittest.main()
