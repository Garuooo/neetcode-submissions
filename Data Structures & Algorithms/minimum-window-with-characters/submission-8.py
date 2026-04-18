class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter=Counter(t)
        s_counter=Counter()
        left=right=0
        minimum=float("inf")
        res=""
        formed_characters=0

        while right < len(s):
            print(s[left:right+1])
            print(formed_characters)
            s_counter[s[right]]+=1
            if s == t:
                return t
            if s[right] in t_counter and s_counter[s[right]] == t_counter[s[right]]:
                print(s[right] in t_counter)
                print(s_counter[s[right]] == t_counter[s[right]])
                formed_characters+=1

            while left < len(s) and s_counter[s[left]] > t_counter[s[left]]:
                s_counter[s[left]]-=1
                left+=1

            if formed_characters == len(t):
                print("equal")
                if minimum > right-left+1:
                    minimum = right-left+1
                    res = s[left:right+1]
            right+=1
        return res
