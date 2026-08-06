# l=[1,1,2,3]

# print(l)
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        for i in arr:
            if arr.count(i)==1:
                k-=1
            if k==0:
                return i
        return ""