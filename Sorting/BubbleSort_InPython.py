def swap(arr, i,j):
    arr[i], arr[j] = arr[j], arr[i]

def bubblesort(arr):
    size = len(arr)

    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

    return arr

sample_array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
sorted_array = bubblesort(sample_array)

print("The Buble SortedArray", sorted_array)

