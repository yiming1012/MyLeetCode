from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    target = 5
    s = Solution()
    print(s.search(nums, target))
