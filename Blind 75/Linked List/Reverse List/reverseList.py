from typing import Optional

class ListNode:
    
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list.

        Parameters:
        - head (Optional[ListNode]): The head node of the input linked list.

        Returns:
        - Optional[ListNode]: The head node of the reversed linked list.

        """

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev