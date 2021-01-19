"""
1138. 字母板上的路径
我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。

在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。



我们可以按下面的指令规则行动：

如果方格存在，'U' 意味着将我们的位置上移一行；
如果方格存在，'D' 意味着将我们的位置下移一行；
如果方格存在，'L' 意味着将我们的位置左移一列；
如果方格存在，'R' 意味着将我们的位置右移一列；
'!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
（注意，字母板上只存在有字母的位置。）

返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。



示例 1：

输入：target = "leet"
输出："DDR!UURRR!!DDD!"
示例 2：

输入：target = "code"
输出："RR!DDRR!UUL!R!"


提示：

1 <= target.length <= 100
target 仅含有小写英文字母
"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        """
        关键点：
        1. 当前点为“z”时，要注意先左右移动，后上下移动
        2. 其他点默认先左右移动后上下移动
        @param target:
        @return:
        """
        px, py = 0, 0
        res = []
        for c in target:
            x, y = (ord(c) - 97) // 5, (ord(c) - 97) % 5
            # 当前是z
            if c == 'z':
                dy = y - py
                if dy > 0:
                    res.extend(["R"] * dy)
                else:
                    res.extend(["L"] * -dy)
                dx = x - px
                if dx > 0:
                    res.extend(["D"] * dx)
                else:
                    res.extend(["U"] * -dx)

            else:
                dx = x - px
                if dx > 0:
                    res.extend(["D"] * dx)
                else:
                    res.extend(["U"] * -dx)
                dy = y - py
                if dy > 0:
                    res.extend(["R"] * dy)
                else:
                    res.extend(["L"] * -dy)
            res.append("!")
            px, py = x, y
        return "".join(res)


if __name__ == '__main__':
    target = "leet"
    print(Solution().alphabetBoardPath(target))
