"""
hard
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # l = (nums1 + nums2)
        # l.sort()
        # n = len(l)
        # if n%2==0:
        #     a = l[n//2]
        #     b = l[n//2-1]
        #     return (a+b)/2
        # else:
        #     return l[n//2]

        # # or simply: 
        # return median(sorted(nums1 + nums2))

        """
        approach 2: two pointer
        """


        """
        optimal method: O(log(m+n))
        """
        # todo 
        