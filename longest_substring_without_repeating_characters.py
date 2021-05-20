class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        characters = [-1]*256
        start = -1
        longest = 0
        n = len(s)
        
        for i in range(n):
            if characters[ord(s[i])]>start:
                start = characters[ord(s[i])]
            longest = max(longest,i-start)
                
            characters[ord(s[i])] = i
            
        return longest