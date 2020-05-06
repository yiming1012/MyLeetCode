import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        执行用时 :60 ms, 在所有 Python3 提交中击败了88.14%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了41.01%的用户
        :param s:
        :return:
        """
        if s == "":
            return 0
        arr = []
        maxSize = 0
        for index, char in enumerate(s):
            print(index, "+", char)
            if char not in arr:
                arr.append(char)
                # print(arr)
            else:
                while True:
                    num = arr[0]
                    arr.remove(num)
                    if num == char:
                        break
                arr.append(char)
            print("删除重复：", arr)

            length = len(arr)
            if maxSize < length:
                maxSize = length
        return maxSize

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        Runtime: 156 ms, faster than 21.77% of Python3 online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
        :param s:
        :return:
        """
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        arr = [s[0]]
        flag = 0
        maxSize = 0
        for char in s[1:]:
            if char in arr[flag:]:
                flag += arr[flag:].index(char) + 1
                arr.append(char)

            maxSize = max(maxSize, len(arr[flag:]))

        return maxSize

    def lengthOfLongestSubstring3(self, s: str) -> int:
        """
        执行用时 :76 ms, 在所有 Python3 提交中击败了55.31%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了40.98%的用户
        :param s:
        :return:
        """
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        arr = []
        flag = 0
        maxSize = 0
        for char in s:
            if char not in arr:
                arr.append(char)
            else:
                arr = arr[arr.index(char) + 1:]
                arr.append(char)
            maxSize = max(maxSize, len(arr))
        return maxSize

    def lengthOfLongestSubstring4(self, s: str) -> int:
        """
        执行用时 :104 ms 在所有 Python3 提交中击败了32.02%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了40.93%的用户
        :param s:
        :return:
        """
        dict = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in dict:
                # max相当于做了if
                i = max(dict[s[j]], i)
            ans = max(ans, j - i + 1)
            dict[s[j]] = j + 1
        return ans

    def lengthOfLongestSubstring5(self, s: str) -> int:
        """
        执行用时 :48 ms, 在所有 Python3 提交中击败了98.97%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了40.88%的用户
        :param s: 
        :return:
        """
        dict = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in dict:
                if i <= dict[s[j]]:
                    i = dict[s[j]] + 1
            # if判断比max函数效率高
            # ans = max(ans,j-i+1)
            if ans < j - i + 1:
                ans = j - i + 1
            dict[s[j]] = j
        return ans


    def lengthOfLongestSubstring6(self, s: str) -> int:
        '''
        执行用时 :60 ms, 在所有 Python3 提交中击败了94.87%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.88%的用户
        思路：
        1.利用dic保存每个值出现的下标
        2.遍历字符串，如果字符在dic中存在，则更新下标i，同时无重复字符串ans的首位为i+1
        3.最后计算ans的最大值
        :param s:
        :return:
        '''
        dic = collections.defaultdict()
        res = 0
        left = 0
        for i, c in enumerate(s):
            if c in dic and dic[c] >= left:
                left = dic[c] + 1
            dic[c] = i
            if res < i - left + 1:
                res = i - left + 1
        return res


a = Solution()
s1 = "abcabcbb"
result = a.lengthOfLongestSubstring6(s1)
print(result)
