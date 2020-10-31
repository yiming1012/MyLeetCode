"""
你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。

示例 1:

输入: [4, 1, 8, 7]
输出: True
解释: (8-4) * (7-1) = 24
示例 2:

输入: [1, 2, 1, 2]
输出: False
注意:

除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/24-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        """
        使用 itertools.permutation 生成全排列
        如果 b == 0，那么，a*b, b and a/b 均为 0，但由于存储在集合中，所以只有一个 0
        *rest 接收不定数量的参数
        因为除法可能会生成浮点数，因而使用近似 24 的数来判断

        @param nums:
        @return:
        """
        @functools.lru_cache(None)
        def helper(nums):
            if len(nums)==1:
                return math.isclose(nums[0],24)
            return any(helper((x,)+tuple(rest)) for a,b,*rest in itertools.permutations(nums) for x in {a+b,a-b,a*b,b and a/b})
        return helper(tuple(nums))
