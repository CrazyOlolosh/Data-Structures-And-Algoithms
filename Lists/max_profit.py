def max_profit(prices):
    profit = 0
    buy_for = prices[0]
    for price in prices:
        if price < buy_for:
            buy_for = price
        elif price - buy_for > profit:
            profit = price - buy_for
    return profit


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Maximum profit:", profit)


"""
    EXPECTED OUTPUT:
    ----------------
    Maximum profit: 5
"""


def max_profit_2(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit
