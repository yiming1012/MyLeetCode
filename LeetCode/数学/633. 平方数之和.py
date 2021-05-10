"""
633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

 

示例 1：

输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
示例 2：

输入：c = 3
输出：false
示例 3：

输入：c = 4
输出：true
示例 4：

输入：c = 2
输出：true
示例 5：

输入：c = 1
输出：true
 

提示：

0 <= c <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-square-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def judgeSquareSum1(self, c: int) -> bool:
        """
        思路：枚举
        1. a^2+b^2=c，那么a和b肯定小于等于sqrt(c)
        2. c<2^31 - 1,时间复杂度小于10^5,所以枚举每个数即可
        @param c:
        @return:
        """
        b = int(c ** 0.5)
        if b ** 2 == c: return True
        visited = set()
        for i in range(1, int(c ** 0.5) + 1):
            visited.add(i * i)
            if c - i * i in visited:
                return True
        return False

    def judgeSquareSum2(self, c: int) -> bool:
        """
        思路：双指针
        1. l,r分别取0，int(sqrt(c))
        2. 如果l*l+r*r==c 则返回True，如果大于c，则r指针左移，否则l指针右移
        @param c:
        @return:
        """
        b = int(c ** 0.5)
        l, r = 0, b
        while l <= r:
            if l * l + r * r == c:
                return True
            elif l * l + r * r > c:
                r -= 1
            else:
                l += 1
        return False

    # 方法三：费马平方和定理


if __name__ == '__main__':
    c = 5
    print(Solution().judgeSquareSum1(c))
    print(Solution().judgeSquareSum2(c))
