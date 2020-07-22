class Solution:
    def __init__(self):
        self.current = set()
        # return

    def handle(self, input: list):
        input_set = set(input)
        items_add = input_set - self.current
        items_remove = self.current - input_set
        self.current = input_set
        return list(items_add), list(items_remove)


if __name__ == '__main__':
    t0 = []
    t1 = [1, 2, 3, 4, 5]
    t2 = [6, 7, 8, 3, 4, 11, 12]
    mim = Solution()
    items_add, items_remove = mim.handle(t0)
    print(items_add, items_remove)
    print(mim.current)
    items_add, items_remove = mim.handle(t1)
    print(items_add, items_remove)
    print(mim.current)
    items_add, items_remove = mim.handle(t2)
    print(items_add, items_remove)
    print(mim.current)
