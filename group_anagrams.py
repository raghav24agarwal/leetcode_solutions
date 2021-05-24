class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = {}
        
        for i in strs:
            word = i
            sorted_word = "".join(sorted(i))
            
            if sorted_word in anagram:
                anagram[sorted_word].append(word)
            else:
                anagram[sorted_word] = [word]
        
        result = []
        
        for key in anagram:
            result.append(anagram[key])
            
        return result
    
