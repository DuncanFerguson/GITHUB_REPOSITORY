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
        print(max_sub)
        return max

        # for i in nums:
        #     print(i)




nums = [-2,1,-3,4,-1,2,1,-5,4]
test = Solution()
test.maxSubArray(nums)