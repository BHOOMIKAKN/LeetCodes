# Given
# a
# string
# s, find
# the
# length
# of
# the
# longest
# substring
# without
# duplicate
# characters.
#
# Example
# 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The
# answer is "abc",
# with the length of 3.
# Example
# 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The
# answer is "b",
# with the length of 1.
# Example
# 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The
# answer is "wke",
# with the length of 3.
# Notice
# that
# the
# answer
# must
# be
# a
# substring, "pwke" is a
# subsequence and not a
# substring.
#####################OUTPUT###################
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
'''