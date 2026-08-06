class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
    

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



# Boyer–Moore majority vote algorithm
# Finding a Candidate: Initialize a candidate and a counter. Traverse the data, incrementing the counter for matching elements and decrementing for different ones. When the counter reaches zero, pick the current element as the new candidate.
# Verification: A second pass is required to verify if the candidate found in step one actually appears more than [n/2] times, confirming it as a true majority. 
# verification is not needed in this problem because the majority element is guaranteed to exist.
