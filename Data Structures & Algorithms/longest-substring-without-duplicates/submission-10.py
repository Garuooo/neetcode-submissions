class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = []
        max_res=0
        for index in range(len(s)):
            while s[index] in characters:
                characters.pop(0)
            characters.append(s[index])
            max_res=max(max_res,len(characters))
        return max_res