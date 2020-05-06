class Solution:
    def isValid(self, s: str) -> bool:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了62.46%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了23.89%的用户
        :param s:
        :return:
        '''
        left = ['(', '{', '[']
        total = ['()', '{}', '[]']
        res = []
        for i in s:
            if i in left:
                res.append(i)
            else:
                if len(res) > 0 and res[-1] + i in total:
                    res.pop()
                else:
                    return False
        return res == []

    def isValid2(self, s: str) -> bool:
        '''
        执行用时 :56 ms, 在所有 Python3 提交中击败了13.77%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了23.89%的用户
        :param s:
        :return:
        '''
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''


arr = "(){}"
s = Solution()
print(s.isValid2(arr))
