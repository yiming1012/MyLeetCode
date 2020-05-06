'''
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.
'''
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        '''
        执行用时 :48 ms, 在所有 Python3 提交中击败了14.01%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了5.88%的用户
        方法：反证法，两个矩阵不重叠只有四种情况
        :param rec1:
        :param rec2:
        :return:
        '''
        if (rec1[2] <= rec2[0]) or (rec2[2] <= rec1[0]) or (rec1[1] >= rec2[3]) or (rec1[3] <= rec2[1]):
            return False
        else:
            return True

    def isRectangleOverlap2(self, rec1: List[int], rec2: List[int]) -> bool:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了51.71%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了5.88%的用户
        方法：两个矩阵重叠，必须满足：两个矩阵的左下角必须小于另外一个的右上角
        :param rec1:
        :param rec2:
        :return:
        '''
        return rec1[0] < rec2[2] and rec1[1] < rec2[3] and rec2[0] < rec1[2] and rec2[1] < rec1[3]

    def isRectangleOverlap3(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = max(rec1[0], rec2[0])
        y1 = max(rec1[1], rec2[1])
        x2 = min(rec1[2], rec2[2])
        y2 = min(rec1[3], rec2[3])
        if x1 < x2 and y1 < y2:
            return True
        else:
            return False


if __name__ == '__main__':
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    s = Solution()
    print(s.isRectangleOverlap(rec1, rec2))
