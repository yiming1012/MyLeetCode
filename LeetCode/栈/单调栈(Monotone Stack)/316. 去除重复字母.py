"""
316. 去除重复字母
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 104
s 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        思路：
        1. 记录每个字母最后出现的位置
        2. 如果遍历到i位置的字符c时，c没有被访问过且c比栈顶字符更小，并且栈顶元素会在i位置之后还会出现，则将栈顶元素出栈，并从标记为访问过的集合中删除
        @param s:
        @return:
        """
        visited = set()
        index = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c not in visited:
                while stack and stack[-1] >= c and index[stack[-1]] >= i:
                    visited.remove(stack.pop())

                stack.append(c)
                visited.add(c)

        return "".join(stack)


if __name__ == '__main__':
    s = "bcabc"
    print(Solution().removeDuplicateLetters(s))
