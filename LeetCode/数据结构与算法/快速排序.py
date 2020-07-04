# 快速排序
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


if __name__ == '__main__':
    a = [4, 6, 7, 8, 3, 5, 9, 0, 1, 2]
    print(quick_sort(a, 0, len(a) - 1))
