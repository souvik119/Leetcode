'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
1>2>3>4>5
5>4>3>2>1

Example 2:
1>2
2>1

Example 3:
[]
[]
'''

# Iterative approach
# Need 2 pointers prev, curr
# prev will be 1 step behind curr pointer
# Time complexity O(n)
# Mem complexity O(1) because just use pointers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev, curr = None, head

    #till the end of list
    while curr:
        #nxt is temp variable to hold next value
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev