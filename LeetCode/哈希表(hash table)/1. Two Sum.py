from typing import List


class Solution:
    '''
    twoSum1:
    Runtime: 5976 ms, faster than 9.97% of Python3 online submissions for Two Sum.
    Memory Usage: 13.6 MB, less than 93.02% of Python3 online submissions for Two Sum.
    第一次做这题的时候利用两个for循环实现，明显效率不高
    '''

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(0, length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    '''
    twoSum2:
    Input:
    [3,2,4]
    6
    Output:
    [0,0]
    Expected:
    [1,2]
    '''

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            print(i, num)
            dict[num] = i
        for i, num in enumerate(nums):
            another_num = target - num
            if another_num in dict:
                index = dict[another_num]
                return [i, index]
        return None

    '''
    twoSum3:
    Runtime: 52 ms, faster than 56.40% of Python3 online submissions for Two Sum.
    Memory Usage: 14.2 MB, less than 60.93% of Python3 online submissions for Two Sum.
    '''

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        '''
        高效的思路：利用hash表存储已经遍历过的数，并将对应的数值和下标存起来。一边遍历一遍在hash表中查找
        :param nums:
        :param target:
        :return:
        '''
        dict = {}
        for i, num in enumerate(nums):
            another_num = target - num
            if another_num in dict:
                index = dict[another_num]
                return [index, i]
            dict[num] = i
        return None

    '''
    towSum4:
    Runtime: 48 ms, faster than 79.14% of Python3 online submissions for Two Sum.
    Memory Usage: 14.2 MB, less than 54.42% of Python3 online submissions for Two Sum.
    '''

    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        '''
        不断优化
        :param nums:
        :param target:
        :return:
        '''
        dict = {}
        for i in range(len(nums)):
            # 代码中尽量不要产生中间变量
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i
        return False

    '''
    TwoSum5:
    Runtime: 40 ms, faster than 97.94% of Python3 online submissions for Two Sum.
    Memory Usage: 14.3 MB, less than 51.16% of Python3 online submissions for Two Sum.
    '''
    def twoSum5(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i
        return False

'''
心得：
1、尽量不要申请变量，会占内存
2、考虑时间复杂度，一般不会为O(n*n)
3、考虑特殊情况，如空列表、不存在
'''
if __name__ == '__main__':
    nums = [2, 8, 11, 15, 7]
    target = 9
    a = Solution()
    result = a.twoSum5(nums, target)
    print(result)
