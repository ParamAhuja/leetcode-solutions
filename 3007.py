# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         n = len(s)
#         count = 0

#         for i in range(n-1):
#             if s[i]==s[i+1]=="a":
#                 continue
#             elif s[i]==s[i+1]=="b":
#                 continue
#             elif s[i]=="a" and s[i+1]=="b":
#                 continue
#             else:
#                 count+=1
#         return count


# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         count=0
#         for i in range(len(s)):
#             leftB=0
#             rightA=0
#             for j in range(0,i+1):
#                 if s[j]=="b":
#                     leftB+=1
#             for j in range(i+1,len(s)):
#                 if s[j]=="a":
#                     rightA+=1
#             if (leftB>=rightA and s[i]=="a"):
#                 count+=1
#             elif (leftB<rightA and s[i]=="b"):
#                 count+=1
#         return count

# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         count=0
#         n=len(s)
#         for i in range(n):
#             leftB=0
#             rightA=0
#             for j in range(0,i+1):
#                 if s[j]=="b":
#                     leftB+=1
#             for j in range(i+1,len(s)):
#                 if s[j]=="a":
#                     rightA+=1
#             cost = leftB + rightA
#             count=min( leftB ,count+1)
#         return count