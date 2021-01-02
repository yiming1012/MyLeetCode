"""
1268. 搜索推荐系统
给你一个产品数组 products 和一个字符串 searchWord ，products  数组中每个产品都是一个字符串。

请你设计一个推荐系统，在依次输入单词 searchWord 的每一个字母后，推荐 products 数组中前缀与 searchWord 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。

请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。

 

示例 1：

输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
输出：[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
解释：按字典序排序后的产品列表是 ["mobile","moneypot","monitor","mouse","mousepad"]
输入 m 和 mo，由于所有产品的前缀都相同，所以系统返回字典序最小的三个产品 ["mobile","moneypot","monitor"]
输入 mou， mous 和 mouse 后系统都返回 ["mouse","mousepad"]
示例 2：

输入：products = ["havana"], searchWord = "havana"
输出：[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
示例 3：

输入：products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
输出：[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
示例 4：

输入：products = ["havana"], searchWord = "tatiana"
输出：[[],[],[],[],[],[],[]]
 

提示：

1 <= products.length <= 1000
1 <= Σ products[i].length <= 2 * 10^4
products[i] 中所有的字符都是小写英文字母。
1 <= searchWord.length <= 1000
searchWord 中所有字符都是小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-suggestions-system
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect
import collections
from typing import List


class Solution:
    def suggestedProducts1(self, p: List[str], s: str) -> List[List[str]]:
        trie = {}
        dic = collections.defaultdict(list)
        for word in p:
            root = trie
            for i, c in enumerate(word):
                bisect.insort(dic[word[:i + 1]], word)
                if c not in root:
                    root[c] = {}
                root = root[c]
        res = []
        for i, c in enumerate(s):
            res.append(dic[s[:i + 1]][:3])

        return res

    def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ans = [[] for _ in range(len(searchWord))]
        for product in products:
            cnt = 0
            for i in zip(product, searchWord):
                if len(set(i)) == 1:
                    if len(ans[cnt]) < 3:
                        ans[cnt].append(product)
                    cnt += 1
                else:
                    break
        return ans


if __name__ == '__main__':
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(Solution().suggestedProducts1(products, searchWord))
