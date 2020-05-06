'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5

'''
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        '''
        执行用时 :432 ms, 在所有 Python3 提交中击败了27.47%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param target:
        :return:
        '''
        # way1
        half = (target + 1) // 2
        arr = []

        for i in range(1, half):
            sum = 0
            # subarr=[]
            for j in range(i, half + 1):
                sum += j
                if sum > target:
                    break
                elif sum == target:
                    subarr = [k for k in range(i, j + 1)]
                    arr.append(subarr)
                    break

        return arr

    def findContinuousSequence2(self, target: int) -> List[List[int]]:
        '''
        执行用时 :164 ms, 在所有 Python3 提交中击败了69.12%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param target:
        :return:
        '''
        # way1
        half = (target + 1) // 2
        arr = []

        for i in range(1, half):
            t = (2 * i - 1) / 2
            n = (2 * target + t ** 2) ** 0.5 - t
            if n == int(n):
                arr.append([k for k in range(i, i + int(n))])

        return arr

    def findContinuousSequence3(self, target: int) -> List[List[int]]:
        '''
        执行用时 :172 ms, 在所有 Python3 提交中击败了66.97%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param target:
        :return:
        '''
        # way1
        half = (target + 1) // 2
        arr = []
        i = 1
        while i < half:
            t = (2 * i - 1) / 2
            n = (2 * target + t ** 2) ** 0.5 - t

            if n == int(n):
                arr.append([k for k in range(i, i + int(n))])
                i += 1
            i += 1

        return arr

    def findContinuousSequence4(self, target: int) -> List[List[int]]:
        '''
        间隔法
        执行用时 :56 ms, 在所有 Python3 提交中击败了92.82%的用户
        内存消耗 :13.2 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param target:
        :return:
        '''
        # 我们的间隔从1开始
        i, res = 1, []

        # (x+y)*(y-x+1)/2=target
        # x = (target-i*(i+1)/2)/(i+1)

        # 根据上面的条件1，限定i的大小，即间隔的范围
        while i * (i + 1) / 2 < target:
            # 根据条件2，如果x不为整数则扩大间隔
            if not (target - i * (i + 1) / 2) % (i + 1):
                # 如果两个条件都满足，代入公式求出x即可，地板除//会把数改成float形式，用int()改回来
                x = int((target - i * (i + 1) / 2) // (i + 1))
                # 反推出y，将列表填入输出列表即可
                res.append(list(range(x, x + i + 1)))
            # 当前间隔判断完毕，检查下一个间隔
            i += 1

        # 由于间隔是从小到大，意味着[x,y]列表是从大到小的顺序放入输出列表res的，所以反转之
        return res[::-1]

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了96.41%的用户
        内存消耗 :13.3 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param target:
        :return:
        '''
        # 我们的间隔从2开始
        i, res = 2, []

        # (x+y)*(y-x+1)/2=target
        # x = (target-i*(i+1)/2)/(i+1)

        # 根据上面的条件1，限定i的大小，即间隔的范围
        while target > i * (i - 1) / 2:
            # 根据条件2，如果x不为整数则扩大间隔
            if not (target - i * (i - 1) / 2) % i:
                # 如果两个条件都满足，代入公式求出x即可，地板除//会把数改成float形式，用int()改回来
                x = int((target - i * (i - 1) / 2) // i)
                # 反推出y，将列表填入输出列表即可
                res.append(list(range(x, x + i)))
            # 当前间隔判断完毕，检查下一个间隔
            i += 1

        # 由于间隔是从小到大，意味着[x,y]列表是从大到小的顺序放入输出列表res的，所以反转之
        return res[::-1]
