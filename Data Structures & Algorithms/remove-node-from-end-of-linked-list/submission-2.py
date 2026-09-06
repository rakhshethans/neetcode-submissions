# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # to find the nth node, use two pointers
        # they have a difference of n between them
        # the first pointer will point to that node
        # once found, store the previous node and set the node.next of that to the node.next of the current node
        # then return head

        fast = head
        for i in range(n):
            fast = fast.next

        slow = head
        prev = None

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        # now slow is the nth node from the end
        # prev is the node before it
        if prev:
            prev.next = slow.next
        elif slow.next:
            head = slow.next
        else:
            head = None
 
        
        return head