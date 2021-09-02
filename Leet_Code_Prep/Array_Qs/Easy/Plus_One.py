class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        print(i)
        for i in reversed(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

digits = [1, 2, 9]
# digits = [4, 3, 2, 1]
# digits = [0]
# digits = [9]

print(Solution().plusOne(digits))