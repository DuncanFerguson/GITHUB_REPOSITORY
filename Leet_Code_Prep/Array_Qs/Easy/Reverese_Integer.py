class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:
            x = (int(str(x)[::-1]))
        else:
            x = (-int(str(x)[:0:-1]))
        if -2 ** 31 <= x <= (2 ** 31) - 1:
            return x
        else:
            return 0


# num = 123
num = 1534236469
# num = -321
# num = -10000

print(Solution().reverse(num))