class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        produkt_ohne = []

        for idx in range(len(nums)): 
                liste_ohne = nums[:idx] + nums[idx+1:]
                produkt_ohne.append(math.prod(liste_ohne))

        return produkt_ohne