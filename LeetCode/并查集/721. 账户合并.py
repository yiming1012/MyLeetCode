"""
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该帐户的邮箱地址。

现在，我们想合并这些帐户。如果两个帐户都有一些共同的邮件地址，则两个帐户必定属于同一个人。请注意，即使两个帐户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的帐户，但其所有帐户都具有相同的名称。

合并帐户后，按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。accounts 本身可以以任意顺序返回。

例子 1:

Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
  第一个和第三个 John 是同一个人，因为他们有共同的电子邮件 "johnsmith@mail.com"。
  第二个 John 和 Mary 是不同的人，因为他们的电子邮件地址没有被其他帐户使用。
  我们可以以任何顺序返回这些列表，例如答案[['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
  ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']]仍然会被接受。

注意：

accounts的长度将在[1，1000]的范围内。
accounts[i]的长度将在[1，10]的范围内。
accounts[i][j]的长度将在[1，30]的范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/accounts-merge
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        思路：并查集
        1. 以每个account为单位求邮箱的交集，如果存在，则为一个
        """
        n = len(accounts)
        parent = {i: i for i in range(n)}

        def union_find(x):
            if x != parent[x]:
                parent[x] = union_find(parent[x])
            return parent[x]

        for i in range(n):
            for j in range(i + 1, n):
                if set(accounts[i][1:]).intersection(accounts[j][1:]):
                    a = union_find(parent[i])
                    b = union_find(parent[j])
                    if a != b:
                        parent[a] = b

        visit = [0] * n
        res = []
        for i in range(n):
            if visit[i]:
                continue
            name = accounts[i][0]
            account = accounts[i][1:]
            for j in range(i + 1, n):
                if union_find(j) == union_find(i):
                    visit[j] = 1
                    account.extend(accounts[j][1:])
            res.append([name] + sorted(list(set(account))))
        return res

    def accountsMerge2(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        思路：并查集
        1. 以每个邮箱为单位求
        """
        H = {}
        I = list(range(len(accounts)))

        def root(i):
            if I[i] != i:
                I[i] = root(I[i])
            return I[i]

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in H:
                    I[root(I[i])] = root(H[e])
                else:
                    H[e] = root(i)

        ret = collections.defaultdict(set)
        for i in range(len(accounts)):
            ret[root(i)] |= set(accounts[i][1:])
        return [(accounts[k][0:1] + sorted(v)) for k, v in ret.items()]


if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    print(Solution().accountsMerge(accounts))
    print(Solution().accountsMerge2(accounts))
