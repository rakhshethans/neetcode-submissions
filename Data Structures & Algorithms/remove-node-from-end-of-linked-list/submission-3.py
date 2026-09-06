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


        # how I made it more efficient after::
        # use a dummy node, this dummy node becomes the new head
        # this deals with edge cases where the head of the list is being removed

        dummy = ListNode(0, head)    # make a dummy node that points to head 

        fast = dummy
        # because we are using dummy as the head from here, we need to go to n+1 as dummy isn't the real head
        for i in range(n+1):
            fast = fast.next

        slow = dummy

        # at the end of this slow will point to the node BEFORE the node to remove, so we don't need a variable prev for the previous variable.
        while fast:
            slow = slow.next
            fast = fast.next
        # now slow is the nth node from the end
        # prev is the node before it
        
        # slow is one before the node to remove, set slow.next to slow.next.next to skip the node to remove
        slow.next = slow.next.next
 
        # we return dummy.next as this is the actual head of the list
        return dummy.next