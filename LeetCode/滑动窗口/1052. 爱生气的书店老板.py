"""
1052. 爱生气的书店老板
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
 

示例：

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 

提示：

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxSatisfied1(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        arr = [0] * (n + 1)
        window = [0] * (n + 1)
        pre = 0
        presum = 0
        for i in range(n):
            pre += customers[i] * (1 - grumpy[i])
            arr[i + 1] = pre
            presum += customers[i]
            if i >= X - 1:
                window[i + 1] = presum
                presum -= customers[i - X + 1]

        print(window, arr)
        res = float('-inf')
        for i in range(X, n + 1):
            res = max(res, arr[i - X] + window[i] + arr[-1] - arr[i])
            print(i, res)
        return res

    def maxSatisfied2(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        total = sum([a for a, b in zip(customers, grumpy) if b == 0])
        res = 0
        max_ = 0
        for i in range(n):
            res += customers[i] * grumpy[i]
            if i >= X - 1:
                max_ = max(max_, res)
                res -= customers[i - X + 1] * grumpy[i - X + 1]
        return total + max_


if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    print(Solution().maxSatisfied1(customers, grumpy, X))
    print(Solution().maxSatisfied2(customers, grumpy, X))
