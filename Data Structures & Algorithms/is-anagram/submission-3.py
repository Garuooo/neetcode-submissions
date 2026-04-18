class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_map = defaultdict(int)
        s_map = defaultdict(int)
        characters = set()
        for c in s:
            s_map[c] += 1
            characters.add(c)

        for c in t:
            t_map[c] += 1
            characters.add(c)

        return t_map == s_map