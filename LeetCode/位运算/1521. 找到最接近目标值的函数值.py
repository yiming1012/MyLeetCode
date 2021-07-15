"""
1521. 找到最接近目标值的函数值
Winston 构造了一个如上所示的函数 func 。他有一个整数数组 arr 和一个整数 target ，他想找到让 |func(arr, l, r) - target| 最小的 l 和 r 。

请你返回 |func(arr, l, r) - target| 的最小值。

请注意， func 的输入参数 l 和 r 需要满足 0 <= l, r < arr.length 。

 

示例 1：

输入：arr = [9,12,3,7,15], target = 5
输出：2
解释：所有可能的 [l,r] 数对包括 [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]]， Winston 得到的相应结果为 [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0] 。最接近 5 的值是 7 和 3，所以最小差值为 2 。
示例 2：

输入：arr = [1000000,1000000,1000000], target = 1
输出：999999
解释：Winston 输入函数的所有可能 [l,r] 数对得到的函数值都为 1000000 ，所以最小差值为 999999 。
示例 3：

输入：arr = [1,2,4,8,16], target = 0
输出：0
 

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^6
0 <= target <= 10^7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-a-value-of-a-mysterious-function-closest-to-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
      res = float('inf')
      cur = set()
      for a in arr:
        cur = {a & x for x in cur} | {a}
        # print(cur)
        res = min(res, min([abs(target-x) for x in cur]))

      return res


if __name__ == '__main__':
    arr = [9, 12, 3, 7, 15]
    target = 5
    print(Solution().closestToTarget(arr, target))