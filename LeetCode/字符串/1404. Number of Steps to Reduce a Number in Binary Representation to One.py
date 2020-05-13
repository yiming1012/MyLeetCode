'''
Given a number s in their binary representation. Return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It's guaranteed that you can always reach to one for all testcases.

 

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4. 
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1. 
Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1. 
Example 3:

Input: s = "1"
Output: 0
 

Constraints:

1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)
        carry = 0
        count = 0
        while len(s) > 1:
            if s[-1] == '0':
                s.pop()
            else:
                i = len(s) - 1
                s[i] = '0'
                carry = 1
                i -= 1
                while carry == 1 and i >= 0:
                    if s[i] == '0':
                        s[i] = '1'
                        carry = '0'
                    else:
                        s[i] = '0'
                        i -= 1

                if carry == 1:
                    s = ['1'] + s

            count += 1
        return count


class Solution:
    def numSteps(self, s: str) -> int:
        n, ans = len(s), 0
        # meet1 记录我们有没有遇见过字符 1
        meet1 = False
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                # 如果当前字符为 0，分为两种情况
                # (1) 还没有遇见过字符 1，那么这个 0 是字符串低位的 0，需要一次除二操作
                # (2) 遇见过字符 1，那么这个 0 会因为它右侧的某次加一操作变为 1，因此它需要一次加一和一次除二操作
                ans += (2 if meet1 else 1)
            else:
                # 如果当前字符为 1，分为两种情况
                # (1) 还没有遇见过字符 1，那么这个 1 需要一次加一和一次除二操作
                #     这里需要考虑一种特殊情况，就是这个 1 是字符串最左侧的 1，它并不需要任何操作
                # (2) 遇见过字符 1，那么这个 1 会因为它右侧的某次加一操作变为 0，因此它只需要一次除二操作
                if not meet1:
                    if i != 0:
                        ans += 2
                    meet1 = True
                else:
                    ans += 1
        return ans


if __name__ == '__main__':
    s = "1101"
    print(Solution().numSteps(s))
