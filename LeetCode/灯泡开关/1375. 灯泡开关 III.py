"""
房间中有 n 枚灯泡，编号从 1 到 n，自左向右排成一排。最初，所有的灯都是关着的。

在 k  时刻（ k 的取值范围是 0 到 n - 1），我们打开 light[k] 这个灯。

灯的颜色要想 变成蓝色 就必须同时满足下面两个条件：

灯处于打开状态。
排在它之前（左侧）的所有灯也都处于打开状态。
请返回能够让 所有开着的 灯都 变成蓝色 的时刻 数目 。

 

示例 1：



输入：light = [2,1,3,5,4]
输出：3
解释：所有开着的灯都变蓝的时刻分别是 1，2 和 4 。
示例 2：

输入：light = [3,2,4,1,5]
输出：2
解释：所有开着的灯都变蓝的时刻分别是 3 和 4（index-0）。
示例 3：

输入：light = [4,1,2,3]
输出：1
解释：所有开着的灯都变蓝的时刻是 3（index-0）。
第 4 个灯在时刻 3 变蓝。
示例 4：

输入：light = [2,1,4,3,6,5]
输出：3
示例 5：

输入：light = [1,2,3,4,5,6]
输出：6
 

提示：

n == light.length
1 <= n <= 5 * 10^4
light 是 [1, 2, ..., n] 的一个排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bulb-switcher-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        """
        思路：
        1. 因为某一个灯泡开了之后，所有的灯泡都变成蓝色，灯泡的顺序是1-n，所以记录最大值m和数组下标i
        2. 如果i+1==m,此时所有开过的灯都变成蓝色
        """
        res = 0
        m = 0
        for i in range(len(light)):
            m = max(m, light[i])
            if i + 1 == m:
                res += 1
        return res


if __name__ == '__main__':
    light = [2, 1, 3, 5, 4]
    print(Solution().numTimesAllBlue(light))
