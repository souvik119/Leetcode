# simplest sorting technique, repeatedly swapping adjacent elements
# O(n ^ 2)

def bubbleSort(arr):
    # optimization if the array is already sorted no need to go through the entire process
    swapped = False

    for i in range(len(arr) - 1):
        # last i elements already in place
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                #swap elements
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if not swapped:
            return