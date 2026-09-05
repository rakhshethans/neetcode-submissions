# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse through the linked list
        # for every connection between nodes, flip them
        nextNode = head
        prevNode = None
        while nextNode:
            temp = nextNode.next
            nextNode.next = prevNode
            prevNode = nextNode
            nextNode = temp
        
        return prevNode
        
            