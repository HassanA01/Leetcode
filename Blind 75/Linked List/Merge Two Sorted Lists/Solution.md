
## `mergeTwoLists` Method Explanation

The `mergeTwoLists` method is designed to merge two sorted linked lists into a single sorted linked list.

### Approach:

1. **Initial Check**:
    - If both `list1` and `list2` are `None`, return `None` since there are no elements to merge.

2. **Initialize Dummy Node**:
    - `head`: A dummy node that precedes the merged linked list.
    - `temp`: A pointer initialized to the `head` node, which helps in building the merged linked list.

3. **Merging Process**:
    - While both `list1` and `list2` have nodes:

        - Compare the values of the nodes that `list1` and `list2` point to.
        
        - If `list1`'s value is smaller, append `list1` to the merged list and move to the next node in `list1`.
        
        - Otherwise, append `list2` to the merged list and move to the next node in `list2`.
        
        - Advance the `temp` pointer to the end of the merged list.

4. **Append Remaining Nodes**:
    - After the while loop, at least one of `list1` and `list2` will be exhausted.
    - If `list1` is exhausted, append the remaining nodes from `list2` to the merged list.
    - If `list2` is exhausted, append the remaining nodes from `list1` to the merged list.

5. **Return Result**:
    - Return `head.next` to skip the dummy node and return the head of the merged linked list.

### Time and Space Complexity:

- **Time Complexity**: <i>O(n + m)</i>, where <i>n</i> is the number of nodes in `list1` and <i>m</i>  is the number of nodes in `list2`. This is because in the worst case, we have to traverse both lists entirely.
  
- **Space Complexity**: <i>O(1)</i>, since we are merging the lists in-place without allocating any new nodes except for the initial dummy node.