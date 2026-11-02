
def search_by_category(cart, category):
    return [
        dvd for dvd in cart.items
        if category.lower() in dvd.category.lower()
    ]


def search_by_title(cart, keyword):
    results = []

    for dvd in cart.items:
        if keyword.lower() in dvd.title.lower():
            results.append(dvd)

    return results
