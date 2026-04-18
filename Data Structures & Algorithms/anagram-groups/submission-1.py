class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = defaultdict(list)
        for string in strs:
            values[str(sorted(string))].append(string)
        print(values)
        return values.values()