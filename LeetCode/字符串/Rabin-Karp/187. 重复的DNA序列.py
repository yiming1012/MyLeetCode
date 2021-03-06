"""
所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

 

示例：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-dna-sequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findRepeatedDnaSequences1(self, s: str) -> List[str]:
        """
        思路：hash
        @param s:
        @return:
        """
        n = len(s)
        visited, res = set(), set()
        for i in range(n - 9):
            tmp = s[i:i + 10]
            if tmp in visited:
                res.add(tmp)
            visited.add(tmp)
        return list(res)

    def findRepeatedDnaSequences2(self, s: str) -> List[str]:
        """
        思路：Rabin-Karp
        @param s:
        @return:
        """
        L, n = 10, len(s)
        if n <= L:
            return []

        # convert string to the array of 2-bits integers:
        # 00_2, 01_2, 10_2 or 11_2
        dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [dic[s[i]] for i in range(n)]

        visited, res = set(), set()
        bitmask = 0
        # compute bitmask of the first sequence in O(L) time
        for i in range(L):
            bitmask <<= 2
            bitmask |= nums[i]
        visited.add(bitmask)
        # iterate over all sequences of length L
        for i in range(1, n - L + 1):
            # compute bitmask of the sequence in O(1) time
            # left shift to free the last 2 bit
            bitmask <<= 2
            # add a new 2-bits number in the last two bits
            bitmask |= nums[i + L - 1]
            # unset first two bits: 2L-bit and (2L + 1)-bit
            bitmask &= ~(3 << 2 * L)

            if bitmask in visited:
                res.add(s[i:i + L])
            visited.add(bitmask)
        return list(res)


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences1(s))
    print(Solution().findRepeatedDnaSequences2(s))
