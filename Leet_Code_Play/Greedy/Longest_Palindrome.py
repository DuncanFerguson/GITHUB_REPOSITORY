

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Creating and filling out a dictionary with letter counts
        count = 1
        for i in set(s):
            x = s.count(i)
            if x > 1:
                if x % 2 == 0:
                    count += x
                else:
                    count += x-1
        max = (count if len(s) >= count else count-1)
        return max

s = "abccccdd"
test = Solution()
test.longestPalindrome(s)