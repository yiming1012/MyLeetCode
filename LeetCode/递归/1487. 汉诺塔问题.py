'''
In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:

(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.

Write a program to move the disks from the first tower to the last using stacks.

Example1:

 Input: A = [2, 1, 0], B = [], C = []
 Output: C = [2, 1, 0]
Example2:

 Input: A = [1, 0], B = [], C = []
 Output: C = [1, 0]
Note:

A.length <= 14

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hanota-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        1. n = 1 时，直接把盘子从 A 移到 C；
        2. n > 1 时，
            (1) 先把上面 n - 1 个盘子从 A 移到 B（子问题，递归）；
            (2) 再将最大的盘子从 A 移到 C；
            (3) 再将 B 上 n - 1 个盘子从 B 移到 C（子问题，递归）。
        """

        def move(n, A, B, C):
            if n == 0:
                return
            move(n - 1, A, C, B)
            C.append(A.pop())
            print(A, B, C)
            move(n - 1, B, A, C)

        n = len(A)
        move(n, A, B, C)
        return C


if __name__ == '__main__':
    A, B, C = [2, 1, 0], [], []
    print(Solution().hanota(A, B, C))
