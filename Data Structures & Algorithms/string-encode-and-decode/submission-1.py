class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for string in strs:
            res += string + "#zeko#"
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("#zeko#")
        return res[:len(res)-1]