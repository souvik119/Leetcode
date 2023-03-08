'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

# Always check the top of list so use stack data structure
# Create a hashmap such that key is closing bracket and value is opening bracket
# Time complexity : O(n)
# Space complexity : O(n)

def isValid(s):
    stack = []
    closeToOpen = {')' : '(',
                   ']' : '[',
                   '}' : '{'}

    for c in s:
        # check if char is closing parentheses
        if c in closeToOpen: # because every key is closing paren
            # check if stack is not empty and matching pen bracket
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    # can return true only if stack is empty not otherwise
    return True if not stack else False

if __name__ == '__main__':
    print(isValid('(]'))