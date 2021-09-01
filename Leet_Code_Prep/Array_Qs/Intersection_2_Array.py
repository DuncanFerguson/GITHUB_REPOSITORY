class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort(), nums2.sort()
        i1, i2 = 0, 0
        intersection = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                intersection.append(nums1[i1])
                i1 += 1
                i2 += 1
        return intersection

nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersect(nums1, nums2))