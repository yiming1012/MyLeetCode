"""
440. 字典序的第K小数字
给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

注意：1 ≤ k ≤ n ≤ 109。

示例 :

输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 十叉树
        cur = 1
        k -= 1
        while k:
            step = 0
            first = cur
            last = cur + 1
            # 判断节点所在区间
            while first <= n:
                step += min(last, n + 1) - first
                first *= 10
                last *= 10
            # print(first,last,cur,step,k)
            # 不在当前分支
            if step <= k:
                k -= step
                # 进入下一个数
                cur += 1
            else:
                # 在当前分支
                k -= 1
                # 进到cur的下一个孩子，比如1进到10
                cur *= 10

        return cur


if __name__ == '__main__':
    n = 13
    k = 5
    print(Solution().findKthNumber(n, k))
