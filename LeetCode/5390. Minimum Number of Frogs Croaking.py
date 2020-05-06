'''
Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.

 

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
Example 4:

Input: croakOfFrogs = "croakcroa"
Output: -1
 

Constraints:

1 <= croakOfFrogs.length <= 10^5
All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-frogs-croaking
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        t = ['c', 'r', 'o', 'a', 'k']
        d = {}
        dd = {}
        for index, i in enumerate('croak'):
            d[i] = 0
            if index > 0:
                dd[i] = t[index - 1]  # dd中的键值对为 {某字符：某字符的前一个字符}，例如'c':'r','o':'r'...
        ans = 0
        l_c = 0  # 来统计'c'和'k'的数量是否匹配，如果不相等说明字符串不合法
        for i in croakOfFrogs:
            d[i] += 1
            if i == 'c':
                l_c += 1
                ans = max(d['c'] - d['k'], ans)  # d['c']-d['k']代表了在遍历的每个时刻，需要有多少个蛙同时呱才满足要求
            else:
                if d[i] > d[dd[i]]:  # 要求该字符出现的次数应该小于等于其前面一个字符出现的次数，如果大于说明字符串不合法
                    return -1
                if i == 'k':  # 说明有一个蛙呱完了，d['c']-1说明，在下个时刻，不需要这个蛙再呱了
                    l_c -= 1
        if l_c:  # 来统计'c'和'k'的数量是否匹配，如果不相等说明字符串不合法
            return -1
        return ans


if __name__ == '__main__':
    croakOfFrogs = "crocroakak"
    s = Solution()
    print(s.minNumberOfFrogs(croakOfFrogs))
