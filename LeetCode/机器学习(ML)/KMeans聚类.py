"""
K-means：
    1.随机选取k个点作为起始点
"""
import sys
import gc
a = [1, 2, 3]
b = [2, 3, 4]
print(id(a))
print(id(b))
del a
gc.collect()
# print(a)
a = [1, 2, 4]
print(id(a))
