# 合并两个有序数组
def merge(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    if i == len(a):
        c = c + b[j:]
    else:
        c = c + a[i:]
    return c


# 递归拆分数组
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


class Solution:
    # 排序两个数组
    def sort(self, a, b):
        arr = []
        la, lb = 0, 0
        while la < len(a) and lb < len(b):
            if a[la] < b[lb]:
                arr.append(a[la])
                la += 1
            else:
                arr.append(b[lb])
                lb += 1
        if la < len(a):
            arr.extend(a[la:])
        if lb < len(b):
            arr.extend(b[lb:])
        return arr

    # 递归拆分数组
    def merge(self, a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        l = self.merge(a[:mid])
        r = self.merge(a[mid:])
        return self.sort(l, r)


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    # print(merge_sort(a))
    print(Solution().merge(a))
