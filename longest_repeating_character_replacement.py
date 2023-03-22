'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

# want to replace the least frequently occuring character because we have limited k
# keep track of most occuring characters (use hashmap) in a window
# windowlen - count[max_count] = val <= k (if val is less than k then its valid)
# 2 pointers l and r starting from 0 and then right shifts fwd, left shifts based on condition windowlen - count[max_count] = val <= k
# keep track of current window length in res variable
# sliding window
# get max value from dictionary max(count.values())

def char_replacement(s, k):

    res = 0
    count = {}

    # initialize left pointer to start from 0
    l = 0
    for r in range(len(s)):
        # update hashmap with character
        count[s[r]] = 1 + count.get(s[r], 0)

        # if window is not valid
        # window length - maxcount is greater than k
        # shift left pointer ahead and remove that char count from dictionary
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        # store max res value till now which is max of res and current window
        res = max(res, r - l + 1)
    
    return res
