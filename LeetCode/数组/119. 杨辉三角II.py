"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。


在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        res.append(0)
        for i in range(1, rowIndex + 1):
            res.insert(0, 0)
            for j in range(len(res) - 1):
                res[j] += res[j + 1]
        res.pop()
        return res


# 方法 1：生成一半，另一半对称生成的一半
class Solution1:
    def getRow(self, rowIndex):
        cur = []
        for i in range(rowIndex + 1):
            # 每行首个元素为 1
            temp = [1]
            # 由上一行生成当前行前一半的元素
            for j in range(i // 2):
                temp += [pre[j] + pre[j + 1]]
            # 对称生成另一半后合并，并组成新杨辉三角
            cur = temp + temp[::-1][(i + 1) % 2:]
            pre = cur
        return cur


# 方法 2：直接循环计算生成
class Solution2:
    def getRow(self, rowIndex):
        cur = [1]
        for i in range(1, rowIndex + 1):
            # 每行首个元素为 1
            temp = [1]
            # 由上一行循环生成当前行元素（除两端）
            for j in range(1, i):
                temp += [pre[j - 1] + pre[j]]
            # 添加最后一个元素 1，并组成新杨辉三角
            cur = temp + [1]
            pre = cur
        return cur


# 方法 3：先直接生成所需空间（用 1 填充），再循环计算更新生成
class Solution3:
    def getRow(self, rowIndex):
        for i in range(rowIndex + 1):
            # 用 1 先填充每行所有元素
            cur = [1] * (i + 1)
            # 由上一行循环生成当前行元素（除两端）
            for j in range(1, i):
                cur[j] = pre[j - 1] + pre[j]
            pre = cur
        return cur


# 方法 4：使用公式
# 组合公式C(n,i) = n!/(i!*(n-i)!)
# 则第(i+1)项是第i项的倍数=(n-i)/(i+1)
class Solution4:
    def getRow(self, rowIndex):
        temp = 1
        res = []
        for i in range(rowIndex + 1):
            res.append(temp)
            temp = temp * (rowIndex - i) // (i + 1)
        return res


# 方法 5：使用公式生成一半
class Solution5:
    def getRow(self, rowIndex):
        temp = 1
        res = []
        # 生成前半部分
        for i in range((rowIndex) // 2 + 1):
            res.append(temp)
            temp = temp * (rowIndex - i) // (i + 1)
        # 前半部分与其镜像对称的后半部分合并
        return res + res[::-1][(rowIndex + 1) % 2:]


# 方法 6：当前行等于上一行前后添零累加：[1,4,6,4,1] = [0,1,3,3,1] + [1,3,3,1,0]
class Solution6:
    def getRow(self, rowIndex):
        res = [1]
        for i in range(rowIndex + 1):
            # temp1, temp2 = [0] + res, res + [0]
            # res = [temp1[j] + temp2[j] for j in range(i + 1)]
            res = [([0] + res)[j] + (res + [0])[j] for j in range(i + 1)]
        return res


if __name__ == '__main__':
    numRows = 5
    print(Solution().getRow(numRows))
    print(Solution1().getRow(numRows))
    print(Solution2().getRow(numRows))
    print(Solution3().getRow(numRows))
    print(Solution4().getRow(numRows))
    print(Solution5().getRow(numRows))
    print(Solution6().getRow(numRows))
