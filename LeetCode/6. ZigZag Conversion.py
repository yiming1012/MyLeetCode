class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        执行用时 :1912 ms, 在所有 Python3 提交中击败了5.02%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了35.38%的用户
        :param s:
        :param numRows:
        :return:
        '''
        if len(s) <= 2 or numRows < 2:
            return s
        print(s, len(s), numRows)
        mod = 2 * numRows - 2
        result = ""
        # 获取行列
        for i in range(numRows):
            for j in range(len(s)):
                k = j % mod
                if k == i or k == mod - i:
                    result = result + s[j]

        return result

    def convert(self, s: str, numRows: int) -> str:
        '''
        执行用时 :76 ms, 在所有 Python3 提交中击败了42.68%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了35.38%的用户
        :param s:
        :param numRows:
        :return:
        '''
        if len(s) <= 2 or numRows < 2:
            return s
        mod = 2 * numRows - 2
        dictData = {}
        mod = numRows * 2 - 2
        for i in range(len(s)):
            k = i % mod
            if k >= numRows:
                k = mod - k
            dictData[k] = (dictData.get(k) if dictData.get(k) else "") + str(s[i])
        result = "".join(dictData.values())
        return result

    def convert2(self, s: str, numRows: int) -> str:
        '''
        执行用时 :72 ms, 在所有 Python3 提交中击败了47.55%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了35.38%的用户
        :param s:
        :param numRows:
        :return:
        '''
        if len(s) <= 2 or numRows < 2:
            return s
        mod = 2 * numRows - 2
        dictData = {}
        mod = numRows * 2 - 2
        for i in range(numRows):
            dictData[i] = ""
        for i in range(len(s)):
            k = i % mod
            if k >= numRows:
                k = mod - k
            dictData[k] += str(s[i])
        result = "".join(dictData.values())
        return result

    def convert3(self, s: str, numRows: int) -> str:
        '''
        方法巧妙之处在于：向下时k增加，斜着时k减小
        :param s:
        :param numRows:
        :return:
        '''
        if len(s) <= 2 or numRows < 2:
            return s
        dictData = {}
        k = 0
        flag = 1
        for i in range(numRows):
            dictData[i] = ""
        for i in range(len(s)):
            dictData[k] += str(s[i])
            if k == numRows - 1:
                flag = -1
            elif k == 0:
                flag = 1
            k += flag

        result = "".join(dictData.values())

        return result

    def convert4(self, s: str, numRows: int) -> str:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了93.23%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了35.38%的用户
        :param s:
        :param numRows:
        :return:
        '''
        if numRows < 2:
            return s
        # 此刻的list比dict效率高
        res = ["" for _ in range(numRows)]
        print(res)
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)


'''
本题的关键在于：找规律
1、我首先找到的规律是：在竖勾这一部分，有numGroup=2*nums-2个字符，每个数的下标index =i%numGroup,
如果index大于nums-1，说明该数在√这里，将index=numGroup-index,就可以得到0~nums对应的值，添加到数组对应的部分
2、官方给出的规律：向下从0加到nums-1，向上从nums-1减到0.定义一个flag=-1，遇到0变为+1，遇到nums-1变为-1

'''
s = "PAYPALISHIRING"
s1 = "abcd"
nums = 4
a = Solution()
b = a.convert4(s, nums)
print(b)
