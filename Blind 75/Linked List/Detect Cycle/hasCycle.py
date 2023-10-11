from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list has a cycle using Floyd's cycle detection algorithm.

        Parameters:
        - head (Optional[ListNode]): The head node of the linked list.

        Returns:
        - bool: True if the linked list has a cycle, otherwise False.
        """

        if not head:
            return False
        
        slow_ptr = head
        fast_ptr = head.next

        while True:

            if fast_ptr is None or fast_ptr.next is None:
                return False
            
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True