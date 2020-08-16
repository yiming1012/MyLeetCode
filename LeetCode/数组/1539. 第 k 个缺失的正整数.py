"""
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。

请你找到这个数组里第 k 个缺失的正整数。



示例 1：

输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
示例 2：

输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。


提示：

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j]

"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # 三种情况:左中右
        res = 0
        l = arr[0]
        if l > k:
            return k

        r = arr[-1]
        n = len(arr)
        if r - n < k:
            return k + n

        count = l - 1
        j = 0
        res = l - 1
        while count < k:
            res += 1
            if j < n and arr[j] == res:
                j += 1
            else:
                count += 1
        return res
