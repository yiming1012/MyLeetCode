from typing import List


class Solution:
    count=0
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        n = len(A)
        arr= self.move(n, A, B, C)
        num=self.count
        print(num,arr)

    # 定义move 函数移动汉诺塔
    def move(self, n, A, B, C):
        self.count += 1
        if n == 1:
            C.append(A[-1])
            A.pop()
            return
        else:
            self.move(n - 1, A, C, B)  # 将A上面n-1个通过C移到B
            C.append(A[-1])  # 将A最后一个移到C
            A.pop()  # 这时，A空了
            self.move(n - 1, B, A, C)  # 将B上面n-1个通过空的A移到C
        return C


if __name__ == '__main__':
    A, B, C = [3, 2, 1, 0], [], []
    print(Solution().hanota(A, B, C))

