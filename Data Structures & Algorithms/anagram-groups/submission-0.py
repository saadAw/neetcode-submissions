class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for strr in strs:
            sorted_strr = "".join(sorted(strr))
            
            if sorted_strr in hashmap:
                hashmap[sorted_strr].append(strr)
                continue

            hashmap[sorted_strr] = [strr]

        return list(hashmap.values())