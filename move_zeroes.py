'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''

# Left pointer and right pointer to swap values
# Every time we see non zero value move to left
# right pointer at index 1 and left at index 0 and move according to where we find non zero value
# this algo also used in quicksort

def moveZeroes(nums):
    #setting up pointers
    l = 0
    #right pointer will iterate through the array
    for r in range(len(nums)):
        # if number is non zero then swap
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            #increment left pointer
            l += 1
    return nums

if __name__ == '__main__':
    print(moveZeroes([0,1,0,3,12]))
    print(moveZeroes([0]))