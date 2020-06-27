"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    count = 0

    def reversePairs(self, nums: List[int]) -> int:
        """
        思路：利用归并排序的特点
        1. 两个排序数组，如果a数组的某个点比b数组的某个点大，那么a中该点后面的数都比b中该点大，count+=len(a)-i
        2. 注意归并排序的递归出口：if len(nums)<=1:return nums
        """

        def mergeSort(a, b):
            l1, l2 = len(a), len(b)
            if not l1: return b
            if not l2: return a
            i, j = 0, 0
            res = []
            while i < l1 and j < l2:
                if a[i] <= b[j]:
                    res.append(a[i])
                    i += 1
                else:
                    # 统计逆序对
                    self.count += l1 - i
                    res.append(b[j])
                    j += 1
            # 判断a和b是否遍历完
            if i < l1:
                res.extend(a[i:])
            else:
                res.extend(b[j:])
            return res

        def merge(arr):
            # 如果arr长度小于等于1时，返回
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            # 将有序数组一分为二
            left = merge(arr[:mid])
            right = merge(arr[mid:])
            # 排序两个有序数组
            return mergeSort(left, right)

        sortedArr = merge(nums)
        print(sortedArr)
        return self.count


if __name__ == '__main__':
    nums = [4, 3, 5, 7, 6, 2]
    print(Solution().reversePairs(nums))
