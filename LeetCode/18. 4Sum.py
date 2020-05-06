'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        第一遍用dfs求解超时
        :param nums:
        :param target:
        :return:
        '''
        n = len(nums)
        nums.sort()

        def dfs(arr, index):
            if len(arr) == 4 and sum(arr) == target:
                res.append(arr)
                return
            if len(arr) > 4:
                return

            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                if sum(arr) > target and nums[i] >= 0:
                    break

                dfs(arr + [nums[i]], i + 1)

        res = []
        dfs([], 0)
        return res



    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        利用hash来存储每个书对应的下标
        :param nums:
        :param target:
        :return:
        '''
        nums.sort()  # 排序放在前面，建立字典得是在排序之后建立
        length = len(nums)
        if length == 0: return []
        hashmap = dict((value, index) for index, value in enumerate(nums))  # 注意 这么创建完字典后，重复的值都将被覆盖
        # print(hashmap)
        # 设置一个集合，用于放最终结果，使用集合可以产生去重复的效果
        res = set()

        max_num = nums[-1]
        for i in range(length - 3):
            a = nums[i]
            if a + 3 * max_num < target: continue  # 当最小的数和3倍最大的数加一起还比目标值小的话，证明这个数a和其他的组合也不可能达到目标值，所以需要更大的数，则开始下一次循环
            if 4 * a > target: break  # 如果当最小的数的4倍就比目标值大，则退出循环，直接输出没有符合答案的解
            for j in range(i + 1, length - 2):
                b = nums[j]
                if a + b + 2 * max_num < target: continue
                if a + 3 * b > target: break
                for k in range(j + 1, length - 1):
                    c = nums[k]
                    d = target - (a + b + c)
                    if d > max_num: continue
                    if d < c: break
                    if d in hashmap and hashmap[d] > k:
                        res.add((a, b, c, d))
        return list(res)



    def fourSum3(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        执行用时 :100 ms, 在所有 Python3 提交中击败了86.61%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了6.52%的用户
        思路：和三数相加一样，注意去重，以及优化
        :param nums:
        :param target:
        :return:
        '''
        n = len(nums)
        arr = []
        # 如果数组长度小于4，退出
        if n < 4:
            return []
        # 对数组排序
        nums.sort()
        for i in range(n - 3):
            if nums[i] * 4 > target:
                break
            if nums[n - 1] * 4 < target:
                break
            # 去重
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # 如果最小的四个数都大于target，则跳出循环
                if nums[i] + nums[j] * 3 > target:
                    break
                # 如果最大的四个数都小于target，则跳出循环
                if nums[i] + nums[j] +nums[n - 1] * 2 < target:
                    break

                # 去重
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                low, high = j + 1, n - 1
                while low < high:
                    tmp = nums[i] + nums[j] + nums[low] + nums[high]
                    if tmp == target:
                        subArr = [nums[i], nums[j], nums[low], nums[high]]
                        arr.append(subArr)
                        # 如果相邻的两个数一样，则跳过
                        while high - 1 > low and nums[high] == nums[high - 1]:
                            high -= 1
                        while low + 1 < high and nums[low] == nums[low + 1]:
                            low += 1
                        low += 1
                        high -= 1
                    elif tmp > target:
                        high -= 1
                    else:
                        low += 1

        return arr


if __name__ == '__main__':
    arr = [-1, 0, 1, 2, -1, -4]
    target=0
    s = Solution()
    print(s.fourSum3(arr,target))

