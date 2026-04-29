class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = defaultdict(int)

        for i in nums:
            seen[i] += 1
        
        sorted_dict = dict(sorted(seen.items(), key=lambda x: x[1]))
        return list(sorted_dict.keys())[-k:]