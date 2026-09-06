# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        # reverse the right half of the list
        # merge the 2 lists altenately

        # find the middle of the list
        # the end of the first half should point to none
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        middle = slow   # now we have the middle of the list

        second = slow.next
        slow.next = None

        # reverse from the middle of the list to the end
        nextNode = second
        middle.next = None
        prevNode = None

        while nextNode:
            temp = nextNode.next
            nextNode.next = prevNode
            prevNode = nextNode
            nextNode = temp
        # prevNode points to the start of the second half now
        # merge the 2 lists alternatively
        
        first = head
        second = prevNode

        while second:
            temp = first.next
            temp2 = second.next

            first.next = second
            second.next = temp

            first = temp
            second = temp2    
        
        

