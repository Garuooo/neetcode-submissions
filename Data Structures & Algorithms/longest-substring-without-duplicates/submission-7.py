class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        comb=[]
        if len(s)==1:
            return 1
        for letter in s:
            print(comb,letter,max_length)
            if letter not in comb:
                comb.append(letter)
            else:
                max_length=max(max_length,len(comb))
                while letter in comb:
                    comb.pop(0)
                comb.append(letter)
        return max(max_length,len(comb))