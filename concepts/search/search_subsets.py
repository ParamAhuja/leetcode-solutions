"""
Subset: Any selection of elements; order does not matter, and elements do not need to be next to each other.

Subarray: A contiguous (unbroken) part of an array. In [1, 2, 3], [2, 3] is a subarray, but [1, 3] is not.

Subsequence: A sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements (same as a subset, but order matters).
"""

"""
all possible subsets: 2^n

time comp: O(n.2**n)
space comp: O(n)
"""

"""
METHOD 1: Recursive tree: 

Time Complexity: O(n * 2n), generating all subsets requires 2n recursive calls, and copying each subset of size up to n takes O(n) time.
Auxiliary Space: O(n), recursion stack and temporary subset use at most n space at a time.


"""
def search_subsets(a):
    n = len(a)
    subsets = []
    # func in func to use global instead of nonlocal 
    def dfs(k, current_path):
        # base case after root node
        if k == n:
            subsets.append(current_path[:]) # IMPORTANT to copy and not directly append
            return 
        
        # left subtree
        dfs(k+1,current_path )
        # right subtree
        current_path.append(a[k])
        dfs(k+1,current_path )
        # backtrack to parent node (remove element)
        current_path.pop()
    dfs(0,[])
    return subsets
a=[1,2]
print(search_subsets(a))


"""
METHOD 2: bit masking
take a decimal number (mask) from 0 to 2**(n-1) and loop on its binary rep (length n) hence O(n. 2**n)

Time Complexity: O(n * 2n), generating all subsets requires 2n recursive calls, and copying each subset of size up to n takes O(n) time.
Auxiliary Space: O(n), temporary subset at most n space at a time.


"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for mask in range(2**n): # or 1<<n does the same thing
            subset = []
            # apply masking and append
            for i in range(n):
                if (mask & (1<<i)):
                    subset.append(nums[i])
            ans.append(subset[:])
        return ans

