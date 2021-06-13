class Solution:
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def getPrefixes(word):
            n = len(word)
            prefixes = []
            for i in range(n):
                if word[i:] == word[i:][::-1]:
                    prefixes.append(word[:i])
                    
            return prefixes
                    
            
        def getSuffixes(word):
            n = len(word)
            suffixes = []
            for i in range(n):
                if word[:i+1] == word[:i+1][::-1]:
                    suffixes.append(word[i+1:])
                    
            return suffixes
         
        #storing words with indices in a dictionary
        word_dict = {word:i for i,word in enumerate(words)}
        #print(word_dict)
        
        result = []
        
        
        
        for index,word in enumerate(words):
            reversed_word = word[::-1]
            
            #when exact reverse of current word exists in words
            
            if reversed_word in word_dict and index!=word_dict[reversed_word]:
                result.append([index,word_dict[reversed_word]])
                
        
            #for prefixes
        
            prefixes = getPrefixes(word)
            #print("prefixes",prefixes)
            
            for prefix in prefixes:
                reversed_prefix = prefix[::-1]
                
                if reversed_prefix in word_dict:
                    result.append([index,word_dict[reversed_prefix]])
                                   
        
            #for suffixes
                                   
            suffixes = getSuffixes(word)
            #print("suffixes",suffixes)
            
            for suffix in suffixes:
                reversed_suffix = suffix[::-1]
                
                if reversed_suffix in word_dict:
                    result.append([word_dict[reversed_suffix],index])
                    
                    
        #print("res",result)
        
        return result