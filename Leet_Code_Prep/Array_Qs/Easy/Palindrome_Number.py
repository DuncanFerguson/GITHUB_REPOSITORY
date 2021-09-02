# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         x = str(x)
#         for i in range(len(x)//2):
#             if x[i] != x[-i-1]:
#                 return False
#         return True

# Faster Solution. Just Flip and check
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        y = x[::-1]
        return bool(str(y) == x)




num = 12
# num = 111

print(Solution().isPalindrome(num))