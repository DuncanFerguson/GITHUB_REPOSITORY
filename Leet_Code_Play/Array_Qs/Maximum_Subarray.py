import math

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub = -math.inf
        for i in range(len(nums)):
            current_sub = 0
            for j in range(i, len(nums)):
                current_sub += nums[j]
                max_sub = max(max_sub, current_sub)
        return max_sub

nums = [-2, 5, -2, 6, 5, -10,-1, 1, 50, -24, 50, -6]
test = Solution()
print(test.maxSubArray(nums))