def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) - 1]
    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

sample_array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
sorted_array = quick_sort(sample_array)
print("SortedArray", sorted_array)