'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

'''

# Brute Force - check each value with other from the list but this O(n squared)
# Use hashmap : value : index
# Check (target - current value) first then check if difference is in hashmap
# time: O(n)
# memory : O(n)

def twoSum(nums, target):
    prevMap = {} #value : index
    for i, num in enumerate(nums):
        if target - num in prevMap:
            return prevMap[target - num], i
        prevMap[num] = i

if __name__ == '__main__':
    print(twoSum([3,2,4], 6))