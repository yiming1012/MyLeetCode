"""
774. 最小化去加油站的最大距离
整数数组 stations 表示 水平数轴 上各个加油站的位置。给你一个整数 k 。

请你在数轴上增设 k 个加油站，新增加油站可以位于 水平数轴 上的任意位置，而不必放在整数位置上。

设 penalty() 是：增设 k 个新加油站后，相邻 两个加油站间的最大距离。

请你返回 penalty() 可能的最小值。与实际答案误差在 10-6 范围内的答案将被视作正确答案。
 

示例 1：

输入：stations = [1,2,3,4,5,6,7,8,9,10], k = 9
输出：0.50000
示例 2：

输入：stations = [23,24,36,39,46,56,57,65,84,98], k = 1
输出：14.00000
 

提示：

10 <= stations.length <= 2000
0 <= stations[i] <= 108
stations 按 严格递增 顺序排列
1 <= k <= 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        """
        思路：
        1. 先计算相邻两个数的差
        2. 二分计算合适的间距x，计算差v能被分成最多几个x，向下取整
        @param stations:
        @param k:
        @return:
        """
        delta = 1e-6
        arr = []
        n = len(stations)
        for i in range(1, n):
            arr.append(stations[i] - stations[i - 1])
        print(arr)

        def check(x):
            cnt = 0
            for v in arr:
                cnt += int((v - delta) // x)
            print(x, cnt)
            return cnt <= k

        l, r = 0, max(arr)
        while r - l > delta:
            mid = l + (r - l) / 2
            if check(mid):
                r = mid
            else:
                l = mid
        return r


if __name__ == '__main__':
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 9
    print(Solution().minmaxGasDist(stations, k))
