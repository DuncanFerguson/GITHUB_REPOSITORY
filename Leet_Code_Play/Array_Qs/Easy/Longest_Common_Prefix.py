# Slow Option
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         prefix = strs[0]
#         for i in range(1, len(strs)):
#             prefix = self.commonPrefix(prefix, strs[i])
#         return prefix
#
#     def commonPrefix(self, str1, str2):
#         result = ""
#         i, j = 0, 0
#         while i <= len(str1)-1 and j <= len(str2)-1:
#             if str1[i] != str2[j]:
#                 break
#             result += str1[i]
#             i += 1
#             j += 1
#         return result


class Solution:
    def longestCommonPrefix(self, strs):
        i = 0
        prefix = ""
        while True:
            temp = ""
            for k in range(len(strs)):
                if i == len(strs[k]):
                    return prefix
                if k == 0:
                    temp = strs[k][i]
                elif strs[k][i] != temp:
                    return prefix
            prefix += temp
            i += 1

        return prefix


# word = ['flow', 'flow', 'flow']
# word = ["flower", "flow", "flight"]
# word = ["dog", "racecar", "car"]
word = ["ab", "a"]

print(Solution().longestCommonPrefix(word))