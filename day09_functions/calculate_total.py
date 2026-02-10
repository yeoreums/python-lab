def calculate_total(prices):
    a = 0

    for price in prices:
        if price >= 0:
            a += price
    
    a = a + (a / 10)
    return a



prices = [100, 200, -50, 300]

result = calculate_total(prices)
print(result)
