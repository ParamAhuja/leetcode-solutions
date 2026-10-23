# redo - nice question

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        comm = 2**(ceil(log2(n)))-1
        isSorted = True

        for i in range(n):
            if nums[i]!=i:
                # print(comm, nums[i])
                comm = comm & nums[i]
                isSorted = False

        if not isSorted: return comm
        else: return 0