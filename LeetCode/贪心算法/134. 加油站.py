"""
134. 加油站
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明: 

如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。
示例 1:

输入:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

输出: 3

解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
示例 2:

输入:
gas  = [2,3,4]
cost = [3,4,3]

输出: -1

解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gas-station
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        思路：贪心算法
        1. 因为是环路行驶，所以将长度为n的数组首尾拼接成长度为2n-1的数组方便遍历，比如gas=[1,2,3,4,5]，拼接后为[1,2,3,4,5,1,2,3,4]
        2. 关键是，如果从i到j这段不满足条件，那么k属于[i,j]区间，都不存在k到j满足条件，需要从j+1开始重新计算
        3. 优化点：如果访问到j不满足条件，而且j超过了数组长度n，则表明不存在满足条件的加油方式，返回-1
        @param gas:
        @param cost:
        @return:
        """
        gasNum = 0
        n = len(gas)
        count = 0
        for i in range(2 * n - 1):
            if gasNum + gas[i % n] - cost[i % n] >= 0:
                gasNum += gas[i % n] - cost[i % n]
                count += 1
            else:
                if i >= n:
                    return -1
                gasNum = 0
                count = 0
            if count == n:
                return i - n + 1

        return -1


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(Solution().canCompleteCircuit(gas, cost))
