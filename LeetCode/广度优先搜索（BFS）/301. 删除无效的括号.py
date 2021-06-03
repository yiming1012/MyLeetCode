"""
301. 删除无效的括号
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。

 

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]
 

示例 1：

输入：s = "()())()"
输出：["(())()","()()()"]
示例 2：

输入：s = "(a)())()"
输出：["(a())()","(a)()()"]
示例 3：

输入：s = ")("
输出：[""]
 

提示：

1 <= s.length <= 25
s 由小写英文字母以及括号 '(' 和 ')' 组成
s 中至多含 20 个括号

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def isValid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0: return False
            return cnt == 0

        # 对每个字符串删除一个字符后比较
        queue = collections.deque()
        queue.append(s)
        visited = set()
        res = []
        while queue:
            s = queue.popleft()
            if s in visited: continue
            if isValid(s):
                if not res or len(s) == len(res[0]):
                    res.append(s)
                if res and len(s) < len(res[0]):
                    break

            visited.add(s)
            for i, c in enumerate(s):
                if c in "()":
                    tmp = s[:i] + s[i + 1:]
                    if tmp not in visited:
                        queue.append(tmp)

        return res


if __name__ == '__main__':
    s = "()())()"
    print(Solution().removeInvalidParentheses(s))
