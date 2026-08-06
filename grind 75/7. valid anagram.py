""" anagrams are words made of same letters

use hashmap simply
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for i in s:
            if i in hash:
                hash[i]+=1
            else:
                hash[i] = 1
        
        for i in t:
            # remove elements from hashmap
            if i in hash:
                if hash[i]>1:
                    hash[i]-=1
                else:
                    hash.pop(i)
            else:
                return False

        
        if len(hash)>0:
            return False
        return True