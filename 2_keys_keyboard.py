class Solution:
    
    keys = [0]*1001
        
    keys[2], keys[3] = 2, 3
        
    for i in range(4,1001):
            
        minn = i
        for j in range(1,i):
            if i%j==0:
                cost = i//j
                cost += keys[j]
                    
                if cost<minn:
                    minn = cost
                        
        keys[i] = minn
            
    
    def minSteps(self, n: int) -> int:
        
        return self.keys[n]