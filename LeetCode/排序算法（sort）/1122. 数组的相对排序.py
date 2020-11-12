"""
1122. 数组的相对排序
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

 

示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
 

提示：

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        题解：https://leetcode-cn.com/problems/relative-sort-array/solution/python3-ji-shu-pai-xu-by-yim-6/
        @param arr1:
        @param arr2:
        @return:
        """
        cnt = [0] * 1001
        res = []
        # 统计arr1中每个数的频次
        for num in arr1:
            cnt[num] += 1

        # 按照arr2的顺序以及出现频次将每个数放入res中
        for num in arr2:
            res.extend([num] * cnt[num])
            cnt[num] = 0

        # 将桶中剩余元素按顺序和频次放入res数组后面
        for i in range(1001):
            if cnt[i] > 0:
                res.extend([i] * cnt[i])
        return res


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(Solution().relativeSortArray(arr1, arr2))
