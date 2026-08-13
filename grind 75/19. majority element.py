"""
method 1: sorting the array and find middle element

method 2: hashmap and find element having more than floor n/2 count

method 3: boyer - moyer algorithm (THIS METHOD): based on the fact that if there is a majority element in an array, it will always remain in the lead, even after encountering other elements.

method 4: bit manipulation: based on that since the majority element appears more than \(\lfloor n / 2 \rfloor\) times, its bits will also appear more than \(\lfloor n / 2 \rfloor\) times
# todo
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1

        for i in nums[1:]:
            if i == majority:
                count+=1
            else:
                if count == 0:
                    count=1
                    majority = i
                else:
                    count-=1
        return majority
