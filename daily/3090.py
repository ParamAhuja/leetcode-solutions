"""
same as 2958 with k most frequency
sliding window, hashmap
"""

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = right = 0
        maxi = 0
        n = len(s)
        hash=defaultdict(int)
        while(right<len(s)):
            hash[s[right]]+=1
            while hash[s[right]] == 3:
                hash[s[left]]-=1
                left+=1
            right+=1
            maxi = max(maxi, right-left)
        return maxi