class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        
        def recursion(matchsticks, sides, index):
            if index==len(matchsticks):
                if sides[0]==sides[1]==sides[2]==sides[3]==0:
                    return True
                else:
                    return False

            
            for i in range(0,4):
                if matchsticks[index]>sides[i]:
                    continue
                    
                sides[i]-=matchsticks[index]
                if recursion(matchsticks, sides, index+1):
                    return True
                sides[i]+=matchsticks[index]
                
                
            return False
        
        
        total_sum = sum(matchsticks)
        if total_sum%4 != 0:
            return False
        
        if len(matchsticks)<4:
            return False
        
        matchsticks.sort(reverse = True)
        
        target = total_sum//4
        
        if matchsticks[0]>target:
            return False
        
        sides = [target] * 4

        return recursion(matchsticks,sides,0)