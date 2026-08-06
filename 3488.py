class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        n = len(nums)
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]].append(i)
            else:
                h[nums[i]]=[i]

        
        for j in queries:
            t_list = h[nums[j]]
            m = len(t_list)
            if m == 1:
                answer.append(-1)
                continue
            low = 0
            high = m-1
            mid = (high)//2
            while low<high:
                if t_list[mid] == j:
                    break
                elif t_list[mid]<j:
                    low= mid+1
                    mid = (low+high)//2
                else:
                    high = mid-1
                    mid = (low+high)//2
            a1 = abs(t_list[(mid+1)%m] - t_list[mid])
            a = min(a1, abs(n - a1))
            b1 = abs(t_list[(mid-1)%m] - t_list[mid])
            b = min(b1, abs(n - b1))
            ans = min( a , b )

            answer.append(ans)
        return answer