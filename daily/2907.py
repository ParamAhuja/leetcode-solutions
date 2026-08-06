#Brute Force--

# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
#         l=len(rating)
#         count=0
#         for i in range(0,l-2):
#             for j in range(i+1,l-1):
#                 for k in range(j+1,l):
#                     if (rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]):
#                         count+=1
#         return count


class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n=len(rating)
        count=0
        for i in range(1,n-1): 
            low=0
            high=0
            rev_low=0
            rev_high=0
            for j in range(0,i):
                if rating[j]<rating[i]:
                    low+=1
                else:
                    rev_high+=1
            for k in range(i+1,n):
                if rating[i]<rating[k]:
                    high+=1
                else:
                    rev_low+=1
            count+= (high*low) + (rev_low * rev_high)
        return count
    
rating=[2,5,3,4,1]
myObject=Solution()
ans=myObject.numTeams(rating)
print(ans)
# expected- 3