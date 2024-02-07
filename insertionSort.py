def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
        print(arr)
    return arr


if __name__ == "__main__":
    insertionSort([1, 4, 3, 5, 6, 2])
