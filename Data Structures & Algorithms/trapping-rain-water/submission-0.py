class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l = 0
        r = len(height) - 1

        highest_l = height[l]
        highest_r = height[r]

        water_trapped = 0

        while l < r:

            if highest_l < highest_r:
                l += 1
                
                highest_l = max(highest_l, height[l])
            
                water_trapped += highest_l - height[l]
                
            else:
        
                r -= 1
               
                highest_r = max(highest_r, height[r])
                
                water_trapped += highest_r - height[r]

        return water_trapped