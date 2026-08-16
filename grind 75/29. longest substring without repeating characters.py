class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """using dict"""
        # left=right=0
        # ans = 0
        # hashmap = defaultdict(int)
        # while(right<len(s)):
        #     hashmap[s[right]]+=1
        #     while (hashmap[s[right]] > 1):
        #         hashmap[s[left]]-=1
        #         left+=1
        #     right+=1
        #     ans = max(ans, right-left)
        # return ans

        
        """using set"""
        left=right=0
        ans = 0
        hashset = set()
        while(right<len(s)):
            while (s[right] in hashset):
                hashset.remove(s[left])
                left+=1
            hashset.add(s[right])
            right+=1
            ans = max(ans, right-left)
        return ans