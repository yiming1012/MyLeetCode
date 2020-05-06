'''
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.

 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
 

Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000

'''
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        '''
        执行用时 :64 ms, 在所有 Python3 提交中击败了18.87%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了23.58%的用户
        :param candies:
        :param num_people:
        :return:
        '''
        count = 1
        arr = [0 for i in range(num_people)]
        while candies >= count:
            arr[(count - 1) % num_people] += count
            candies -= count
            count += 1
        arr[(count - 1) % num_people] += candies
        return arr

    def distributeCandies2(self, candies: int, num_people: int) -> List[int]:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了35.09%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了23.58%的用户
        :param candies:
        :param num_people:
        :return:
        '''
        count = 1
        arr = [0 for i in range(num_people)]
        while candies > 0:
            """
            min(count, candies)可以处理最后剩余的candies
            """
            arr[(count - 1) % num_people] += min(count, candies)
            candies -= min(count, candies)
            count += 1
        return arr


    def distributeCandies3(self, candies: int, num_people: int) -> List[int]:
        '''
        执行用时 :32 ms, 在所有 Python3 提交中击败了95.96%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了23.58%的用户
        :param candies:
        :param num_people:
        :return:
        '''
        count = int((2 * candies + 0.25) ** 0.5 - 0.5)
        arr = [0] * num_people
        div, mod = divmod(count, num_people)
        '''
        利用数学规律，等差数列求解
        '''

        for i in range(num_people):
            arr[i] = int((i + 1 + i + 1 + num_people * (div - 1)) * div * 0.5)
            if i < mod:
                arr[i] += int(i + 1 + num_people * div)

        arr[mod] += int(candies - (1 + count) * count * 0.5)

        return arr


if __name__ == '__main__':
    candies = 36
    num_people = 4
    s = Solution()
    print(s.distributeCandies(candies, num_people))
