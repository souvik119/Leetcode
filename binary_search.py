# list must be sorted
# O(log n)

def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        # number in left half
        if nums[mid] > target:
            r = mid - 1
        # number in right half
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
        
    return -1


