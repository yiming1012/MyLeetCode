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
    print(Solution().merge(a))
