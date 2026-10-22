class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # operations:
        # 1. reverse: either at start (if right rotations are needed), or at end, if changing order
        # 2. left rotate

        # simplified goal:
        # to sort in ascending using left OR right rotations or descending then reverse

        # issues:
        # 1. check if possible to sort - using either ascending or descending config
        # 2. decide if to sort left or right side, whichever is cheaper


        # 1. find drops from both direction - if 2 or more exists in both, return -1, if <2 in any, use that
        n = len(nums)
        inc = 0
        dec = 0
        incIndex = None
        decIndex = None
        for i in range(n):
            if (nums[(i+1)%n] > nums[i]):
                inc+=1
                if incIndex==None:
                    incIndex = i
            else:
                dec+=1
                if decIndex==None:
                    decIndex = i
        if inc>=2 and dec>=2:
            return -1
        
        # what if inc and dec both are 1
        if inc==1 and dec==1:
            if incIndex<decIndex:
                return 0
            else:
                return 1

        
        if dec==1:
            # for 5 elems, decIndex should be index 4 for it to be sorted
            # if not, check which is better, reverse->rotate->reverse or directly reverse
            if decIndex==n-1:
                return 0
            if decIndex >= ceil(n/2):
                return 2 + ((n-1) - decIndex)
            else:
                return decIndex+1
        if inc==1:
            # for 5 elems, incIndex should be index 4 for it to be sorted
            # if not, check which is better, reverse->rotate or rotate->reverse
            # return 1+ min(incIndex-)
            if incIndex==n-1:
                return 1
            if incIndex >= n//2:
                return 1 + ((n-1) - incIndex)
            else:
                return 2 + incIndex 