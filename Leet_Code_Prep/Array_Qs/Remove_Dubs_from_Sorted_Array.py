# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# # Throwing it into the set and casting it back into a list to get rid of the duplicates
# nums = list(set(nums))
# print(nums)
#
# # If we want to preserve the order AKA the list is not sorted
# new_nums = {}
# new_list = [new_nums.setdefault(x, x) for x in nums if x not in new_nums]
# print(new_list)

class Solution:
    def removeDuplicates(self, nums):
        return nums

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 1:
#             return nums
#         i, j = 1, 1
#         while i < len(nums):
#             if nums[i-1] != nums[i]:
#                 nums[j] = nums[i]
#                 j += 1
#             i += 1
#         return j

print(Solution().removeDuplicates([1,1,2]))





# Testing for Leet Code. Removing the nums but keeping their place value
# nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1, 1, 2]
# k = Solution().removeDuplicates(nums)
