"""
1442. 形成两个异或相等数组的三元组数目
给你一个整数数组 arr 。

现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。

a 和 b 定义如下：

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
注意：^ 表示 按位异或 操作。

请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。

 

示例 1：

输入：arr = [2,3,1,6,7]
输出：4
解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
示例 2：

输入：arr = [1,1,1,1,1]
输出：10
示例 3：

输入：arr = [2,3]
输出：0
示例 4：

输入：arr = [1,3,5,7,9]
输出：3
示例 5：

输入：arr = [7,11,12,9,5,2,7,17,22]
输出：8
 

提示：

1 <= arr.length <= 300
1 <= arr[i] <= 10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter
from typing import List


class Solution:
    def countTriplets1(self, arr: List[int]) -> int:
        """
        思路：
        1. 由题意得，arr[i]^……^arr[k]==0,k>i，我们可以想到前缀和
        2. 如果pre[i]==pre[k]，k>=i+2那么[i+1,k]之间所有数都满足条件
        @param arr:
        @return:
        """
        n = len(arr)
        res = 0
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] ^ arr[i]
        # arr[i]^……^arr[k]==0,k>i
        for i in range(n):
            for k in range(i + 2, n + 1):
                if pre[i] == pre[k]:
                    res += k - i - 1
        return res

    def countTriplets2(self, arr: List[int]) -> int:
        """
        思路：
        1. 在j1,j2,……,jm中都满足，则总数为(i-j1)+(i-j2)+……+(i-jm)
        2. 所以需要统计i的个数和（j1+j2+……+jm）
        @param arr:
        @return:
        """
        n = len(arr)
        res = 0
        pre = 0
        cnt, total = Counter(), Counter()
        for i in range(n):
            t = pre ^ arr[i]
            if t in cnt:
                res += cnt[t] * i - total[t]
            cnt[pre] += 1
            total[pre] += i
            pre = t

        return res


if __name__ == '__main__':
    arr = [2, 3, 1, 6, 7]
    print(Solution().countTriplets1(arr))
    print(Solution().countTriplets2(arr))
