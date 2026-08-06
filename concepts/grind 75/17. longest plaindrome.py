"""
making a palindrome using letters - longest plaindrome

evens + maximum 1 odd
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = {}
        for i in s:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        
        countEven = 0
        countOdd = 0
        for i in hash:
            countEven+=hash[i]//2
            countOdd+=hash[i]%2
        ans = 2*countEven + min(1, countOdd)
        return ans