
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_counter = Counter(t)
        s_counter = Counter()
        left = 0
        min_len = float("inf")
        min_window = ""
        required_chars = len(t_counter)
        formed_chars = 0
        
        for right in range(len(s)):
            s_counter[s[right]] += 1
            
            if s[right] in t_counter and s_counter[s[right]] == t_counter[s[right]]:
                formed_chars += 1
            
            while left <= right and formed_chars == required_chars:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                
                s_counter[s[left]] -= 1
                if s[left] in t_counter and s_counter[s[left]] < t_counter[s[left]]:
                    formed_chars -= 1
                
                left += 1
        
        return min_window
