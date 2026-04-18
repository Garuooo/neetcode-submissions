class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter=Counter(s1)
        s2_counter=Counter(s2[:len(s1)])
        if len(s1) > len(s2):
            return False

        if s1_counter == s2_counter:
            return True

        for index in range(len(s1),len(s2)):
            print(s1_counter,s2_counter)
            s2_counter[s2[index]]+=1
            s2_counter[s2[index-len(s1)]]-=1

            if s2_counter[s2[index-len(s1)]] ==0:
                del s2_counter[s2[index-len(s1)]]
            if s1_counter == s2_counter:
                return True
        return s1_counter == s2_counter