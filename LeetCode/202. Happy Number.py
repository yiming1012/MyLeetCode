'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        执行用时 :60 ms, 在所有 Python3 提交中击败了18.22%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.97%的用户
        思路：
        1、如果n<=0,return False
        2、如果不是happy number，肯定会无线循环，我们利用一个set存放每次的结果，如果出现一个数存在于set中，则返回FALSE
        :param n:
        :return:
        '''
        if n <= 0:
            return False
        res = set()
        while n != 1:
            sum = 0
            while n > 0:
                n, b = n // 10, n % 10
                sum += b ** 2
            if sum in res:
                return False
            res.add(sum)
            n = sum
        return True

    def isHappy2(self, n):
        """
        执行用时 :44 ms, 在所有 Python3 提交中击败了52.37%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.97%的用户
        思路：将数字看成字符串，计算后拼接
        :type n: int
        :rtype: bool
        """
        res = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in res:
                return False
            else:
                res.add(n)

        return True

    def isHappy(self, n: int) -> bool:
        '''
        思路：利用快慢指针判断是否有循环
        :param n:
        :return:
        '''
        n = str(n)
        slow = n
        fast = str(sum(int(i) ** 2 for i in n))
        while slow != fast:
            slow = str(sum(int(i) ** 2 for i in slow))
            fast = str(sum(int(i) ** 2 for i in fast))
            fast = str(sum(int(i) ** 2 for i in fast))
        return slow == "1"


"""
方法：使用“快慢指针”思想找出循环：“快指针”每次走两步，“慢指针”每次走一步，当二者相等时，即为一个循环周期。此时，判断是不是因为1引起的循环，是的话就是快乐数，否则不是快乐数。
注意：此题不建议用集合记录每次的计算结果来判断是否进入循环，因为这个集合可能大到无法存储；另外，也不建议使用递归，同理，如果递归层次较深，会直接导致调用栈崩溃。不要因为这个题目给出的整数是int型而投机取巧。

class Solution {
public:
    int bitSquareSum(int n) {
        int sum = 0;
        while(n > 0)
        {
            int bit = n % 10;
            sum += bit * bit;
            n = n / 10;
        }
        return sum;
    }
    
    bool isHappy(int n) {
        int slow = n, fast = n;
        do{
            slow = bitSquareSum(slow);
            fast = bitSquareSum(fast);
            fast = bitSquareSum(fast);
        }while(slow != fast);
        
        return slow == 1;
    }
};

"""


if __name__ == '__main__':
    n = 19
    s = Solution()
    print(s.isHappy(n))
