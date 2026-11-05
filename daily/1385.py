# easy
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # ans = 0
        # for i in arr1:
        #     flag = True
        #     for j in arr2:
        #         if abs(i-j)<=d:
        #             flag=False
        #             break
        #     if flag:
        #         ans+=1
        # return ans

        arr2.sort()
        ans = 0
        for i in arr1:
            # first element greater than i
            l,r = 0, len(arr2)-1
            pos = len(arr2)
            while(l<=r):
                mid = (l+r)//2
                if arr2[mid]>i:
                    pos = mid
                    r = mid-1
                else:
                    l=mid+1
            if abs(arr2[pos-1] - i)>d and ((pos!=len(arr2) and abs(arr2[pos] - i)>d) or pos==len(arr2)):
                ans+=1
        return ans
