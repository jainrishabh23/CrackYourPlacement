# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:


        d1 = head1
        d2 = head2
        while d1 != d2:
            d1 = head2 if d1 == None else d1.next
            d2 = head1 if d2 == None else d2.next
        return d1
    
        