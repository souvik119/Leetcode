'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

def majority_element(nums):
    num_count = {}
    for num in nums:
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num] += 1

        if num_count[num] > len(nums)/2:
            return num
        
if __name__ == '__main__':
    print(majority_element([3,2,3]))
    print(majority_element([2,2,1,1,1,2,2]))