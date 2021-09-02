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
        i, j = 0, 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))

