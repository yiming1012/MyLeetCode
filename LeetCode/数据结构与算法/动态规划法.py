# -*- coding:utf-8 -*-
import sys

# 需要用硬币凑满的钱数
amount = 12
# 硬币的种类
coins = [1, 3, 5]


def coin_dynamic(amount, coins):
    dp = [0]
    for i in range(1, amount + 1):
        dp.append(sys.maxsize)
        for j in range(len(coins)):
            if coins[j] <= i and dp[i - coins[j]] + 1 < dp[i]:
                dp[i] = dp[i - coins[j]] + 1
    return dp


aa = coin_dynamic(amount, coins)
print(aa)


