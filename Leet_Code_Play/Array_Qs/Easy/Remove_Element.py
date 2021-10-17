class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = nums.count(val)
        nums =[i for i in nums if i != val]
        print(nums)
        return k


nums = [0,1,2,2,3,0,4,2]
val = 2

test = Solution()
print(test.removeElement(nums, val))
