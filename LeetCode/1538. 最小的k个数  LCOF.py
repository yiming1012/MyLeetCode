'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]


限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
'''
from typing import List

import heapq


class Solution:
    # 数组排序
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了99.81%的用户
        内存消耗 :14.5 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param arr:
        :param k:
        :return:
        '''
        if len(arr) <= k:
            return arr
        arr.sort()
        return arr[:k]

        '''
        下面这一行代码可以代替上面的代码
        return sorted(arr)[:k]
        '''

    # 堆排序
    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        '''
        执行用时 :92 ms, 在所有 Python3 提交中击败了39.10%的用户
        内存消耗 :15 MB, 在所有 Python3 提交中击败了100.00%的用户
        时间复杂度：O(nlogk)
        空间复杂度：O(k)
        :param arr:
        :param k:
        :return:
        '''
        heap = []
        for i in arr:
            heapq.heappush(heap, -i)
            if len(heap) > k:
                # 每次pop掉最小的元素
                heapq.heappop(heap)
        return [-x for x in heap]

        # 一行代码搞定
        # return heapq.nsmallest(k, arr)

    # 快速排序
    def getLeastNumbers3(self, arr: List[int], k: int) -> List[int]:
        '''
        执行用时 :76 ms, 在所有 Python3 提交中击败了56.00%的用户
        内存消耗 :16.3 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：利用快速排序找到前K个，不一定是排好序的。如果index<K,就对index+1后面的排序，反之对前面的排序
        :param arr:
        :param k:
        :return:
        '''
        low = 0
        high = len(arr) - 1

        def quickSort(low, high):
            lowIndex, highIndex = low, high
            pivot = arr[high]
            if low < high:
                while low < high:
                    while arr[low] <= pivot and low < high:
                        low += 1
                    while arr[high] >= pivot and low < high:
                        high -= 1
                    if low < high:
                        arr[low], arr[high] = arr[high], arr[low]

                print(low, high)
                arr[low], arr[highIndex] = arr[highIndex], arr[low]
                index = low
                print(arr)
                print("index:", index)
                if index == k:
                    print("find it")
                    return arr[:k]
                elif index < k:
                    print("index<k:", index)
                    quickSort(index + 1, highIndex)
                else:
                    print("index>k:", index)
                    quickSort(lowIndex, index - 1)

        quickSort(low, high)
        return arr[:k]


if __name__ == '__main__':
    arr = [8, 9, 2, 1, 3, 6, 5, 4, 7]
    k = 3
    s = Solution()
    print(s.getLeastNumbers3(arr, k))
