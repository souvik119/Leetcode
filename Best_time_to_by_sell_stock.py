'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

# This is a sliding window problem
# Max profit can be found by taking min buy price and max sell price
# Two pointers left and right
# Left pointer starts at index 0 and right pointer starts at index 1
# if value of right pointer is less than left pointer then move left to right, means always find lowest buying price
# right value should always be greater than left
# keep moving right to next element to find max profit

# Mem : O(1) since we did not use any extra ds
# Time : O(n) since scan the array one time

def max_profit(prices):
    # left is by, right is sell
    l, r = 0, 1
    maxProfit = 0

    while r < len(prices):
        # is this profitable transaction
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1
    
    return maxProfit

if __name__ == '__main__':
    print(max_profit([7,1,5,3,6,4]))
    print(max_profit([7,6,4,3,1]))