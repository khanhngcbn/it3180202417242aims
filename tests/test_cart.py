
import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        # Thêm 20 DVD, tất cả phải thành công
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(
                title=f"DVD {i + 1}",
                cost=10.0
            )
            result = cart.add_dvd(dvd)
            self.assertTrue(result)

        # Kiểm tra giỏ hàng có đúng 20 DVD
        self.assertEqual(
            len(cart.items),
            MAX_NUMBERS_ORDERED
        )

        # Thêm DVD thứ 21, phải bị từ chối
        extra_dvd = DigitalVideoDisc(
            title="DVD 21",
            cost=10.0
        )

        result = cart.add_dvd(extra_dvd)

        self.assertFalse(result)

        # Giỏ hàng vẫn chỉ được chứa 20 DVD
        self.assertEqual(
            len(cart.items),
            MAX_NUMBERS_ORDERED
        )


if __name__ == "__main__":
    unittest.main()
