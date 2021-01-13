"""
1191. K 次串联后最大子数组之和
给你一个整数数组 arr 和一个整数 k。

首先，我们要对该数组进行修改，即把原数组 arr 重复 k 次。

举个例子，如果 arr = [1, 2] 且 k = 3，那么修改后的数组就是 [1, 2, 1, 2, 1, 2]。

然后，请你返回修改后的数组中的最大的子数组之和。

注意，子数组长度可以是 0，在这种情况下它的总和也是 0。

由于 结果可能会很大，所以需要 模（mod） 10^9 + 7 后再返回。



示例 1：

输入：arr = [1,2], k = 3
输出：9
示例 2：

输入：arr = [1,-2,1], k = 5
输出：2
示例 3：

输入：arr = [-1,-2], k = 7
输出：0


提示：

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4
"""
from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        presum = [arr[0]]
        for i in range(1, n):
            presum.append(presum[-1] + arr[i])

        suffix = [arr[-1]]
        for i in range(n - 2, -1, -1):
            suffix.append(suffix[-1] + arr[i])

        def count(a):
            pre = 0
            res = 0
            for i, num in enumerate(a):
                if pre <= 0:
                    pre = num
                else:
                    pre += num
                res = max(res, pre)
            return res

        s1 = sum(arr)
        s2 = count(arr)
        s3 = count(arr * 2)

        ans = s2
        if k == 1:
            ans = max(ans, s1)
        else:
            ans = max(ans, s3, max(presum) + (k - 2) * s1 + max(suffix))
        return ans % mod


if __name__ == '__main__':
    arr = [1, 2]
    k = 3
    print(Solution().kConcatenationMaxSum(arr, k))
