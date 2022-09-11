## Besst Time to Buy and Sell Stock
## Time Complexity :- O(n)
## Space Complexity :- O(1)

## function definition
def findMaxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit


## Driver code
# prices = [7, 5, 3, 6, 4, 15, 20]
# prices = [7, 3, 5, 6, 20, 1, 2]

input_test = '7,3,5,6,20,1,2'
prices = list(map(int, input_test.split(",")))
## function calling
max_profit = findMaxProfit(prices)
print(max_profit)