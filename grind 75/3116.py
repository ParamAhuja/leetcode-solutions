"""
# hard problem, todo again, also look at Gosper's Hack


Array
Math
Binary Search
Bit Manipulation
Combinatorics
Number Theory
"""


"""
We need to find the kth smallest possible amount.
Instead of generating the amounts explicitly, we count how many distinct amounts are at most m.

ex: Take coins=[2,3,5] and m=30.
find all values that can me made upto m.
(all multiples of each coins upto m, but inclusion-exclusion to ensure uniue values.)
also we only need count of all values because we need to binary search in self.count(m), for smallest number such that count(m)>=k
logic: the answer (say x) is from a sorted array, consisting of mutiples of given coins. altough we can not binary search on it directly to find ans, we can find count(m) - number of unique values that can be made of all coins, hence when smallest value when count(m) >=k, m would the the ans
lower bound of m = smallest coin 
upper bound of m = smallest coin * k
"""
"""
subset = {
    1: [[2], [3]]
    2: [[2,3]]
}
lcms = {
    1: [2, 3]
    2: [6]
}
"""


class Solution:
    def combos(self, arr, curr_path, subsets):
        # backtracking to find subsets
        if len(arr) == 0:
            subsets[len(curr_path)].append(curr_path[:])
            return
        x = arr.pop(0)
        self.combos(arr, curr_path, subsets)
        curr_path.append(x)
        self.combos(arr, curr_path, subsets)
        curr_path.pop()
        arr.append(x)

        
    def count(self, coins, m, lcms):
        """
        use inclusion exclusion to find all UNIQUE mutiples of coins smaller or equal to m
        1. singles to find all mutiples (non-unique)
        2. subsets of 2 coins multiple subtracted, 3 add, 4 sub, ... all of them add/sub
        """
        ans = 0
        n = len(coins)
        for i in lcms:
            if i%2 != 0:
                factor = 1
            else:
                factor = -1
            a = lcms[i]
            for x in a:
                # find lcm of subset, then:
                ans += factor* (m//x)
        return ans

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # pre-calculate all possible subsets of coins, for count function
        subsets= defaultdict(list)
        self.combos(coins, [], subsets)
        subsets.pop(0) # non empty only
        # pre-calculate the lcms of those subsets for count function
        lcms = defaultdict(list)
        for i in subsets:
            for j in subsets[i]:
                lcms[i].append(lcm(*j))

        # binary search for the solution m such that count(m)>=k
        low = min(coins)
        high = min(coins) * k
        ans = 0
        while(low<=high):
            m = low+(high-low)//2
            if self.count(coins, m, lcms)>=k:
                ans = m
                high = m-1
            else:
                low = m+1
        return ans