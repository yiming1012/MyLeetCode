"""
给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。

学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试且无法作弊的最大学生人数。

学生必须坐在状况良好的座位上。

 

示例 1：



输入：seats = [["#",".","#","#",".","#"],
              [".","#","#","#","#","."],
              ["#",".","#","#",".","#"]]
输出：4
解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。
示例 2：

输入：seats = [[".","#"],
              ["#","#"],
              ["#","."],
              ["#","#"],
              [".","#"]]
输出：3
解释：让所有学生坐在可用的座位上。
示例 3：

输入：seats = [["#",".",".",".","#"],
              [".","#",".","#","."],
              [".",".","#",".","."],
              [".","#",".","#","."],
              ["#",".",".",".","#"]]
输出：10
解释：让学生坐在第 1、3 和 5 列的可用座位上。
 

提示：

seats 只包含字符 '.' 和'#'
m == seats.length
n == seats[i].length
1 <= m <= 8
1 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-students-taking-exam
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        dp = [[0] * (1 << n) for _ in range(m + 1)]
        # 每行的坏椅子位子
        broken = [0] * (m + 1)
        for i in range(1, m + 1):
            for j in range(n):
                if seats[i - 1][j] == "#":
                    broken[i] |= (1 << j)

        # 二进制位计数
        def bit_count(n):
            count = 0
            while n:
                n &= n - 1
                count += 1
            return count

        res = 0
        for i in range(1, m + 1):
            for j in range(1 << n):
                # j 为当前层合适选择（不会坐在坏椅子上 & 没有相邻的学生）
                if not j & broken[i] and not j & (j >> 1):
                    # 判断上一层的座位
                    for k in range(1 << n):
                        # 上一层的位置没有坏椅子 & 没有相邻的学生 & 当前层有学生的左上右上没有学生
                        if not k & broken[i - 1] and not k & (k >> 1) and not j & (k >> 1) and not j & (k << 1):
                            dp[i][j] = max(dp[i][j], dp[i - 1][k] + bit_count(j))
                res = max(res, dp[i][j])
        return res


if __name__ == '__main__':
    seats = [["#", ".", "#", "#", ".", "#"], [".", "#", "#", "#", "#", "."], ["#", ".", "#", "#", ".", "#"]]
    print(Solution().maxStudents(seats))
