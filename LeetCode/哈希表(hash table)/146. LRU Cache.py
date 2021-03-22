'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import OrderedDict


class LRUCacheDict:

    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.lrucache = OrderedDict()

    def get(self, key: int) -> int:
        # 说明在缓存中,重新移动字典的尾部
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        return self.lrucache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        # 如果存在,删掉,重新赋值
        if key in self.lrucache:
            del self.lrucache[key]

        if len(self.lrucache) == self.maxsize:
            # 弹出字典的头部(因为存储空间不够了)
            self.lrucache.popitem(last=False)

        # 在字典尾部添加
        self.lrucache[key] = value


# Your LRUCache object will be instantiated and called as such:


class DListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.size = 0
        self.head = DListNode()
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            node = self.dic[key]
            self.moveToHead(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            node = DListNode(key, value)
            self.dic[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                node = self.removeTail()
                self.size -= 1
                del self.dic[node.key]
        else:
            node = self.dic[key]
            node.value = value
            self.moveToHead(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def addToHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def removeTail(self):
        node = self.tail.prev
        node.prev.next = self.tail
        node.next.prev = node.prev
        return node


if __name__ == '__main__':
    capacity = 3
    obj = LRUCache(capacity)
    obj.put(1, 2)
    obj.put(3, 4)
    param_1 = obj.get(3)
    print(param_1)
    obj.put(5, 6)
    obj.put(7, 8)
    param_1 = obj.get(3)
    print(param_1)
    param_1 = obj.get(7)
    print(param_1)
    param_1 = obj.get(1)
    print(param_1)
