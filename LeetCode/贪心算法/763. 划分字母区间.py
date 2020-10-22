"""
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

 

示例 1：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-labels
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
import itertools
from typing import List


class Solution:
    def partitionLabels1(self, S: str) -> List[int]:
        """
        思路：动态规划法
        @param S:
        @return:
        """
        n = len(S)
        dp = [1] * n
        for i in range(1, n):
            flag = False
            for j in range(i):
                if S[i] == S[j]:
                    flag = True
                    dp[i] = dp[j]
                if flag:
                    dp[j] = dp[i]
            if not flag:
                dp[i] = dp[i - 1] + 1
        # print(dp)
        return [len(list(v)) for k, v in itertools.groupby(dp)]

    def partitionLabels2(self, S: str) -> List[int]:
        """
        思路：贪心算法
        @param S:
        @return:
        """
        index = collections.defaultdict()
        for i, c in enumerate(S):
            index[c] = i
        res = []
        start = 0
        end = index[S[0]]
        for i, c in enumerate(S):
            if i <= end:
                if index[c] > end:
                    end = index[c]
            else:
                res.append(end - start + 1)
                start = i
                end = index[S[i]]
            if i == len(S) - 1:
                res.append(end - start + 1)
        # print(res)
        return res

    def partitionLabels3(self, S: str) -> List[int]:
        """
        思路：贪心算法
        1. 找到每个元素对应的最右端的下标，每个位置记录当前元素的左右
        2.
        @param S:
        @return:
        """
        n = len(S)
        index = collections.defaultdict()
        for i, c in enumerate(S):
            index[c] = i

        arr = []
        for i, c in enumerate(S):
            arr.append([i, index[c]])
        # print(arr)

        res = []
        res.append(arr[0])
        for i in range(1, n):
            l, r = arr[i]
            if l > res[-1][1]:
                res.append(arr[i])
            else:
                if r > res[-1][1]:
                    res[-1][1] = r

        # print(res)
        ans = []
        for l, r in res:
            ans.append(r - l + 1)
        return ans


    def partitionLabels4(self, S: str) -> List[int]:
        """
        思路：官方题解（贪心算法+双指针）
        小写字符总共有26个， 因此不管多长的字符串， 都是够用的。 存储的是每个字符最大位置而已。 由于是定长，因此空间消耗忽略不计。

        map底层采用红黑树实现， 时间复杂度为o(logn)。

        我想说你可能指的是底层用hash实现的hashmap吧。 如果你模拟写过hashmap你会发现， 会有一些资源开销的。 调整什么的也会做一些操作。

        可能我们平常用hashmap不会考虑到这个， 但是如果定长的数组能够解决问题， 更佳！ 哈希表 = 定长的数组 + 哈希函数映射 + 如果是开散列 + 挂的是链表 + 结点信息资源 + 超过阈值之后调优 + 扩容之后重新分配 等等都是要有开销的。
        @param S:
        @return:
        """
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition


if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels1(S))
    print(Solution().partitionLabels2(S))
    print(Solution().partitionLabels3(S))
