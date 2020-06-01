"""
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        执行用时 :516 ms, 在所有 Python3 提交中击败了92.33%的用户
        内存消耗 :17.2 MB, 在所有 Python3 提交中击败了12.50%的用户
        思路：单调栈
        1. 维护一个单调递减的栈
        2. 比栈顶小，入栈
        3. 如果后面的比前面的温度高，则计算当前位置和栈顶元素下标i的距离d，赋予res[i]
        """
        res = [-1] * len(T)
        stack = []
        for i, num in enumerate(T):
            while stack and num > T[stack[-1]]:
                pre = stack.pop()
                res[pre] = i - pre
            stack.append(i)
        return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures))
