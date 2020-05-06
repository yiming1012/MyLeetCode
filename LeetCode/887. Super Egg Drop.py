'''
You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

 

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation:
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4
 

Note:

1 <= K <= 100
1 <= N <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-egg-drop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        f = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            f[i][1] = i
        for i in range(1, K + 1):
            f[1][i] = 1
        for i in range(2, N + 1):
            for j in range(2, K + 1):
                f[i][j] = f[i][j - 1]
                for k in range(1, i + 1):
                    f[i][j] = min(f[i][j], max(f[k - 1][j - 1], f[i - k][j]) + 1)
        return f[N][K]

    def superEggDrop2(self, K: int, N: int) -> int:
        '''
        此方法主要是求出，K个蛋，最少走i步，可以确定N层楼
        :param K:
        :param N:
        :return:
        '''
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, K + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + 1
            if dp[i][K] >= N:
                return i


if __name__ == '__main__':
    K, N = 2, 100
    s = Solution()
    print(s.superEggDrop(K, N))
