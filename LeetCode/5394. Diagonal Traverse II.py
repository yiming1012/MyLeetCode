'''
Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.
 

Example 1:



Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:



Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
Example 3:

Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
Output: [1,4,2,5,3,8,6,9,7,10,11]
Example 4:

Input: nums = [[1,2,3,4,5,6]]
Output: [1,2,3,4,5,6]
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
There at most 10^5 elements in nums.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diagonal-traverse-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        maxLength = 0
        for num in nums:
            maxLength = max(maxLength, len(num))
        for i in range(len(nums)):
            if len(nums[i]) < maxLength:
                nums[i] += [0] * (maxLength - len(nums[i]))
        m, n = len(nums), len(nums[0])
        res = []
        i, j = 0, 0
        while 0 <= i < m and 0 <= j < n:
            i_, j_ = i, j
            while 0 <= i_ < m and 0 <= j_ < n:
                if nums[i_][j_] != 0:
                    res.append(nums[i_][j_])
                if i_ == 0 or j_ == n - 1:
                    break
                else:
                    i_ -= 1
                    j_ += 1
            if i < m - 1:
                i += 1
                j = 0
            else:
                j += 1
        return res

    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # python3.8不会自动补0
                if nums[i][j] != 0:
                    res.append([i + j, j, nums[i][j]])
        print(res)
        return [num[2] for num in sorted(res)]

    def findDiagonalOrder3(self, nums: List[List[int]]) -> List[int]:
        from collections import defaultdict
        tmp = defaultdict(list)
        # 根据主对角线坐标特性，将横纵方向坐标和相同的放在一组
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                tmp[row + col].append(nums[row][col])
        res = []
        # 按字典的 key 排序进行遍历，取出的就是按题意由左下到右上方↗一组一组的值
        for r_plus_c in sorted(list(tmp.keys())):
            # 由于存的时候是先遍历的存到前面，按题目要求需要返回来，所以取[::-1]
            res.extend(tmp[r_plus_c][::-1])
        return res



if __name__ == '__main__':
    nums = [[1, 2, 3, 4, 5],
            [6, 7],
            [8],
            [9, 10, 11],
            [12, 13, 14, 15, 16]]
    print(Solution().findDiagonalOrder(nums))
    print(Solution().findDiagonalOrder2(nums))
    print(Solution().findDiagonalOrder3(nums))
