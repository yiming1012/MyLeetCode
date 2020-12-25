'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 1：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    res = 0

    def movingCount(self, m: int, n: int, k: int) -> int:
        '''
        执行用时 :128 ms, 在所有 Python3 提交中击败了15.05%的用户
        内存消耗 :17.2 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：DFS深度优先搜索
        :param m:
        :param n:
        :param k:
        :return:
        '''
        loc = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visit = [[0] * n for _ in range(m)]

        # print(visit)

        def dfs(a, b):
            count_a = sum(int(_) for _ in str(a))
            count_b = sum(int(_) for _ in str(b))
            # print(count_a,count_b)
            if count_a + count_b > k:
                return

            else:
                # print(a,b)
                self.res += 1
                # print("res:",self.res)
                visit[a][b] = 1
                for l in loc:
                    i, j = l[0], l[1]
                    # print(i,j)
                    # print("ab:",a,b)
                    if 0 <= a + i < m and 0 <= b + j < n and visit[a + i][b + j]:
                        dfs(a + i, b + j)

        dfs(0, 0)
        return self.res


class Solution2:
    res = 0

    def movingCount(self, m: int, n: int, k: int) -> int:
        '''
        执行用时 :60 ms, 在所有 Python3 提交中击败了72%的用户
        内存消耗 :17.2 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param m:
        :param n:
        :param k:
        :return:
        '''
        loc = [[1, 0], [0, 1]]
        visit = [[0] * n for _ in range(m)]

        # print(visit)

        def dfs(a, b):
            count_ab = sum(int(_) for _ in str(a) + str(b))
            if count_ab > k:
                return
            else:
                self.res += 1
                visit[a][b] = 1
                for l in loc:
                    i, j = l[0], l[1]
                    if 0 <= a + i < m and 0 <= b + j < n and visit[a + i][b + j] == 0:
                        dfs(a + i, b + j)

        dfs(0, 0)
        return self.res


class Solution3:
    def digitsum(self, n):
        ans = 0
        while n:
            ans += n % 10
            n //= 10
        return ans

    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and self.digitsum(i) + self.digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)
