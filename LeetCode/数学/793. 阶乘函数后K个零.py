"""
793. 阶乘函数后K个零
 f(x) 是 x! 末尾是0的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且0! = 1）

例如， f(3) = 0 ，因为3! = 6的末尾没有0；而 f(11) = 2 ，因为11!= 39916800末端有2个0。给定 K，找出多少个非负整数x ，有 f(x) = K 的性质。

示例 1:
输入:K = 0
输出:5
解释: 0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。

示例 2:
输入:K = 5
输出:0
解释:没有匹配到这样的 x!，符合K = 5 的条件。
注意：

K是范围在 [0, 10^9] 的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def zero(n):
            return n // 5 + zero(n // 5) if n > 0 else 0

        l, r = K, 10 * K + 1
        while l < r:
            mid = l + (r - l) // 2
            cnt = zero(mid)

            if cnt == K:
                return 5
            elif cnt < K:
                l = mid + 1
            else:
                r = mid
        return 0
