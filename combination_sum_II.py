class Solution:
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
        res = set()
        
        if sum(candidates)<target:
            return None
        
        def combinations(index, candidates, target, temp, res):
            if target == 0:
                res.add(tuple(temp))
                return
            
            if target<0:
                return
            
            for i in range(index,len(candidates)):
                temp.append(candidates[i])
                j = i+1
                combinations(j,candidates, target-candidates[i],temp, res)
                temp.pop()
                
        combinations(0,candidates, target,[],res)
        
        
        result = []
        for i in res:
            result.append(list(i))
            
        return result
    

            
            
        
        
        