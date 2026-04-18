class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        res = 0
        for character in s:
            while character in chars:
                chars.pop(0)
            chars.append(character)
            res = max(res,len(chars))
        return res