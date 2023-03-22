'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

def is_anagram(s, t):

    #check length
    if len(s) != len(t):
        return False
    
    mapS, mapT = {}, {}

    # create the hashmap of S and T
    for i in range(len(s)):
        # get sets default value if key does not exist        
        mapS[s[i]] = 1 + mapS.get(s[i], 0)
        mapT[t[i]] = 1 + mapT.get(t[i], 0)

    # compare the hashmaps
    for key in mapS:
        # get to avoid key error if key does not exist
        if mapS[key] != mapT.get(key, 0):
            return False
        
    return True
