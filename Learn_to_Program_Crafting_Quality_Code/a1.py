def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(115)
    3
    """

    if n % 50 == 0:
        return n / 50

    else:
        return (n//50) + 1


def stock_prices_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_prices_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    gains = 0
    losses = 0
    for price in price_changes:
        if price > 0:
            gains += price

        elif price < 0:
            losses += price

    return round(gains, 2), round(losses, 2)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

    if k == 0:
        pass

    else:
        oldval = L[:k]
        L[:k] = L[-k:]
        L[-k:] = oldval

if __name__ == '__main__':
    import doctest
    doctest.testmod()
