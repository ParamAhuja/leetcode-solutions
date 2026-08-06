class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # missing number
        # sum and expected sum
        sum = 0
        n = len(nums)
        for i in nums:
            sum+=i
        return int(fabs(n*(n+1)/2 - sum))
    
    #     method 2: xor operation
    #     n = len(arr) + 1
    #     xor1 = 0
    #     xor2 = 0

    #     # XOR all array elements
    #     for i in range(n - 1):
    #         xor2 ^= arr[i]

    #     # XOR all numbers from 1 to n
    #     for i in range(1, n + 1):
    #         xor1 ^= i

    #     # Missing number is the XOR of xor1 and xor2
    #     return xor1 ^ xor2
