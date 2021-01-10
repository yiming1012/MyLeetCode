"""
1231. 分享巧克力
你有一大块巧克力，它由一些甜度不完全相同的小块组成。我们用数组 sweetness 来表示每一小块的甜度。

你打算和 K 名朋友一起分享这块巧克力，所以你需要将切割 K 次才能得到 K+1 块，每一块都由一些 连续 的小块组成。

为了表现出你的慷慨，你将会吃掉 总甜度最小 的一块，并将其余几块分给你的朋友们。

请找出一个最佳的切割策略，使得你所分得的巧克力 总甜度最大，并返回这个 最大总甜度。

 

示例 1：

输入：sweetness = [1,2,3,4,5,6,7,8,9], K = 5
输出：6
解释：你可以把巧克力分成 [1,2,3], [4,5], [6], [7], [8], [9]。
示例 2：

输入：sweetness = [5,6,7,8,9,1,2,3,4], K = 8
输出：1
解释：只有一种办法可以把巧克力分成 9 块。
示例 3：

输入：sweetness = [1,2,2,1,2,2,1,2,2], K = 2
输出：5
解释：你可以把巧克力分成 [1,2,2], [1,2,2], [1,2,2]。
 

提示：

0 <= K < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-chocolate
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

"""
第二个问题，存在多种分割方式，可以分割成k+1块，当sweetsize等于某个连续数组和的时候，是可获得的最大的sweetsize。
原因是当sweetsize+1时，原有连续数组和sweetsize的块不能被独立分割，因此一定小于K+1块。
举例说明：sweetness = [1,2,3,4,5,6,7,8,9], K = 5
K=5时，分割成6块，有两种分割方式，sweetsize =5 或6都可以分割成 K+1块
sweetsize =5时，[1,2,3][4,5][6][7][8][9]，可以看到每个分组都是大于5，有剩余的。
sweetsize =6时，[1,2,3][4,5][6][7][8][9]，可以看到[1,2,3]和[6]都是等于6的，如果sweetsize++,则一定不能分成6块
sweetsize =7时，[1,2,3,4][5,6][7][8][9] 只能分成5块

1、计算总甜度。
2、从0到总甜度之间，二分查找自己能吃到的最高的甜度。针对二分查找处理的每个甜度，采用贪心算法找到自己吃到目标甜度最多可以分多少份。
如果可以分的份数大于K+1，则说明自己可以吃的更多，可以在当前甜度后面继续二分查找。如果小于K+1，则说明自己想吃的太多了，不符合要求，可以在当前甜度前面继续二分查找。


"""


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        """
        思路：二分法
        1. 巧克力总甜度sweetsize=sum(sweetness)，总人数为K+1，平均值avg为sweetsize//(K+1)
        2. 从0到avg遍历，找到满足巧克力分成K+1份条件的x最大值
        3. 单调性证明：如果当前每份巧克力的甜度为x，s为连续小块巧克力的甜度和，count为前面已划分的巧克力份数，如果s>=x，此时前面的巧克力划分为一块，s=0，count+=1,
        如果最后count>=K+1，说明此时每份巧克力的甜度偏小，即x需要增大，同理count<K+1时，说明说明此时每份巧克力的甜度偏小，即x需要增大
        @param sweetness:
        @param K:
        @return:
        """

        def check(x):
            s = 0
            count = 0
            for num in sweetness:
                s += num
                if s >= x:
                    count += 1
                    s = 0
            return count >= K + 1

        l, r = 0, sum(sweetness) // (K + 1)
        while l < r:
            mid = l + (r - l + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l


if __name__ == '__main__':
    sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    K = 5
    print(Solution().maximizeSweetness(sweetness, K))