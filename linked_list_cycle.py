'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

# one way is to store each node in a hashset and compare
# 2nd way is Floyd's Tortoise and Hare algo
# 2 pointers - one fast and slow : fast moves 2 nodes at a time and slow moves 1 node
# thoery is if there is a cycle then pointers will meet at the same point

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

def detect_cycle(head):

    # initialize slow and fast pointers
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # if both pointers meet then there is a cycle
        if slow == fast:
            return True
        
    return False