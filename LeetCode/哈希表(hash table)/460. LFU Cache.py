'''
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

 

Follow up:
Could you do both operations in O(1) time complexity?

 

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lfu-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections


class LFUCache:

    def __init__(self, capacity: int):
        self.dic = collections.defaultdict(lambda: 0)
        self.dicCount = collections.defaultdict(lambda: 0)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dicCount[key] += 1
            self.dicCount[key] = self.dicCount.pop(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return -1
        if len(self.dic) == self.capacity:
            if key in self.dic:
                self.dicCount[key] = self.dicCount.pop(key)
            else:
                popKey = min(self.dicCount, key=self.dicCount.get)
                self.dic.pop(popKey)
                self.dicCount.pop(popKey)

        self.dicCount[key] += 1
        self.dic[key] = value


class LFUCache:

    def __init__(self, capacity: int):
        '''
        执行用时 :1332 ms, 在所有 Python3 提交中击败了7.92%的用户
        内存消耗 :23.1 MB, 在所有 Python3 提交中击败了14.29%的用户
        :param capacity:
        '''
        self.dic = collections.defaultdict(lambda: [0, 0])
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic[key][1] += 1
            self.dic[key] = self.dic.pop(key)
            return self.dic[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return -1
        if len(self.dic) == self.capacity:
            if key in self.dic:
                self.dic[key] = self.dic.pop(key)
            else:
                popKey = min(self.dic, key=lambda x: self.dic[x][1])
                self.dic.pop(popKey)

        self.dic[key][1] += 1
        self.dic[key][0] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)