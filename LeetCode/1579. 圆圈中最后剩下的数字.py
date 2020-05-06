'''
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

 

示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2
 

限制：

1 <= n <= 10^5
1 <= m <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        '''
        超出时间限制
        :param n:
        :param m:
        :return:
        '''
        arr = [_ for _ in range(n)]
        count = 0
        while True:
            for i in range(len(arr)):
                if arr[i] != -1:
                    count = (count + 1) % m
                    if count == 0:
                        arr[i] = -1
                        if arr.count(-1) == n - 1:
                            for num in arr:
                                if num != -1:
                                    return num

    def lastRemaining2(self, n: int, m: int) -> int:
        '''
        超时
        :param n:
        :param m:
        :return:
        '''
        arr = [_ for _ in range(n)]
        i, count = -1, 0
        while True:
            i += 1
            count = (count + 1) % m
            if count == 0:
                arr.remove(arr[i])
                i -= 1
                if len(arr) == 1:
                    return arr[0]
            if i == len(arr) - 1:
                i = -1

    def lastRemaining3(self, n: int, m: int) -> int:
        '''
        依旧超时
        :param n:
        :param m:
        :return:
        '''
        arr = [_ for _ in range(n)]
        i = 0
        while n > 1:
            i = (i + m - 1) % n
            arr.remove(arr[i])
            n -= 1
        return arr[0]

    def lastRemaining4(self, n: int, m: int) -> int:
        '''
        执行用时 :2080 ms, 在所有 Python3 提交中击败了33.61%的用户
        内存消耗 :17.3 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：
        :param n:
        :param m:
        :return:
        '''
        arr = list(range(n))
        i = 0
        while len(arr) > 1:
            i = (i + m - 1) % len(arr)
            arr.pop(i)

        return arr[0]

    def lastRemaining5(self, n: int, m: int) -> int:
        '''
        思路：倒推
        每次删完一个数字，最后剩余的那个数的下标都会向前移动m的长度
        :param n:
        :param m:
        :return:
        '''
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f


if __name__ == '__main__':
    n, m = 5, 3
    s = Solution()
    print(s.lastRemaining(n, m))
