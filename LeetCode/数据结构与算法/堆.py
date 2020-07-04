import heapq

heap = []

# 以堆的形式插入堆
heapq.heappush(heap, 0)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
# 向堆中插入元素，heapq会维护列表heap中的元素保持堆的性质
heapq.heappush(heap, 4)
# heapq把列表x转换成堆
heapq.heapify(heap)
# 从可迭代的迭代器中返回最大的n个数，可以指定比较的key
# heapq.nlargest(n, iterable[, key])
arr = heapq.nsmallest(2, heap)
print(arr)
# 从可迭代的迭代器中返回最小的n个数，可以指定比较的key
# heapq.nsmallest(n, iterable[, key])
# 从堆中删除元素，返回值是堆中最小或者最大的元素
top = heapq.heappop(heap)
print("堆顶元素：", top)
