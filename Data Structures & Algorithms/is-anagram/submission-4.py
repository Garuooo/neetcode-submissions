class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_map = defaultdict(int)
        s_map = defaultdict(int)
        for c in s:
            s_map[c] += 1

        for c in t:
            t_map[c] += 1

        return t_map == s_map