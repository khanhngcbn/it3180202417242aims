
import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        # Thêm 20 DVD
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(
                title=f"DVD {i + 1}",
                cost=10.0
            )
            self.assertTrue(cart.add_dvd(dvd))

        self.assertEqual(
            len(cart.items), MAX_NUMBERS_ORDERED
        )

        # Thử thêm DVD thứ 21
        extra = DigitalVideoDisc("DVD 21", cost=10.0)
        result = cart.add_dvd(extra)

        self.assertFalse(result)
        self.assertEqual(
            len(cart.items), MAX_NUMBERS_ORDERED
        )


if __name__ == "__main__":
    unittest.main()
