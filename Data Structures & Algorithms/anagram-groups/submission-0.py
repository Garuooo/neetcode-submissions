class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams={}
        for word in strs:
            letters=[0 for i in range(26)]
            for letter in word:
                letters[ord(letter)-ord("a")]+=1
            anagrams[tuple(letters)]=anagrams.get(tuple(letters),[]) + [word]

        return list(anagrams.values())