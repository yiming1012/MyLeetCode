"""
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。



例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

 

示例：

输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
 

提示：

输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
超过表示范围（小时 0-11，分钟 0-59）的数据将会被舍弃，也就是说不会出现 "13:00", "0:61" 等时间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-watch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def readBinaryWatch1(self, num: int) -> List[str]:
        """
        思路：回溯法
        1. 定义长度为10的数组，将num个灯分散在数组的各个位置
        2. 前面四位为小时，后面六位为分钟
        @param num:
        @return:
        """
        d = [0] * 10

        def backtrack(index, k, arr):
            if k == 0:
                res.append(arr.copy())
                return
            for i in range(index, 10):
                arr[i] = 1
                backtrack(i + 1, k - 1, arr)
                arr[i] = 0

        res = []
        backtrack(0, num, d)
        ans = []
        # 小时/分钟
        for r in res:
            # 判断小时和分钟的数是否满足条件
            th = 0
            for i, hh in enumerate(r[:4]):
                th += hh << i

            tm = 0
            for i, hh in enumerate(r[4:]):
                tm += hh << i

            if th < 12 and tm < 60:
                tt = str(th) + ":" + (str(tm) if tm >= 10 else "0" + str(tm))
                ans.append(tt)
        return ans

    def readBinaryWatch2(self, num: int) -> List[str]:
        """
        思路：回溯法
        1. 小时由i个灯和分钟由num-i个灯表示；
        2. 小时和分钟的数字集合通过回溯法得到；
        3. 最后拼接起来即可
        @param num:
        @return:
        """

        def backtrack(index, ans, k, nn):
            if k == 0:
                res.append(ans)
                return
            for i in range(index, nn):
                ans += 1 << i
                backtrack(i + 1, ans, k - 1, nn)
                ans -= 1 << i
            return

        result = []
        for i in range(min(4, num + 1)):
            hour = i
            minu = num - i

            res = []
            backtrack(0, 0, hour, 4)
            hours = res

            res = []
            backtrack(0, 0, minu, 6)
            minutes = res

            for h in hours:
                for m in minutes:
                    if 0 <= h < 12 and 0 <= m < 60:
                        result.append(str(h) + ":" + (str(m) if m >= 10 else "0" + str(m)))
        return result

    def readBinaryWatch3(self, num: int) -> List[str]:
        """
        思路：数学
        1. 计算每个时间所需的灯的个数
        2. 统计num对应的时间即可
        @param num:
        @return:
        """

        def count(n):
            cnt = 0
            while n:
                n &= (n - 1)
                cnt += 1
            return cnt

        dic = collections.defaultdict(list)
        for h in range(12):
            for m in range(60):
                # 统计h和m所需的灯个数
                cnt = count(h) + count(m)
                dic[cnt].append(str(h) + ":" + (str(m) if m >= 10 else "0" + str(m)))
        return dic[num]


if __name__ == '__main__':
    num = 2
    print(Solution().readBinaryWatch1(num))
    print(Solution().readBinaryWatch2(num))
    print(Solution().readBinaryWatch3(num))
