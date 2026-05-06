class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        seen = set()
        
        sort_nums = sorted(nums)

        if nums == []:
            return []

        for i in range(len(nums)-2):
            
            if sort_nums[i] in seen:
                continue
            
            seen.add(sort_nums[i])

            l = i + 1
            r = len(nums)-1

            while l < r:
                
                curr = sort_nums[i] + sort_nums[l] + sort_nums[r]
                
                if curr == 0:
                    ret.append([sort_nums[i], sort_nums[l], sort_nums[r]])
                    l += 1
                    while sort_nums[l] == sort_nums[l-1]:
                        l += 1
                        if l >= r: 
                            break

                if curr < 0:
                    l += 1
                    while sort_nums[l] == sort_nums[l-1]:
                        l += 1
                        if l >= r: 
                            break

                
                if curr > 0:
                    r -= 1
                    while sort_nums[r] == sort_nums[r+1]:
                        r -= 1
                        if l >= r: 
                            break
            
                    

        return ret
                
