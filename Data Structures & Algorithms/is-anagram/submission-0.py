class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash={}
        t_hash={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            s_hash[s[i]]=s_hash.get(s[i],0)+1
            t_hash[t[i]]=t_hash.get(t[i],0)+1
        print(s_hash,t_hash)
        return t_hash==s_hash