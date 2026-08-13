""" similar to valid anagram

hashmap
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = {}
        for i in ransomNote:
            if i in hash:
                hash[i]+=1
            else:
                hash[i] = 1
        
        for i in magazine:
            # remove elements from hashmap
            if i in hash:
                if hash[i]>1:
                    hash[i]-=1
                else:
                    hash.pop(i)
            if len(hash)==0:
                return True

        
        if len(hash)>0:
            return False
        return True