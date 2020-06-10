"""
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

 

示例 1：

输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
示例 2：

输入：["b==a","a==b"]
输出：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
示例 3：

输入：["a==b","b==c","a==c"]
输出：true
示例 4：

输入：["a==b","b!=c","c==a"]
输出：false
示例 5：

输入：["c==c","b==d","x!=z"]
输出：true
 

提示：

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] 和 equations[i][3] 是小写字母
equations[i][1] 要么是 '='，要么是 '!'
equations[i][2] 是 '='

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/satisfiability-of-equality-equations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        并查集的思想：用集合中的一个元素代表集合。通常用树或链表
        1.最开始，各自为战，每个元素的父节点都是自己
        2.当a赢了b，则b的父节点是a
        """

        def union_find(x):
            if x == dic[x]:
                return x
            return union_find(dic[x])

        dic = collections.defaultdict(lambda: 0)
        for i in range(26):
            dic[i] = i

        for e in equations:
            if e[1] == '=':
                left = union_find(ord(e[0]) - ord('a'))
                right = union_find(ord(e[3]) - ord('a'))
                if left != right:
                    dic[right] = left

        for e in equations:
            if e[1] == '!':
                left = union_find(ord(e[0]) - ord('a'))
                right = union_find(ord(e[3]) - ord('a'))
                if left == right:
                    return False
        return True

    def equationsPossible2(self, equations: List[str]) -> bool:
        """
        思路：并查集
        """

        def find(x):
            if x == p[x]:
                return p[x]
            else:
                p[x] = find(p[x])
                return p[x]

        # ----------------union find------------------
        p = [i for i in range(26)]
        # '=='
        for eq in equations:
            if eq[1] == '=':
                r1 = find(ord(eq[0]) - ord('a'))
                r2 = find(ord(eq[3]) - ord('a'))
                if r1 != r2:
                    p[r2] = r1

        # '!='
        for eq in equations:
            if eq[1] == '!':
                r1 = find(ord(eq[0]) - ord('a'))
                r2 = find(ord(eq[3]) - ord('a'))
                if r1 == r2:
                    return False
        return True

    def equationsPossible3(self, equations):
        n = noset = set()
        d = {a: a for a in "abcdefghijklmnopqrstuvwxyz"}

        def root(x):
            if x != d[x]:
                d[x] = root(d[x])
            return d[x]

        for a, b, w, c in equations:
            if b == "!":
                noset.add((a, c))
            else:
                d[root(a)] = root(c)  # union
        for i, j in n:
            if root(i) == root(j):
                return False
        return True


if __name__ == '__main__':
    equations = ["a==b", "b!=c", "c==a"]
    print(Solution().equationsPossible(equations))
    print(Solution().equationsPossible2(equations))
