"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import cmp_to_key
from typing import List
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        1. python3使用cmp_to_key代替Python2的cmp
        2. cmp中a>b 返回1 表示将ab交换
        3. 类似于基数排序
        """
        if not nums:
            return ""

        # 返回值为1，交换
        def cmp(x, y):
            return 1 if x + y < y + x else -1

        nums = [str(_) for _ in nums]
        nums.sort(key=cmp_to_key(cmp))
        # print(nums)
        res = "".join(nums)
        return '0' if res[0] == '0' else res

    def largestNumber2(self, nums):
        """
        重载
        """
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(nums))
    print(Solution().largestNumber2(nums))
