# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach:
# Linear check of node and next of node

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node is there or not
        if not head:
            return
        # assigning temp to head       
        temp = head
        # Check 
        while(temp and temp.next):
            # checking node and next node value
            if temp.val == temp.next.val:
                # Skipping out duplicate node
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head

# Time Complexity --    O(N)  as it traverse one time
# Space Complexity --   O(1)  as it not use any extra space 