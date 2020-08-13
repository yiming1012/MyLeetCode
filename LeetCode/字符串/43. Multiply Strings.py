'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def multiply1(self, num1: str, num2: str) -> str:
        '''
        思路：如果数值很小的话，可以用这种方式
        :param num1:
        :param num2:
        :return:
        '''
        sum = 0
        carry = 1
        flag = 1
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                a = int(num1[i])
                b = int(num2[j])
                sum += a * b * carry * flag
                carry *= 10
            flag *= 10
            carry = 1
        return str(sum)

    def multiply2(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = "0"
        m, n = len(num1), len(num2)
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num2[i])
            curr = ["0"] * (n - i - 1)
            for j in range(m - 1, -1, -1):
                product = int(num1[j]) * y + add
                curr.append(str(product % 10))
                add = product // 10
            if add > 0:
                curr.append(str(add))
            curr = "".join(curr[::-1])
            ans = self.addStrings(ans, curr)
        return ans

    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = list()
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            ans.append(str(result % 10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])

    def multiply3(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        if m < n:
            num1, num2 = num2, num1
            m, n = n, m
        res = []
        for i in range(n):
            mul = int(num2[i])
            carry = 0
            cur = []
            for j in range(m - 1, -1, -1):
                carry += mul * int(num1[j])
                cur.append(carry % 10)
                carry //= 10
            if carry > 0:
                cur.append(carry)
            print(cur)
            res.append(0)
            res = self.add(res, cur[::-1])

        return "".join(res)

    def add(self,n1, n2):
        print(n1,n2)
        m, n = len(n1), len(n2)
        i, j = m - 1, n - 1
        carry = 0
        cur = []
        while i >= 0 or j >= 0:
            carry += (n1[i] if i >= 0 else 0) + (n2[j] if j >= 0 else 0)
            cur.append(carry % 10)
            carry //= 10
            i -= 1
            j -= 1
        if carry > 0:
            cur.append(carry)
        return cur[::-1]


if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    s = Solution()
    print(s.multiply1(num1, num2))
    print(s.multiply2(num1, num2))
    print(s.multiply3(num1, num2))
