'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class MyQueue:
    '''
    执行用时 :36 ms, 在所有 Python3 提交中击败了64.07%的用户
    内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.77%的用户
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.stackLeft = []
        self.stackRight = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stackLeft.append(x)
        self.stackRight = self.stackLeft[::-1]

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stackLeft) > 0:
            top = self.stackRight.pop()
            self.stackLeft = self.stackRight[::-1]
            return top
        else:
            return -1

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stackLeft) > 0:
            return self.stackRight[-1]
        else:
            return -1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # if len(self.stackLeft)==0:
        #     return True
        # else:
        #     return False

        return len(self.stackLeft) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.stackLeft = []
        self.stackRight = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stackLeft.append(x)
        self.stackRight = []
        tmp = self.stackLeft.copy()
        while len(tmp) != 0:
            self.stackRight.append(tmp.pop())
        print(self.stackLeft)
        print(self.stackRight)
        # self.stackRight=self.stackLeft[::-1]

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stackRight) > 0:
            top = self.stackRight.pop()
            self.stackLeft = []
            tmp = self.stackRight.copy()
            while len(tmp) != 0:
                self.stackLeft.append(tmp.pop())
            # self.stackLeft=self.stackRight[::-1]
            return top
        else:
            return -1

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stackRight) > 0:
            return self.stackRight[-1]
        else:
            return -1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # if len(self.stackLeft)==0:
        #     return True
        # else:
        #     return False

        return len(self.stackLeft) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
