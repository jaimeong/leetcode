# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:

# Input: coins = [2], amount = 3
# Output: -1

# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

# Example 4:

# Input: coins = [1], amount = 1
# Output: 1

# Example 5:

# Input: coins = [1], amount = 2
# Output: 2

 

# Constraints:

#     1 <= coins.length <= 12
#     1 <= coins[i] <= 231 - 1
#     0 <= amount <= 104
"""
target = 11
coins = [1,2,5]

Approach #1: greedy
5, 5, 1  = 3

Solution #1: dynamic programming
target = 11
coins = [1,2,5]

cc(11) = cc(10) + 1
cc(10) = cc(9) + 1
cc(9) = cc(8) + 1
.
.
cc(5) = min(cc(4) + 1, new coin)
cc(4) = min(cc(3) + 1, new coin)
cc(3) = min(cc(2) + 1, new coin)
cc(2) = min(cc(1) + 1, new coin)
cc(1) = 1
cc(0) = 0


"""

# def cc(coins, amount):
# 	ans = [1 for i in range(amount+1)]
# 	ans[0] = 0


# 	for i in range(1, amount+1):
# 		for each in coins:
# 			if amount-each >= 0:
# 				ans[i] = min(ans[amount-each]+1, ans[i])
# 	print(ans)
# 	return ans[-1]
#   #return dp[amount] if dp[amount] != amount + 1 else -1

def cc(coins, amt):
    alist = [amt+1 for i in range(amt+1)]
    alist[0] = 0
    for i in range(amt+1):
        for each in coins:
            if i - each >= 0:
                alist[i] = min(alist[i], alist[i-each]+1)

    print(alist)
    return alist[-1]



print(cc([1,2,5], 11))