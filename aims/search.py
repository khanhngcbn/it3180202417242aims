
def search_by_title(cart, keyword):
    results = []

    for dvd in cart.items:
        if keyword.lower() in dvd.title.lower():
            results.append(dvd)

    return results
