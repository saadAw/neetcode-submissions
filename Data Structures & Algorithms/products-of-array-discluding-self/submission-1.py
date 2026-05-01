class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = []
        right = []
        right = [1] * len(nums)
        
        #from left
        for i in range(len(nums)):
            if i == 0:
                left.append(1)
                continue
            left.append(left[i-1] * nums[i-1])


        #from right
        for i in range(len(nums) -1, -1, -1):
            if i == len(nums)-1:
                right[i] = 1
                continue
            right[i] = right[i+1] * nums[i+1]
        
        product = [1] * len(nums)
        
        for i in range(len(nums)):
            product [i] = left[i] * right[i]

        return product