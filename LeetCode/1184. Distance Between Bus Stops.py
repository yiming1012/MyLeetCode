'''
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.

 

Example 1:



Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.
 

Example 2:



Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.
 

Example 3:



Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
 

Constraints:

1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distance-between-bus-stops
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        '''
        执行用时 :76 ms, 在所有 Python3 提交中击败了22.02%的用户
        内存消耗 :14.5 MB, 在所有 Python3 提交中击败了10.00%的用户
        :param distance:
        :param start:
        :param destination:
        :return:
        '''
        if destination<start:
            start,destination=destination,start

        return min(sum(distance[start:destination]),sum(distance)-sum(distance[start:destination]))

    def distanceBetweenBusStops2(self, distance: List[int], start: int, destination: int) -> int:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了90%的用户
        内存消耗 :14.5 MB, 在所有 Python3 提交中击败了10.00%的用户
        优化思路：尽量将前一步运算出来的结果通过变量存起来，不要在用一次sum等函数
        :param distance:
        :param start:
        :param destination:
        :return:
        '''
        if start > destination:
            start, destination = destination, start
        forward = sum(distance[start:destination])
        backward = sum(distance) - forward
        return min(forward, backward)