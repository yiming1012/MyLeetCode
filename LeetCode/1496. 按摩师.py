'''
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

注意：本题相对原题稍作改动

 

示例 1：

输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
示例 2：

输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
示例 3：

输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-masseuse-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        '''
        执行用时 :56 ms, 在所有 Python3 提交中击败了20.56%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：动态规划法，dp[i]=max(nums[i)+dp[i-2],dp[i-1]
        时间复杂度：O(n)
        空间复杂度：O(n)
        :param nums:
        :return:
        '''
        length = len(nums)
        if length == 0:
            return 0
        dp = [0] * length

        for i in range(length):
            if i == 0:
                dp[i] = nums[0]
            elif i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[length - 1]

    def massage2(self, nums: List[int]) -> int:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了60.83%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
        时间复杂度：O(n)
        空间复杂度：O(1)
        :param nums:
        :return:
        '''
        a, b = 0, 0
        for num in nums:
            b, a = max(num + a, b), b
        return b




if __name__ == '__main__':
    # arr = [2, 1, 4, 5, 3, 1, 1, 3]
    arr = [2, 7, 9, 3, 1, 5]
    s = Solution()
    print(s.massage2(arr))
