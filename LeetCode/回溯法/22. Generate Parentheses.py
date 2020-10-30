'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        执行用时 :64 ms, 在所有 Python3 提交中击败了14.42%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.03%的用户
        :param n:
        :return:
        '''

        def dfs(left, right, s):
            '''
            :param left:"("的剩余次数
            :param right:")"的剩余次数
            :param s:括号匹配字符串
            :return:
            '''
            if right == 0:
                res.append(s)
                return

            if left > 0:
                dfs(left - 1, right, s + "(")
                print(left, right, s)
            if right > left:
                dfs(left, right - 1, s + ")")
                print(left, right, s)

        res = []
        left, right = n, n
        dfs(left, right, "")
        return res

    def generateParenthesis2(self, n: int) -> List[str]:

        res = []
        cur_str = ''

        def dfs(cur_str, left, right, n):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号已经使用的个数
            :param right: 右括号已经使用的个数
            :return:
            """
            if left == n and right == n:
                res.append(cur_str)
                return
            if left < right:
                return

            if left < n:
                dfs(cur_str + '(', left + 1, right, n)

            if right < n:
                dfs(cur_str + ')', left, right + 1, n)

        dfs(cur_str, 0, 0, n)
        return res


if __name__ == '__main__':
    n = 3
    left, right = n, n
    s = Solution()
    print(s.generateParenthesis(n))
