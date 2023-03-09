'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
'''

# general linkedlist class structure

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# use a dummy element at the front to avoid edge cases
# tail pointer points to dummy node initially

def merge_lists(l1, l2):
    # create a dumy node at the beginning to handle edge cases
    dummy = ListNode()
    # tail pointer points to dummy node
    tail = dummy

    # compare 2 lists and move pointers accordingly
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        # tail has to point to next no matter what
        tail = tail.next
    
    # if any of the lists remain just append it to tail
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    
    return dummy.next

