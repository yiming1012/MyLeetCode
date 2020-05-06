
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        执行用时 :1408 ms, 在所有 Python3 提交中击败了61.80%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了51.96%的用户
        :param s:
        :return:
        '''
        maxLength = 0
        start = end = 0
        if len(s) <= 1000:
            for i in range(len(s) - 1):
                if i + 1 < len(s) and s[i] == s[i + 1]:
                    k = i
                    j = i + 1
                    while k >= 0 and j < len(s) and s[j] == s[k]:
                        if maxLength < j - k + 1:
                            maxLength = j - k + 1
                            start = k
                            end = j
                        k -= 1
                        j += 1

                if i + 2 < len(s) and s[i] == s[i + 2]:
                    k = i
                    j = i + 2
                    while k >= 0 and j < len(s) and s[j] == s[k]:
                        if maxLength < j - k + 1:
                            maxLength = j - k + 1
                            start = k
                            end = j
                        k -= 1
                        j += 1

        return s[start:end + 1]

    def longestPalindrome2(self, s: str) -> str:
        '''
        执行用时 :1440 ms, 在所有 Python3 提交中击败了61.11%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了51.96%的用户
        :param s:
        :return:
        '''
        maxLength = 0
        start = end = 0
        mid = len(s) // 2
        if len(s) <= 1000:
            # 上半段
            for i in range(mid, 0, -1):
                if i + 1 < len(s) and i - 1 >= 0 and s[i - 1] == s[i + 1]:
                    k = i - 1
                    j = i + 1
                    while k >= 0 and j < len(s) and s[j] == s[k]:
                        if maxLength <= j - k + 1:
                            maxLength = j - k + 1
                            start = k
                            end = j
                        k -= 1
                        j += 1

                if i >= 1 and s[i] == s[i - 1]:
                    k = i - 1
                    j = i
                    while k >= 0 and j < len(s) and s[j] == s[k]:
                        if maxLength <= j - k + 1:
                            maxLength = j - k + 1
                            start = k
                            end = j
                        k -= 1
                        j += 1
            # 下半段
            for i in range(mid + 1, len(s), 1):
                if i + 1 < len(s) and i - 1 >= 0 and s[i - 1] == s[i + 1]:
                    k = i - 1
                    j = i + 1
                    while k >= 0 and j < len(s) and s[j] == s[k]:
                        if maxLength < j - k + 1:
                            maxLength = j - k + 1
                            start = k
                            end = j
                        k -= 1
                        j += 1

                if i >= 1 and s[i] == s[i - 1]:
                    k = i - 1
                    j = i
                    while k >= 0 and j < len(s) and s[j] == s[k]:
                        if maxLength < j - k + 1:
                            maxLength = j - k + 1
                            start = k
                            end = j
                        k -= 1
                        j += 1

    def longestPalindrome3(self, s: str) -> str:
        '''
        执行用时 :108 ms, 在所有 Python3 提交中击败了91.82%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了51.59%的用户
        :param s:
        :return:
        '''
        maxLength = 0
        start = 0
        i = 0;
        length = len(s)
        while i < length:
            k = i
            '''
            这里很巧妙的将重复的字符当成同一个字符处理,i移动到最后面的一个相同字符
            不仅方便可以确定起始和终止位置，还可以减少遍历，直接从最后一个相同字符下一个开始遍历
            '''

            while i < length - 1 and s[i] == s[i + 1]:
                i += 1
            j = i
            while k > 0 and j < length - 1 and s[k - 1] == s[j + 1]:
                k -= 1
                j += 1
            if maxLength < j - k + 1:
                maxLength = j - k + 1
                start = k

            i += 1
        return s[start:start + maxLength]

'''
1、最先想到的是中心查找，分两种情况：abba和aba。
2、官方答案很巧妙的将重复的字符当成同一个字符处理,i移动到最后面的一个相同字符
不仅方便可以确定起始和终止位置，还可以减少遍历，直接从最后一个相同字符下一个开始遍历
'''