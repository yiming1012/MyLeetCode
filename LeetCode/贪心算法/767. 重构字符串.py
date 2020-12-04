"""
767. 重构字符串
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
注意:

S 只包含小写字母并且长度在[1, 500]区间内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorganize-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        pq = []
        cnt = collections.Counter(S)
        # 判断最大是否超过(n+1）//2
        if max(cnt.values()) > (n + 1) // 2:
            return ""

        for k, v in cnt.items():
            heapq.heappush(pq, (-v, k))

        res = []
        while pq:
            v1, k1 = heapq.heappop(pq)
            if not pq:
                res.append(k1)
                break
            v2, k2 = heapq.heappop(pq)
            res.append(k1)
            res.append(k2)
            v1 += 1
            v2 += 1
            if v1 < 0:
                heapq.heappush(pq, (v1, k1))
            if v2 < 0:
                heapq.heappush(pq, (v2, k2))

        return "".join(res)


    def reorganizeString2(self, S: str) -> str:
        res = ""
        counter = collections.Counter(S)
        # 边界条件
        if max(counter.values()) > (len(S) + 1) // 2:
            return res

        # 将字母添加到堆中
        pq = []
        for key, val in counter.items():
            heapq.heappush(pq, (-val, key))

        prev = (0, None)

        # 开始重构字符串
        while pq:
            v, k = heapq.heappop(pq)
            res += k
            if prev[0] < 0:
                heapq.heappush(pq, prev)
            prev = (v + 1, k)

        return res


if __name__ == '__main__':
    S = "aabbbac"
    print(Solution().reorganizeString(S))
    print(Solution().reorganizeString2(S))
