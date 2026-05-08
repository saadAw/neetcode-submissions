class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        l = 0 
        seen = set()

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])

            curr = r - l + 1

            longest = max(longest, curr)

        return longest
