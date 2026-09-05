# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currOne = list1
        currTwo = list2

        dummy = ListNode()
        tail = dummy 

        while currOne and currTwo:
            if currOne.val < currTwo.val:
                # add currOne and move it forward
                tail.next = currOne
                tail = tail.next
                currOne = currOne.next
            else:
                tail.next = currTwo
                tail = tail.next
                currTwo = currTwo.next

        # if one of them has a remainder, add them

        tail.next = currOne if currOne else currTwo   

        return dummy.next
        