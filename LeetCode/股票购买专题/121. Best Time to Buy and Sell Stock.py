'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了98.52%的用户
        内存消耗 :14.2 MB, 在所有 Python3 提交中击败了25.38%的用户
        :param prices:
        :return:
        '''
        if len(prices) <= 1:
            return 0
        minValue = prices[0]
        profit = 0

        for i in prices[1:]:
            if i < minValue:
                minValue = i
            else:
                profit = max(i - minValue, profit)
        return profit


'''
本题的关键：找到最小值minValue，i往后面遍历，计算（i-minValue）。最小值必须在i的前面
'''
if __name__ == '__main__':
    arr = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(arr))
