'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''

# 2 diverging pointers starting from each position

def longest_pallindrome(s):

    res = ""
    reslen = 0

    for i in range(len(s)):

        # odd length strings
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > reslen:
                res = s[l:r+1]
                reslen = r - l + 1
            
            l -= 1
            r += 1

        #even length strings
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > reslen:
                res = s[l:r+1]
                reslen = r - l + 1
            
            l -= 1
            r += 1

    return res