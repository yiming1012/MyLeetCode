"""
LCP 29. 乐团站位
某乐团的演出场地可视作 num * num 的二维矩阵 grid（左上角坐标为 [0,0])，每个位置站有一位成员。乐团共有 9 种乐器，乐器编号为 1~9，每位成员持有 1 个乐器。

为保证声乐混合效果，成员站位规则为：自 grid 左上角开始顺时针螺旋形向内循环以 1，2，...，9 循环重复排列。例如当 num = 5 时，站位如图所示



请返回位于场地坐标 [Xpos,Ypos] 的成员所持乐器编号。

示例 1：

输入：num = 3, Xpos = 0, Ypos = 2

输出：3

解释：


示例 2：

输入：num = 4, Xpos = 1, Ypos = 2

输出：5

解释：


提示：

1 <= num <= 10^9
0 <= Xpos, Ypos < num

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/SNJvJP
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        level = min(xPos, num - xPos - 1, yPos, num - yPos - 1)
        # print(level)
        # 计算外面层的数目
        total = num * num - (num - level * 2) ** 2
        # print(total)
        # 枚举每条边
        if xPos == level:
            total += (yPos - level + 1)
        elif yPos == num - level - 1:
            total += 1 + (num - level * 2 - 1) + xPos - level
        elif xPos == num - level - 1:
            total += 1 + (num - level * 2 - 1) * 2 + num - yPos - level - 1
        elif yPos == level:
            total += 1 + (num - level * 2 - 1) * 3 + num - xPos - level - 1

        # print(total)
        return (total - 1) % 9 + 1

