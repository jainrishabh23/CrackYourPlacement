# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach:
#  Using hare and tortoise method for finding middle node in LL

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Storing head to temp variable
        temp = head
        # assigning slow pointer at temp(head)
        slow = temp
        # assigning fast pointer at temp(head)
        fast = temp
        # Checking for the end node i.e. null 
        while(fast and fast.next):
            # move slow pointer by one step
            slow = slow.next
            # move fast pointer by two step
            fast = fast.next.next
        # returning the slow pointer or returning second half of linked list
        return slow


# Time Complexity --    O(N/2)  as it traverse one time
# Space Complexity --   O(1)  as it not use any extra space 