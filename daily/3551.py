"""
pattern: minimum swaps 

topics: cycle detection/greedy, sorting 
"""

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digiSum(n):
            ans = 0
            while(n!=0):
                ans+=n%10
                n//=10
            return ans
        def swapper(arr, temp):
            """
            function to find minimum number of swaps needed from arr to temp
            """
            n = len(arr)
            vis = [False] * n

            pos = {}
            for i in range(len(arr)):
                pos[arr[i]] = i

            swaps = 0
            for i in range(n):
                if vis[i] or pos[temp[i]] == i:
                    continue

                j, cycleSize = i, 0
                while not vis[j]:
                    vis[j] = True

                    j = pos[temp[j]]
                    cycleSize += 1

                if cycleSize > 0:
                    swaps += (cycleSize - 1)
            return swaps

        # ---- reference of digi sum to sort
        ref = []
        for i in nums:
            ref.append(digiSum(i))

        # ---- sort temp using ref (merge sort)
        # (better) alternative:
        # n = len(nums)
        # indexed_nums = [(nums[i], digit_sum(nums[i]), i) for i in range(n)]
        
        # # Sort based on digit sum, then by value
        # temp = sorted(indexed_nums, key=lambda x: (x[1], x[0]))

        temp = nums.copy()
        n = len(temp)

        def merge(temp, ref, left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid

            # Create temp arrays
            Lr = [0] * n1
            Rr = [0] * n2
            Lt = [0] * n1
            Rt = [0] * n2

            # Copy data to arrays L and R
            for i in range(n1):
                Lr[i] = ref[left + i]
                Lt[i] = temp[left + i]
            for j in range(n2):
                Rr[j] = ref[mid + 1 + j]
                Rt[j] = temp[mid + 1 + j]
                
            i = 0  
            j = 0  
            k = left  

            # Merge the temp arrays back
            # into originals
            while i < n1 and j < n2:
                if Lr[i] < Rr[j]:
                    temp[k] = Lt[i]
                    ref[k] = Lr[i]
                    i += 1
                elif Lr[i] == Rr[j]:
                    if Lt[i] <= Rt[j]:
                        temp[k] = Lt[i]
                        ref[k] = Lr[i]
                        i += 1
                    else:
                        temp[k] = Rt[j]
                        ref[k] = Rr[j]
                        j += 1
                else:
                    temp[k] = Rt[j]
                    ref[k] = Rr[j]
                    j += 1
                k += 1

            # Copy the remaining elements of L[],
            # if there are any
            while i < n1:
                temp[k] = Lt[i]
                ref[k] = Lr[i]
                i += 1
                k += 1

            # Copy the remaining elements of R[], 
            # if there are any
            while j < n2:
                temp[k] = Rt[j]
                ref[k] = Rr[j]
                j += 1
                k += 1

        def mergeSort(temp, ref, left, right):
            if left < right:
                mid = (left + right) // 2

                mergeSort(temp, ref, left, mid)
                mergeSort(temp, ref, mid + 1, right)
                merge(temp, ref, left, mid, right)
        mergeSort(temp, ref, 0, n-1)

        return swapper(nums, temp)