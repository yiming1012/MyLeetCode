class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []



    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # print(self.arr)
        self.arr.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.arr)>0:
            last = self.arr[len(self.arr)-1]
            self.arr = self.arr[:len(self.arr)-1]
            return last
        else:
            return False


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.arr[len(self.arr)-1] if len(self.arr)>0 else False


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.arr)==0



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
print(obj)
param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
print(param_4)