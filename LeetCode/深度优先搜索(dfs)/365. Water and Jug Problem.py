'''
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/water-and-jug-problem
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import math


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了83.56%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了10.00%的用户
        思路：z=ax+by,其中x,y,z都是整数，如果gcd(x,y)=d,ax+by也是d的倍数，一定存在整数a,b使得ax+by=d成立
        :param x:
        :param y:
        :param z:
        :return:
        '''
        if x + y < z:
            return False
        if x == z or y == z or x + y == z:
            return True
        return z % math.gcd(x, y) == 0


'''
解题思路
可以使用BFS,DFS(递归),DFS(栈),贝祖定理解决

1.BFS
每次操作不外乎6种情况，y加满水/y排空水/x加满水/x排空水/y倒入x中(2 cases)/x倒入y中(2 cases)：
y加满水：(cur_x,y).
y排空水:(cur_x,0).
x加满水:(x,cur_y).
x排空水:(0,cur_y).
y倒入x中(2 cases):
假设倒入水的容量为V：则y中剩余：cur_y-V；x中拥有：cur_x+V;
若倒完之后y还有剩余，说明x已满：V=x-cur_x
故在这种情况下：(x,cur_y+cur_x-x)
若倒完之后y空了，说明：V=cur_y,
故在这种情况下:(cur_x+cur_y,0)

x倒入y中(2 cases):
与上面情况相似，得到：
若倒完之后x还有剩余:(cur_x+cur_y-y,y)
若倒完之后x空了:(0,cur_x+cur_y)

这6种情况看作(cur_x,cur_y)的邻居顶点，故可以使用图的BFS/DFS搜索。

代码--BFS（队列）：
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        #图的广度优先搜索#每个顶点连接6种状态
        from collections import deque
        queue=deque()
        visited=set()
        queue.append((0,0))#初始(x,y)为空
        visited.add((0,0))
        while queue:
            cur_x,cur_y=queue.popleft()
            if cur_x==z or cur_y==z or cur_x+cur_y==z:
                return True
            for (nbr_x,nbr_y) in [(cur_x,y),(cur_x,0),(x,cur_y),(0,cur_y),(x,cur_y+cur_x-x) if cur_x+cur_y>=x else (cur_x+cur_y,0),(cur_x+cur_y-y,y) if cur_x+cur_y>=y else (0,cur_x+cur_y)]:#y加满水/y排空水/x加满水/x排空水/y倒入x中(2 cases)/x倒入y中(2 cases)
                if (nbr_x,nbr_y) not in visited:
                    queue.append((nbr_x,nbr_y))
                    visited.add((nbr_x,nbr_y))
        return False
2.DFS(递归)
同样，可以采用DFS，编写辅助函数DFS(cur_x,cur_y)来递归调用自身，隐式的调用栈。但是其递归深度会很大，可以修改递归深度sys.setrecursionlimit(nums).

代码 -DFS(递归)
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        #图的深度优先搜索--递归 #每个顶点连接6种状态
        #import sys
        #sys.setrecursionlimit(10000)#设置最大递归次数
        visited=set()
        def DFS(cur_x,cur_y):
            if cur_x==z or cur_y==z or cur_x+cur_y==z:#递归基
                return True
            if (cur_x,cur_y) not in visited:#当前元素不在visited中，则添加标记
                visited.add((cur_x,cur_y))
            for (nbr_x,nbr_y) in [(cur_x,y),(cur_x,0),(x,cur_y),(0,cur_y),(x,cur_y+cur_x-x) if cur_x+cur_y>=x else (cur_x+cur_y,0),(cur_x+cur_y-y,y) if cur_x+cur_y>=y else (0,cur_x+cur_y)]:#y加满水/y排空水/x加满水/x排空水/y倒入x中(2 cases)/x倒入y中(2 cases)
                if (nbr_x,nbr_y) not in visited:#若不在visited中
                    visited.add((nbr_x,nbr_y))#添加标记
                    if DFS(nbr_x,nbr_y): return True#满足条件则返回
                    visited.remove((nbr_x,nbr_y))#删除标记
            return False#搜索完也没找到返回False
        return DFS(x,y)
3.DFS(栈)
既然自身调用函数会导致超出最大递归深度，那就直接显示用栈来编写DFS

代码 -DFS(栈)
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        #图的深度优先搜索--栈 #每个顶点连接6种状态
        stack=[]#用栈进行回溯
        visited=set()
        stack.append((0,0))#将初始值设为（0，0）
        #visited.add((0,0))
        while stack:#栈非空
            cur_x,cur_y=stack.pop()#弹出栈顶
            if cur_x+cur_y==z or cur_x==z or cur_y==z:return True#终止条件
            if (cur_x,cur_y) not in visited:#若栈顶元素未被访问
                visited.add((cur_x,cur_y))#未被访问的栈顶元素添加访问标记
                for (nbr_x,nbr_y) in [(cur_x,y),(cur_x,0),(x,cur_y),(0,cur_y),(x,cur_y+cur_x-x) if cur_x+cur_y>=x else (cur_x+cur_y,0),(cur_x+cur_y-y,y) if cur_x+cur_y>=y else (0,cur_x+cur_y)]:#y加满水/y排空水/x加满水/x排空水/y倒入x中(2 cases)/x倒入y中(2 cases)
                    stack.append((nbr_x,nbr_y))#未被访问的栈顶元素的邻居入栈
    
        return False
4.贝祖定理
贝祖定理：若a,b是整数,且gcd(a,b)=d，那么对于任意的整数x,y,ax+by都一定是d的倍数，特别地，一定存在整数x,y，使ax+by=d成立。它的一个重要推论是：a,b互质的充要条件是存在整数x,y使ax+by=1.分析题目条件，可以将目标改写为：给定x,y,找到整数a,b,使得ax+by=z, s.t. z<=x+y。ax+by=z有解iff z是x,y的最大公约数的倍数，则找到x,y的最大公约数并判断z是否是其倍数就可以了。

代码 -贝祖定理（利用math.gcd(x,y)求最大公约数）
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        #贝祖定理：若a,b是整数,且gcd(a,b)=d，那么对于任意的整数x,y,ax+by都一定是d的倍数，
        #特别地，一定存在整数x,y，使ax+by=d成立。它的一个重要推论是：a,b互质的充要条件是存在整数x,y使ax+by=1.
        #目标改写为：给定x,y,找到整数a,b,使得ax+by=z
        #ax+by=z有解iff z是x,y的最大公约数的倍数
        #找到x,y的最大公约数并判断z是否是其倍数
        #special cases:
        if x+y<z:
            return False
        if x==0 or y==0:
            return z==0 or x+y==z
        return z%math.gcd(x,y)==0

'''