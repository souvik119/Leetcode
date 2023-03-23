# O(n ^ 2)
# selection sort repeatedly gets the lowest element from unserted part of array to sorted part

def selectionSort(arr):

    for i in range(len(arr) - 1):
        # assume min value at current sorted portion
        min_val_index = i
        
        for j in range(i+1, len(arr)):
            # finding lowest element from unsorted portion of list
            if arr[j] < arr[min_val_index]:
                min_val_index = j
        
        #swapping elements to sort array
        arr[i], arr[min_val_index] = arr[min_val_index], arr[i]
