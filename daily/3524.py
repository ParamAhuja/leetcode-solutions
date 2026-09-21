# do again

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # TLE:
        # result = [0]*k
        # n = len(nums)
        # for i in range(n):
        #     prod = 1
        #     for j in range(i, n):
        #         prod *=nums[j]
        #         idx = prod%k
        #         result[idx] +=1
        # return result


        # dp:
        result = [0]*k
        n = len(nums)
        dp = [0]*k # array to keep track of what subarrays ended were processed last time
        for i in range(n):
            # add that element to subarrays - stretch or solo
            r = nums[i]%k
            updates = [0]*k
            updates[r]+=1
            for x in range(k):
                updates[(x * r)%k] += dp[x]
                # take each remainder x in result, it represents number of subarrays that ended on x
                # we need to find what remainder would they give if we stretch to add nums[i], and update "updates" for result[x] times that
            for j in range(len(updates)):
                result[j]+=updates[j]
            dp = updates
        return result