class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        执行用时 :96 ms, 在所有 Python3 提交中击败了23.64%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了30.54%的用户
        :param x:
        :return:
        '''
        if x<0:
            return False
        else:
            res =0
            flag = x
            while x!=0:
                x,y = x//10,x%10
                res = res*10+y
                # print(res)
            print(res,x)
            if res == flag:
                return True
            else:
                return False

    def isPalindrome(self, x: int) -> bool:
        '''
        执行用时 :84 ms, 在所有 Python3 提交中击败了37.08%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了28.96%的用户
        :param x:
        :return:
        '''
        #为负数和末尾为0的不是回文
        if x<0 or (x % 10 == 0 and x!=0):
            return False
        reverse = 0
        while x>reverse:
            reverse = reverse*10 + x%10
            x//=10
        return x==reverse or x==reverse//10

    def isPalindrome(self, x: int) -> bool:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了96.89%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了28.96%的用户
        :param x:
        :return:
        '''
        # 直接变为字符串反转
        reverse = str(x)[::-1]
        return str(x) == reverse


'''
1、回文的特点：正反都一样，只需要比较前后一半即可
2、反转 利用字符串比较方便str(x)[::-1]
3、整数的反转一定要考虑到 溢出
'''
s= Solution()
print(s.isPalindrome2(12121))