"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MinStack:
    """
    思路：同步栈
        1. 定义两个栈stack和minStack。
        2. stack每次记录新加入的数据，minStack同步记录当前的最小值
        3. 保证每次stack和minStack同步执行，两个栈的大小相等
    时间复杂度：O(1)
    空间复杂度：O(n)
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            self.minStack.append(min(x, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


class MinStack2:
    """
    思路：不同步栈
        1. 定义两个栈stack和minStack。
        2. stack每次记录新加入的数据，如果新加入的元素比当前最小值还小，则加入minStack，这里需注意相等值也要加到minStack中
        3. 在pop出栈的时候，如果stack和minStack的栈顶元素相同，则一同pop，否则，仅stack出栈
    时间复杂度：O(1)
    空间复杂度：O(n)
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(1)
    obj.pop()
    obj.push(2)
    obj.push(3)
    obj.pop()
    obj.push(4)
    obj.push(6)
    obj.push(5)
    obj.getMin()


    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)


