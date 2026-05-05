class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        counter = 0

        for number in nums:
            if number-1 in nums_set:
                continue
            temp = 1

            while(number+1 in nums_set):
                temp += 1
                number += 1
                
            if temp > counter:
                    counter = temp
        return counter