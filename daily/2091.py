"""
greedy 
# revise
"""

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini = math.inf
        maxi = - math.inf
        a = None
        b = None
        for i, x in enumerate(nums):
            if x>maxi:
                b = i
                maxi = x
            if x<mini:
                a = i
                mini = x
        n = len(nums)
        # scenario1: remove from both sides
        i = min( (a+1 + n-b), (b+1 + n-a) )
        # scenario2: remove both from front
        j = max(a, b)+1
        # scenario3: remove both from end
        k = n-min(a, b)

        return min(i, j, k)

"""
stupid solution i did at first: rule based using indices
"""

        # mini = math.inf
        # maxi = - math.inf
        # a = None
        # b = None
        # for i, x in enumerate(nums):
        #     if x>maxi:
        #         b = i
        #         maxi = x
        #     if x<mini:
        #         a = i
        #         mini = x
        # n = len(nums)
        # ans = 0
        # # remove whichever is closer to the end first
        # if min((a+1), (n-a)) < min((b+1), (n-b)):
        #     # min element is closer, remove that. then update the index and len
        #     if (a+1) < (n-a):
        #         ans+=(a+1)
        #         n-= (a+1)
        #         if a<b:
        #             b-=(a+1)
        #     else:
        #         ans+=(n-a)
        #         n-= (n-a)

        #     # now, remove the other
        #     ans+=min((b+1), (n-b))

        # else:
        #     if (b+1) < (n-b):
        #         ans+=(b+1)
        #         n-= (b+1)
        #         if b<a:
        #             a-=(b+1)
        #     else:
        #         ans+=(n-b)
        #         n-= (n-b)

        #     ans+=min((a+1), (n-a))

        # return ans
