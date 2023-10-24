from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted linked list.

        Parameters:
        - list1 (Optional[ListNode]): The head node of the first sorted linked list.
        - list2 (Optional[ListNode]): The head node of the second sorted linked list.

        Returns:
        - Optional[ListNode]: The head node of the merged sorted linked list.
        
        """
        
        if not list1 and not list2:
            return
        
        head = ListNode()
        temp = head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        if not list1:
            temp.next = list2
        else:
            temp.next = list1
        
        return head.next