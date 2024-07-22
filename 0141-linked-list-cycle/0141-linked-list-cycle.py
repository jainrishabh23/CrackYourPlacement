# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach:
#  Using hare and tortoise method for finding cycle in LL

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Storing head to temp variable
        temp = head
        # assigning slow pointer to temp(head)
        slow = temp
        # assigning fast pointer to temp(head)
        fast = temp
        # Checking for the end node i.e. null 
        while(fast and fast.next):
            # move slow pointer by one step
            slow = slow.next
            # move fast pointer by two step
            fast = fast.next.next
            # Checking slow and fast pointer collision
            if slow == fast:
                # returning true in case of collision or loop
                return True


# Time Complexity --    O(N)  as it traverse one time
# Space Complexity --   O(1)  as it not use any extra space 