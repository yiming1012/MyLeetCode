"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random
from heapq import nlargest
from typing import List


class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        """
        思路：快速选择算法
        1. 快排的思想是确定index，使得index左边的数小于等于nums[index]，右边的数大于nums[index]
        2. 只需确定一边即可
        3. 其中防止数组有序，时间复杂度退化到O(N**2）
        """

        def quickSort(left, right):
            if left < right:
                x, y = left, right
                # 随机替换掉第一个数，防止数组有序，时间复杂度退化到O(N**2）
                index = random.randint(x, y)
                nums[left], nums[index] = nums[index], nums[left]
                pivot = nums[left]
                while left < right:
                    while left < right and nums[right] < pivot:
                        right -= 1
                    while left < right and nums[left] >= pivot:
                        left += 1
                    nums[left], nums[right] = nums[right], nums[left]

                nums[left], nums[x] = nums[x], nums[left]
                if k - 1 < left:
                    quickSort(x, left - 1)
                elif k - 1 > left:
                    quickSort(left + 1, y)
                else:
                    return

        quickSort(0, len(nums) - 1)
        # print(nums)
        return nums[k - 1]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """堆排序思想"""

        def heapify(a, start, end):
            """ 自上向下堆化
            Args:
                a (list): 输入数组
                start (int): 堆化目标在数组的位置
                end (int): 堆在数组的截止位置
            """
            while True:
                max_pos = start  # 初始化最大值所在位置为目标所在
                if start * 2 + 1 <= end and a[start] < a[start * 2 + 1]:
                    # 如果左叶子节点存在，且大于目标值，则将最大值所在位置指向该节点所在位置
                    max_pos = start * 2 + 1
                if start * 2 + 2 <= end and a[max_pos] < a[start * 2 + 2]:
                    # 如果右叶子节点存在，且大于目标值，则将最大值所在位置指向该节点所在位置
                    max_pos = start * 2 + 2
                if max_pos == start:
                    # 如果目标即为最大，完成该节点堆化，跳出循环
                    break
                # 交换位置，将最大值
                a[start], a[max_pos] = a[max_pos], a[start]
                start = max_pos

        # 建堆,只需要对前半节点堆化
        for i in range(len(nums) // 2 - 1, -1, -1):
            heapify(nums, i, len(nums) - 1)
        # 排序，只需要循环K次，排序TOP K个节点
        i = len(nums) - 1
        while i > len(nums) - 1 - k:
            nums[0], nums[i] = nums[i], nums[0]
            i -= 1
            heapify(nums, 0, i)
        return nums[len(nums) - k]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heapreplace
        # 使用堆的nlargest(n,iter)返回前n个最大的数,倒序排练
        return nlargest(k, nums)[-1]

    def findKthLargest4(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heapreplace
        # 使用小顶堆
        heap = []
        for i in range(len(nums)):
            if i < k:
                heappush(heap, nums[i])
            else:
                if nums[i] > heap[0]:
                    m = heapreplace(heap, nums[i])
        return heap[0]


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(Solution().findKthLargest1(nums, k))
    print(Solution().findKthLargest2(nums, k))
    print(Solution().findKthLargest3(nums, k))
    print(Solution().findKthLargest4(nums, k))
