"""
topics:
hashmap, sliding window
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        ls = len(s)
        if lp>ls:
            return []
        
        hash_p = Counter(p)

        hash_w = Counter(s[0:lp])

        ans = []
        if hash_p == hash_w:
            ans.append(0)

        for i in range(1, ls-lp+1):
            hash_w[s[i-1]]-=1
            if hash_w[s[i-1]] == 0:
                hash_w.pop(s[i-1])
            if s[i+lp-1] in hash_w:
                hash_w[s[i+lp-1] ]+=1
            else:
                hash_w[s[i+lp-1] ] = 1
            if hash_p == hash_w:
                ans.append(i)
        return ans


"""
BETTER: used array for hashmap
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m=len(s),len(p)
        if n<m:
            return[]

        c1,c2=[0]*26,[0]*26
        for i in range(m):
            c1[ord(p[i])-97]+=1
            c2[ord(s[i])-97]+=1

        res=[]
        if c1==c2:
            res.append(0)

        for i in range(m,n):
            c2[ord(s[i])-97]+=1
            c2[ord(s[i-m])-97]-=1
            if c1==c2:
                res.append(i-m+1)

        return res
"""


"""
BEST: eliminate O(n) hashmaps equality check every time to O(1)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        c1, c2 = [0] * 26, [0] * 26
        
        # Populate initial target array (p) and first window (s[:m])
        for i in range(m):
            c1[ord(p[i]) - 97] += 1
            c2[ord(s[i]) - 97] += 1

        # Count initial matching character frequencies out of 26
        matches = 0
        for i in range(26):
            if c1[i] == c2[i]:
                matches += 1

        res = []
        if matches == 26:
            res.append(0)

        # Slide the window across s
        for i in range(m, n):
            # 1. Add right character (s[i])
            r_idx = ord(s[i]) - 97
            if c2[r_idx] == c1[r_idx]:
                matches -= 1  # Breaking a match
            c2[r_idx] += 1
            if c2[r_idx] == c1[r_idx]:
                matches += 1  # Creating a match

            # 2. Remove left character (s[i - m])
            l_idx = ord(s[i - m]) - 97
            if c2[l_idx] == c1[l_idx]:
                matches -= 1  # Breaking a match
            c2[l_idx] -= 1
            if c2[l_idx] == c1[l_idx]:
                matches += 1  # Creating a match

            # 3. If all 26 character frequencies match
            if matches == 26:
                res.append(i - m + 1)

        return res
"""