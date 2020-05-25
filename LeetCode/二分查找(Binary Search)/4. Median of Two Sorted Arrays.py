"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
通过次数145,839提交次数395,459

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and B[j - 1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i - 1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0:
                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


"""
1、主要是将两个数组分成四个部分，交叉对比，确定是否需要移位，
2、如果A[i-1]>B[j],说明中位数在左边，将右边界缩小right=i-1
3、如果A[i]<B[j-1],说明中位数在右边，将左边边界扩大left =i+1
4、如果A[i-1]<=B[j]、A[i]>=B[j-1]，说明找到了合适位置
5、如果位置合适判断左右的值max(A[i-1],B[j-1])和右边最小值min(A[i-1],B[j-1])
6、需要考虑边界问题i==0,j==0,i==len(nums1),j==len(nums2)
"""


def findMedianSortedArrays(self, nums1, nums2):
    """
    执行用时 :56 ms, 在所有 Python3 提交中击败了97.15%的用户
    内存消耗 :13.5 MB, 在所有 Python3 提交中击败了36.20%的用户
    :param self:
    :param nums1:
    :param nums2:
    :return:
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    length1 = len(nums1)
    length2 = len(nums2)
    mid = (length1 + length2 + 1) // 2
    mod = (length1 + length2) % 2
    left = 0
    right = length1

    while left <= right:
        i = (left + right) // 2
        j = mid - i
        # 向左移动
        if i > 0 and nums1[i - 1] > nums2[j]:
            right = i - 1
        # 向右移动
        elif i < length1 and nums1[i] < nums2[j - 1]:
            left = i + 1
        # 位置合适
        else:
            # 判断是否是边界
            if i == 0:
                leftMax = nums2[j - 1]
            elif j == 0:
                leftMax = nums1[i - 1]
            else:
                leftMax = max(nums1[i - 1], nums2[j - 1])

            if mod == 1:
                return leftMax

            if i == length1:
                rightMin = nums2[j]
            elif j == length2:
                rightMin = nums1[i]
            else:
                rightMin = min(nums1[i], nums2[j])

            return (leftMax + rightMin) / 2


A = [1,3]
B = [2]
mid = median(A, B)
print(mid)
