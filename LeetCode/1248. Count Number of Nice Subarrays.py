'''
Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        '''
        执行用时 :1388 ms, 在所有 Python3 提交中击败了15.48%的用户
        内存消耗 :20.4 MB, 在所有 Python3 提交中击败了25.00%的用户
        :param nums:
        :param k:
        :return:
        '''
        n = len(nums)
        countOdd = 0
        stack = []
        for i in range(n):
            if nums[i] % 2 == 1:
                stack.append(i)

        if len(stack) < k:
            return 0

        for i in range(len(stack)):
            if i + 1 >= k:
                leftIndex = i - k + 1
                if leftIndex > 0:
                    leftLength = stack[leftIndex] - stack[leftIndex - 1]
                else:
                    leftLength = stack[leftIndex] + 1

                if i < len(stack) - 1:
                    rightLength = stack[i + 1] - stack[i]
                else:
                    rightLength = len(nums) - stack[i]

                countOdd += leftLength * rightLength

        print(stack)
        return countOdd

    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        '''
        官方题解
        方法一：数学
        思路和算法

        这个题目中偶数其实是没有用的，我们可以单独建立一个 \textit{odd}odd 数组来记录第 ii 个奇数的下标。那么我们可以枚举奇数，假设当前枚举到第 ii 个，那么 [\textit{odd}[i],\textit{odd}[i+k-1]][odd[i],odd[i+k−1]] 这个子数组就恰好包含 kk 个奇数。由于奇数和奇数间存在偶数，所以一定存在其他子数组 [l,r][l,r] 满足 [l,r][l,r] 包含 [\textit{odd}[i],\textit{odd}[i+k-1]][odd[i],odd[i+k−1]] 且 [l,r][l,r] 里的奇数个数为 kk 个，那么这个需要怎么统计呢？

        由于我们已经记录了每个奇数的下标，所以我们知道对于第 ii 个奇数，它的前一个奇数的下标为 \textit{odd}[i-1]odd[i−1]，也就是说 (\textit{odd}[i-1],\textit{odd}[i])(odd[i−1],odd[i]) 间的数都为偶数。同理可得 (\textit{odd}[i+k-1],\textit{odd}[i+k])(odd[i+k−1],odd[i+k]) 间的数也都为偶数。那么我们可以得出满足 l\in (\textit{odd}[i-1],\textit{odd}[i]]l∈(odd[i−1],odd[i]] 且 r\in [\textit{odd}[i+k-1],\textit{odd}[i+k])r∈[odd[i+k−1],odd[i+k]) 条件的子数组 [l,r][l,r] 包含 [\textit{odd}[i],\textit{odd}[i+k-1]][odd[i],odd[i+k−1]] 且 [l,r][l,r] 里的奇数个数为 kk 个。因此对于第 ii 个奇数，它对答案的贡献为符合条件的 [l,r][l,r] 的个数，即：

        (\textit{odd}[i] - \textit{odd}[i - 1]) * (\textit{odd}[i + k] - \textit{odd}[i + k - 1])
        (odd[i]−odd[i−1])∗(odd[i+k]−odd[i+k−1])

        我们只要遍历一遍 \textit{odd}odd 数组即可求得最后的答案，注意边界的处理。

        C++Python3
        class Solution:
            def numberOfSubarrays(self, nums: List[int], k: int) -> int:
                n = len(nums)
                odd = [-1]
                ans = 0
                for i in range(n):
                    if nums[i] % 2 == 1:
                        odd.append(i)
                odd.append(n)
                print(odd)
                for i in range(1, len(odd) - k):
                    ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
                return ans
        复杂度分析

        时间复杂度：O(n)O(n)，其中 nn 为数组的大小。遍历 \textit{odd}odd 数组最坏情况下需要 O(n)O(n) 的时间。

        空间复杂度：O(n)O(n)，其中 nn 为数组的大小。\textit{odd}odd 数组需要 O(n)O(n) 的空间。


        边界处理太妙了，分别把-1和n加到stack首尾
        :param nums:
        :param k:
        :return:
        '''
        n = len(nums)
        odd = [-1]
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        print(odd)
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        '''
        前缀和+hash
        :param nums:
        :param k:
        :return:
        '''
        dic = collections.defaultdict(lambda: 0)
        cumsum, res = 0, 0
        dic[0] = 1
        for i in range(len(nums)):
            cumsum += nums[i] & 1
            if cumsum - k in dic:
                res += dic[cumsum - k]
            dic[cumsum] += 1
        return res


if __name__ == '__main__':
    nums = [1, 1, 2, 1, 1]
    s = Solution()
    print(s.numberOfSubarrays(nums))
