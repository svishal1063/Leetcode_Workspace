prices = [2,4,1]
l,r = 0,1 
best_profit = 0 

while r < len(prices):
    if prices[l] < prices[r]:
        best_profit = max((prices[r]-prices[l],best_profit))
    else:
        l = r 
    r += 1 

print(best_profit)

## this problem uses the sliding window/
## two pointer approach to solve the problem.