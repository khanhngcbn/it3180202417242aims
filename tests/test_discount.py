import unittest
from aims.discount import apply_discount


class TestDiscount(unittest.TestCase):

    def test_discount_20_percent(self):
        result = apply_discount(100, 20)
        self.assertEqual(result, 80)

    def test_invalid_percent(self):
        with self.assertRaises(ValueError):
            apply_discount(100, 150)


if __name__ == "__main__":
    unittest.main()
