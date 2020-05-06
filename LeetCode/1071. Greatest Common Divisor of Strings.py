'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了44.21%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了7.48%的用户
        数学法：
        1、先计算出两个字符串最大公因子长度
        2、如果两个字符串存在最大公因子T，str1=m*T,str2=n*T.必定满足str1 + str2 == str2 + str1
        :param str1:
        :param str2:
        :return:
        '''
        candidate = math.gcd(len(str1), len(str2))
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:candidate]


    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        '''
        执行用时 :32 ms, 在所有 Python3 提交中击败了80.71%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.83%的用户
        :param str1:
        :param str2:
        :return:
        '''
        candidate = math.gcd(len(str1), len(str2))
        if (len(str1) // candidate) * str1[:candidate] == str1 and (len(str2) // candidate) * str1[
                                                                                              :candidate] == str2:
            return str1[:candidate]
        return ""












