Certainly!

Here's a short docstring for the `reverseList` method:

```python
class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list.

        Parameters:
        - head (Optional[ListNode]): The head node of the input linked list.

        Returns:
        - Optional[ListNode]: The head node of the reversed linked list.
        """
        # ... rest of the method ...
```

---

## `reverseList` Method Explanation

The `reverseList` method reverses a singly linked list.

### Approach:

1. **Initialization**:
    - `curr`: Points to the current node, starting with the `head` of the linked list.
    - `prev`: Initialized to `None`, represents the previous node which will become the next node for `curr` as we reverse the list.

2. **Traversal & Reversal**:
    - While the `curr` is not `None` (i.e., we haven't reached the end of the list):
    
        - Store the next node (`curr.next`) in a temporary variable `temp`.
        - Update `curr.next` to point to `prev`, effectively reversing the current node's direction.
        - Move `prev` to point to `curr`, preparing for the next iteration.
        - Move `curr` to the next node in the original sequence using `temp`.

3. **Return Reversed List's Head**:
    - After the loop, `curr` will be `None` and `prev` will point to the new head of the reversed list.
    - Return `prev` to successfully return the reversed Linked List.


### Time and Space Complexity:

- **Time Complexity**: <i>O(n)</i>, where <i>n</i> is the number of nodes in the linked list. This is because we traverse the linked list once.
  
- **Space Complexity**: <i>O(1)</i>, since we only use a constant amount of space regardless of the size of the linked list.

---