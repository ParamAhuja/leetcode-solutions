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
METHOD 2: bit manipulation

Time Complexity: O(n * 2n), generating all subsets requires 2n recursive calls, and copying each subset of size up to n takes O(n) time.
Auxiliary Space: O(n), temporary subset at most n space at a time.


"""

def find_subsets(a):
    subsets = []
    n = len(a)
    for i in range(1<<n): # or range(2**n) to go from 0 to 2**n-1
        subset = []
        for j in range(n):
            if i&(1<<j):
                subset.append( a[j] )
        subsets.append(subset)
    return subsets

a = [1,2]
print(find_subsets(a))

