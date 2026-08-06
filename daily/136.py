class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in hash:
            if hash[i] == 1:
                return i
# Find the number that appears once, and the other numbers twice


