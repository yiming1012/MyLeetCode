"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math
from functools import lru_cache


class Solution:
    def numTrees1(self, n: int) -> int:
        """
        思路：卡特兰数
        """
        return int(math.factorial(n * 2) / math.factorial(n) ** 2 / (n + 1))

    def numTrees2(self, n: int) -> int:
        """
        动态规划
        假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数
        即有:G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
        n为根节点，当i为根节点时，其左子树节点个数为[1,2,3,...,i-1]，右子树节点个数为[i+1,i+2,...n]，
        所以当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，即f(i) = G(i-1)*G(n-i),
        上面两式可得:G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]

    @lru_cache()
    def numTrees3(self, n: int) -> int:
        """
        思路：递归+备忘录
        """
        if n <= 0: return 1
        if n <= 2: return n

        return sum([self.numTrees(i - 1) * self.numTrees(n - i) for i in range(1, n + 1)])


if __name__ == '__main__':
    n = 8
    print(Solution().numTrees1(n))
    print(Solution().numTrees2(n))
    print(Solution().numTrees3(n))
