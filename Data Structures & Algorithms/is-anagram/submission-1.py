class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)
        for element in s:
            hash_s[element] = hash_s[element]+1

        for element in t:
            hash_t[element] = hash_t[element]+1
        
        return hash_t == hash_s