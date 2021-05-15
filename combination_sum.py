class Solution:
    
    def combinations(self, index:int, candidates:List[int], target:int, combo:List[int], result:List[List[int]] ) -> List[List[int]] :
        
        if target==0:
            result.append(list(combo))
            return

        
        if target<0:
            return
        
        for i in range(index, len(candidates)):
            combo.append(candidates[i])
            self.combinations(i, candidates, target-candidates[i], combo, result)
            combo.pop()
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        index = 0
        result = []
        combo = []
        
        self.combinations(index, candidates, target, combo, result)
        
        return result
        

            
            
        
        
        
        
        
        