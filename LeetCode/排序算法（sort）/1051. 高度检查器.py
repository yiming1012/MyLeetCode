"""
1051. 高度检查器
学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。

请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。

注意，当一组学生被选中时，他们之间可以以任何可能的方式重新排序，而未被选中的学生应该保持不动。

 

示例：

输入：heights = [1,1,4,2,1,3]
输出：3
解释：
当前数组：[1,1,4,2,1,3]
目标数组：[1,1,1,2,3,4]
在下标 2 处（从 0 开始计数）出现 4 vs 1 ，所以我们必须移动这名学生。
在下标 4 处（从 0 开始计数）出现 1 vs 3 ，所以我们必须移动这名学生。
在下标 5 处（从 0 开始计数）出现 3 vs 4 ，所以我们必须移动这名学生。
示例 2：

输入：heights = [5,1,2,3,4]
输出：5
示例 3：

输入：heights = [1,2,3,4,5]
输出：0
 

提示：

1 <= heights.length <= 100
1 <= heights[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/height-checker
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def heightChecker1(self, heights: List[int]) -> int:
        """
        思路：计数排序
        @param heights:
        @return:
        """
        if not heights:
            return 0
        n = len(heights)
        cnt = [0] * 101
        for h in heights:
            cnt[h] += 1
        line = []
        for i in range(1, 101):
            line.extend([i] * cnt[i])
        res = 0
        for i in range(n):
            if heights[i] != line[i]:
                res += 1
        return res

    def heightChecker2(self, heights: List[int]) -> int:
        """
        思路：不用新建line数组
        @param heights:
        @return:
        """
        if not heights:
            return 0
        cnt = [0] * 101
        for h in heights:
            cnt[h] += 1
        res = 0
        j = 0
        for i in range(1, 101):
            while cnt[i]:
                if heights[j] != i:
                    res += 1
                j += 1
                cnt[i] -= 1

        return res


if __name__ == '__main__':
    heights = [1, 1, 4, 2, 1, 3]
    print(Solution().heightChecker(heights))
