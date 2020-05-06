'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
 

Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/additive-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
## 思路：
只要固定前面两个数，后面的数都是确定的。所以我们用两个循环找前面两个数，看是否可以引出后面的数。

思路一：递归

思路二：迭代
'''


## 代码:

# 思路一：

class Solution:
    def isAdditiveNumber1(self, num: str) -> bool:

        def isValid(sub1, sub2, num):
            # print(sub1, sub2, num)
            if not num: return True
            sub1, sub2, = sub2, str(int(sub1) + int(sub2))
            return num.startswith(sub2) and isValid(sub1, sub2, num[len(sub2):])

        n = len(num)
        for i in range(1, n // 2 + 1):
            if num[0] == "0" and i > 1: return False
            sub1 = num[:i]
            for j in range(1, n):
                # 剩下的长度都没有前面两个数最大长度长
                if max(i, j) > n - i - j: break
                if num[i] == "0" and j > 1: break
                sub2 = num[i: i + j]
                # 找到两个数, 看后面的数是否能引出来
                if isValid(sub1, sub2, num[i + j:]): return True
        return False

    # 思路二：迭代
    def isAdditiveNumber2(self, num: str) -> bool:

        def isValid(sub1, sub2, num):
            while num:
                sub1, sub2, = sub2, str(int(sub1) + int(sub2))
                if not num.startswith(sub2): return False
                num = num[len(sub2):]
            return True

        n = len(num)
        for i in range(1, n // 2 + 1):
            if num[0] == "0" and i > 1: return False
            sub1 = num[:i]
            for j in range(1, n):
                # 剩下的长度都没有前面两个数最大长度长
                if max(i, j) > n - i - j: break
                if num[i] == "0" and j > 1: break
                sub2 = num[i: i + j]
                # 找到两个数, 看后面的数是否能引出来
                if isValid(sub1, sub2, num[i + j:]): return True
        return False

    def isAdditiveNumber3(self, num: str) -> bool:
        def isValid(num1, num2, s):
            if num1[0] == '0' and len(num1) > 1: return False
            if num2[0] == '0' and len(num2) > 1: return False
            tmp = str(int(num1) + int(num2))
            l = len(tmp)
            if s.startswith(tmp):
                num1, num2 = num2, tmp
                s = s[l:]
                if s == '': return True
                return isValid(num1, num2, s)
            return False

        n = len(num)
        for i in range(1, n + 1 >> 1):
            num1 = num[:i]
            for j in range(i + 1, n):
                num2 = num[i: j]
                if isValid(num1, num2, num[j:]):
                    return True
        return False

    def isAdditiveNumber4(self, num: str) -> bool:
        '''
        执行用时 :56 ms, 在所有 Python3 提交中击败了12.97%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了7.14%的用户
        :param num:
        :return:
        '''

        def isValid(num1, num2, remain):
            if num1[0] == '0' and len(num1) > 1: return False
            if num2[0] == '0' and len(num2) > 1: return False
            num3 = str(int(num1) + int(num2))
            if remain.startswith(num3):
                num1, num2 = num2, num3
                remain = remain[len(num3):]
                if remain == "":
                    return True
                return isValid(num1, num2, remain)
            return False

        n = len(num)
        for i in range(1, n + 1 // 2):
            num1 = num[:i]
            for j in range(i + 1, n):
                num2 = num[i:j]
                remain = num[j:]
                if isValid(num1, num2, remain):
                    return True
        return False


if __name__ == '__main__':
    num = "123456579"
    s = Solution()
    print(s.isAdditiveNumber4(num))
