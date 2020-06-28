class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        res = 0
        while x > 0:
            # x, y = divmod(x, 10)
            x, y = x // 10, x % 10
            # 判断是否越界最大值,不能用Long来存储
            if res > 2 ** 31 // 10 or (flag == 1 and res == 2 ** 31 // 10 and y > 7) or (
                    flag == -1 and res == 2 ** 31 // 10 and y > 8):
                return 0
            res = res * 10 + y

        return res * flag

'''
1、int类型的整数范围[minInt,maxInt]为：-2**31~2**31-1
2、反转整数时要考虑，此时的数和maxInt//10相比较，如果还有下一个数，可能会溢出
'''

s = Solution()
a = s.reverse(-123)
print(a)
