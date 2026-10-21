"""
already sorted -> return 0
length is 2 -> return -1
(smallest character is at first) or (largest character is at last) -> return 1
(one and only largest character at first) and (one and only smallest character at last) -> return 3
fallback -> return 2
"""
class Solution:
    def minOperations(self, s: str) -> int:
        def isSorted(substring, left, right): # inclusive of left and right indices
            for i in range(left, right):
                if s[i+1]<s[i]:
                    return False
            return True
        right = len(s)-1
        left = 0
        if isSorted(s, left, right):
            return 0
        elif right==1:
            return -1
        

        minimal = s[0]
        maximal = s[0]
        minimal_count = 0
        maximal_count = 0
        for i in s:
            if i==minimal:
                minimal_count +=1
            elif i<minimal:
                minimal = i
                minimal_count = 1

            if i==maximal:
                maximal_count +=1
            elif i>maximal:
                maximal = i
                maximal_count = 1

        
        if minimal == s[left] or maximal == s[right]:
            return 1
        elif s[0]==maximal and maximal_count==1 and s[-1] == minimal and minimal_count==1:
            return 3
        else:
            return 2


# another:
# class Solution:
#     def minOperations(self, s: str) -> int:
#         n = len(s)
#         mx, mn = max(s), min(s)
#         if all(a <= b for a, b in zip(s, s[1:])):
#             return 0
#         if n == 2:
#             return -1
#         if s[0] == mn or s[-1] == mx:
#             return 1
#         for i in range(1, n - 1):
#             if s[i] == mn or s[i] == mx:
#                 return 2
#         return 3