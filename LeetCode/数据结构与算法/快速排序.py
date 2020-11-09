"""
模板一在数组有序的情况下，时间复杂度会退化到O(N^2)
模板二采用中位数作为pivot，可避免上述情况
"""


# 快速排序模板一
def quick_sort1(arr, left, right):
    if left < right:
        pivot = arr[right]
        l, r = left, right
        while left < right:
            while left < right and arr[left] <= pivot:
                left += 1
            while left < right and arr[right] >= pivot:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        arr[left], arr[r] = arr[r], arr[left]
        quick_sort1(arr, l, left - 1)
        quick_sort1(arr, left + 1, r)
    return arr


# 快速排序模板二
def quick_sort2(nums, l, r):
    if l >= r: return
    i, j = l, r
    # pivot = nums[random.randint(l,r)]
    pivot = nums[l + (r - l) // 2]
    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    quick_sort2(nums, l, j)
    quick_sort2(nums, i, r)
    return nums


if __name__ == '__main__':
    a = [4, 6, 7, 8, 3, 5, 9, 0, 1, 2]
    print(quick_sort1(a, 0, len(a) - 1))
    print(quick_sort2(a, 0, len(a) - 1))
