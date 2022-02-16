def maximumToys(prices, k):
    toys = 0
    prices.sort()
    for price in prices:
        if k - price >= 0:
            k -= price
            toys += 1
        else:
            break

    return toys
