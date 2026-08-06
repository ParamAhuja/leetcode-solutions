
""" handling non-alnum and upper case while doing palindrome check

use simple 2 pointer and skip the alnums
use lower() before checking equality
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while (left<right):
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
            
        return True