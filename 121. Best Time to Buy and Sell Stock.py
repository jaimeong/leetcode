# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.


##

###



def stonks(nums):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    if(len(nums) <= 1):
        return 0

    profit = 0
    min_price = nums[0]

    for each in nums:
        min_price = min(min_price, each)
        profit = max(profit, each - min_price)



    return profit






print(stonks([7,1,5,3,6,4]))