# do again

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # Observation 1: We need to go down from n**2 to anything, by fixing the redundant operations of calculating each subarray from start to end and not using the overlapping section. 
        # Solution: we need to fix the start or end (lets fix end because convention). Loop through nums, and at iteration i, store the new subarrays (the number of distinct elements of all the subarrays ending at index (i)), in an array (arr).
        # hence, the array is an n length array, which updates at every iteration, to now track subarrays ending in index i.
        # example: nums = [1,2,1]
        # at i = 0: [1, 0, 0] - single subarray [1]
        # at i = 1: [2, 1, 0] - subarray [1,2] and [2]
        # at i = 2: [2, 2, 1] - subarray [1, 2, 1] and [1,2] and [2]
        # it does so by adding 1 to all elements in the range: from last occurance of nums[i] to index i.

        # Observation 2: we need to do a lot of range updates as well as range queries (for sum of square) on this array arr.
        # solution: hence build a segment tree on this array. 
        # also, for the range query, we can simply take the root element's value of segment tree after updation

        # observation 3: we need to track the last occurance, hence keep a hashmap.

        # observation 4: lazy propagation in segment tree. because we dont need sum of counts, but sum of SQUARE.

        # observation 5: modulo is needed for large numbers.
