class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # merge sorted arrays -
        # auxillary space solution -
        # ans = []
        # a = 0
        # b = 0
        # while (m)!=a and n!=b:
        #     if nums1[a]<nums2[b]:
        #         ans.append(nums1[a])
        #         a+=1
        #     else:
        #         ans.append(nums2[b])
        #         b+=1
        # if a==m:
        #     ans = ans + nums2[b:n]
        # else:
        #     ans = ans + nums1[a:m]

        # in place solution -
        i = m - 1 
        j = n - 1  
        k = m + n - 1  
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # method 3:
        # make a hashmap and reconstuct the array -