"""
605. 种花问题
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
注意:

数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        思路：贪心算法
        1. 判断左中右三个位置是否存在1，存在则跳过，否则就种花
        2. 当n==0时，种花完毕，返回True
        3. 否则，返回False
        @param flowerbed:
        @param n:
        @return:
        """
        if n == 0:
            return True
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 1: continue
            if i > 0 and flowerbed[i - 1] == 1: continue
            if i + 1 < m and flowerbed[i + 1] == 1: continue
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
        return False


if __name__ == '__main__':
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(Solution().canPlaceFlowers(flowerbed, n))
