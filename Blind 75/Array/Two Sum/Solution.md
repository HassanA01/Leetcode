## TwoSum Solution

The TwoSum problem can be effectively solved using a dictionary. This approach is described in detail below:

### Approach

1. **Initialize a Dictionary**: 
   * We use a dictionary to store complementary values. The key of the dictionary will be the <b>difference</b> between the target and `nums[i]`, and the value will be the index `i`. 
   * This setup is useful because when we encounter a number in the `nums` array, we can quickly check if its complement towards the target has been seen before.

2. **Loop Through the Numbers**: 
   For each number in the `nums` array, we calculate the required complement to reach the target sum.

   - If this complement is already a key in our dictionary, it means we've found a pair in the `nums` array that sums up to the target. In this case, we can immediately return a list containing the current index and the index stored in the dictionary for the complement.
   
   - Otherwise, add the current number and its index to the dictionary and continue the loop.

3. **Return Empty List if No Solution**:
   If we loop through the entire `nums` array without finding a pair that sums to the target, we simply return an empty list.

### Time and Space Complexity

- **Time Complexity**: The approach runs in <em>O(n)</em> time, where <i>n</i> is the number of elements in the `nums` array. This is because we traverse the `nums` array once, and dictionary operations (like checking for the existence of a key or adding a key-value pair) are on average \(O(1)\).
  
- **Space Complexity**: The space complexity is also <i>O(n)</i> because, in the worst case, we might store <b>all</b> numbers from the `nums` array in the dictionary.

---