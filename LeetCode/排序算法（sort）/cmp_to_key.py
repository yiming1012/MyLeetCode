"""
如果元组里第一个元素是奇数，就用元组里第一个元素进行排序，
如果元组里第一个元素是偶数，则用这个元组里的第二个元组进行大小比较，
面对这样的需求，列表的sort方法无法满足。

"""

from functools import cmp_to_key


def cmp(x, y):
    a = x[0] if x[0] % 2 == 1 else x[1]
    b = y[0] if y[0] % 2 == 1 else y[1]

    # return 1 if a < b else -1 if a > b else 0
    return 1 if a > b else -1 if a < b else 0


lst = [(9, 4), (2, 10), (4, 3), (3, 6)]
lst.sort(key=cmp_to_key(cmp))


# print(lst)

def cmp2(x, y):
    print(x, y)
    if y > x:
        return 1
    elif x > y:
        return -1
    else:
        return 0


sst = [3, 2, 6, 4, 7, 1]
sst.sort(key=cmp_to_key(cmp2))
print(sst)

