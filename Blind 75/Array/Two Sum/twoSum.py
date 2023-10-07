from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums: A list of integers in which we want to find the pair of integers that sum up to <target>
        
        Return the indicies of the two numbers which add to <target>
        """

        d = {}
        
        for i in range(len(nums)):
            if target - nums[i] not in d:
                d[nums[i]] = i
            else:
                return [i, d[target - nums[i]]]
        
        return []
    