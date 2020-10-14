# 快速排序模板一
def quick_sort(arr, left, right):
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
        arr[left], a[r] = arr[r], arr[left]
        quick_sort(arr, l, left - 1)
        quick_sort(arr, left + 1, r)
    return arr


# 快速排序模板二
def quicksort(nums, start, end):
    if start >= end:
        return
    left, right = start, end
    pivot = nums[(start + end) // 2]

    while left <= right:
        while left <= right and nums[left] <= pivot:
            left += 1
        while left <= right and nums[right] >= pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    quicksort(nums, start, right)
    quicksort(nums, left, end)
    return nums


if __name__ == '__main__':
    a = [4, 6, 7, 8, 3, 5, 9, 0, 1, 2]
    print(quick_sort(a, 0, len(a) - 1))
    print(quicksort(a, 0, len(a) - 1))
