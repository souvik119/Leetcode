def insertionSort(arr):

    # traversing array from 1 to len(arr)
    for i in range(len(arr)):
        # current element to be compared with rest of sorted array
        temp = arr[i]

        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = temp