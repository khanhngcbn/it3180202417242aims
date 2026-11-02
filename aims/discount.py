def apply_discount(total, percent):
    if not 0 <= percent <= 100:
        raise ValueError("Invalid discount percent")

    return total * (100 - percent) / 100
