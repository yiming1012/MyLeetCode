'''
Three stones are on a number line at positions a, b, and c.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints.  Formally, let's say the stones are currently at positions x, y, z with x < y < z.  You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

 

Example 1:

Input: a = 1, b = 2, c = 5
Output: [1,2]
Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
Example 2:

Input: a = 4, b = 3, c = 2
Output: [0,0]
Explanation: We cannot make any moves.
Example 3:

Input: a = 3, b = 5, c = 1
Output: [1,2]
Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.
 

Note:

1 <= a <= 100
1 <= b <= 100
1 <= c <= 100
a != b, b != c, c != a
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/moving-stones-until-consecutive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        s = a + b + c
        l = min(a, b, c)
        r = max(a, b, c)
        m = s - l - r
        # 下面这一行可以替代上面四行
        # a,b,c=sorted([a,b,c])
        print(a, b, c)
        if r - l == 2:
            return [0, 0]
        else:
            return [1 if min(r - m, m - l) <= 2 else 2, r - l - 2]



class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        '''

        思路：BFS经典模板
        :param m:
        :param n:
        :param k:
        :return:
        '''
        # 计算位数的和
        def add_coor(a, b):
            ans = 0
            while a != 0:
                ans += a % 10
                a //= 10
            while b != 0:
                ans += b % 10
                b //= 10
            return ans

        from collections import deque
        mat = [[0 for _ in range(n)] for _ in range(m)]  # 先创建 m x n 的矩阵并都设为 0
        mat[0][0] = 1  # 将初始位置设为1，代表已经访问过
        temp = deque() # 用一个队列存储即将扩展的点的坐标
        temp.append([0, 0])
        res = 0
        # BFS经典模板
        while temp:
            temp_point = temp.popleft()
            print(temp_point)
            res += 1
            x, y = temp_point
            print(x,y)
            for x_bias, y_bias in [[0, 1], [1, 0]]:
                new_x = x + x_bias
                new_y = y + y_bias
                if  new_x > m - 1 or new_y > n - 1 or add_coor(new_x, new_y) > k or mat[new_x][new_y] == 1:
                    continue
                mat[new_x][new_y] = 1
                temp.append([new_x, new_y])
        return res

    def movingCount2(self, m: int, n: int, k: int) -> int:
        '''
        思路：遍历矩阵
        :param m:
        :param n:
        :param k:
        :return:
        '''
        # 可达的格子
        num_set = set()

        for i in range(0, m):
            m_sum = i // 10 + i % 10
            # x 坐标超过 k 时，不用继续搜索
            if m_sum > k:
                break

            for j in range(0, n):
                n_sum = j // 10 + j % 10
                # y 坐标超过 k 时，不用继续搜索
                if n_sum > k:
                    break

                # 只要左边的格子或者上边的格子可达，该格子即可达
                if m_sum + n_sum <= k and (i == 0 or (i - 1, j) in num_set or (i, j - 1) in num_set):
                    num_set.add((i, j))
                    # print(i, j)

        return len(num_set)



if __name__ == '__main__':
    a, b, c = 5, 3, 7
    s = Solution()
    print(s.numMovesStones(a, b, c))
