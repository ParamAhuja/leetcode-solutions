"""
METHOD 1: recursive 

working: 
- a `chosen` boolean list is maintained with n length (initially all false), which is used to choose one element at a time
- recursive calls are made, and if an element is already chosen, skip that and chose next one then call again
- base case is when all element are chosen, which is end of a path

time comp: O(n . n!)
space comp: O(n . n!)
"""
def find_permutations(a):
    permutations = []
    n= len(a)
    chosen = [False for i in range(n)]

    def permute(current_path):
        # base case: root node, when fully permuted
        if len(current_path) == n:
            permutations.append(current_path[:])
            # print(current_path)
            return

        # each element rotation
        for i in range(n):
            #skipping chosen elements
            if chosen[i]:
                continue
            # calling for rest of elements
            chosen[i] = True
            current_path.append(a[i])
            permute(current_path)
            #backtracking (remove element)
            current_path.pop()
            chosen[i] = False
    permute([])
    return permutations
    

a = [1,2]
print(find_permutations(a))


"""
PYTHON standard lib
"""

from itertools import permutations

a = [1, 2, 3]
all_perms = list(permutations(a))


"""
In-Place Swapping
Instead of using a chosen array and building current_path from scratch, you can generate permutations in-place by swapping the elements of the array itself.

same comp
"""

def find_permutations_swap(a):
    permutations = []
    
    def backtrack(first=0):
        if first == len(a):
            permutations.append(a[:])
            return
        for i in range(first, len(a)):
            # Swap current element into position
            a[first], a[i] = a[i], a[first]
            backtrack(first + 1)
            # Backtrack (restore original order)
            a[first], a[i] = a[i], a[first]

    backtrack()
    return permutations

"""HEAP'S algorithm:
(most-efficient)

It minimizes movement by fixing the N-th element and generating permutations for the remaining N-1 elements recursively, swapping strategically based on whether N is even or odd.

same comp, but with the smallest constant factor among recursive methods.
"""
def heap_permutation(a):
    permutations = []

    def generate(k, arr):
        if k == 1:
            permutations.append(arr[:])
            return

        generate(k - 1, arr)

        for i in range(k - 1):
            if k % 2 == 0:
                arr[i], arr[k - 1] = arr[k - 1], arr[i]
            else:
                arr[0], arr[k - 1] = arr[k - 1], arr[0]
            generate(k - 1, arr)

    generate(len(a), a[:])
    return permutations


"""
Lexicographical Order (Next Permutation Method)

How it works
- Find the largest index i such that a[i] < a[i + 1].
- Find the largest index j > i such that a[i] < a[j].
- Swap a[i] and a[j].
- Reverse the sub-array from i + 1 to the end.

same comp

Key Advantage: Iterative (no stack overflow risk for large logic) and automatically handles duplicate inputs without generating duplicates, other dont.
"""

def next_permutation(a):
    n = len(a)
    i = n - 2
    
    # Step 1: Find first decreasing element from right
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
        
    if i == -1:
        return False  # Fully sorted in descending order (last permutation)
        
    # Step 2: Find element larger than a[i] from right
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
        
    # Step 3: Swap them
    a[i], a[j] = a[j], a[i]
    
    # Step 4: Reverse suffix
    a[i + 1:] = reversed(a[i + 1:])
    return True

def find_permutations_lexicographical(a):
    a = sorted(a)
    permutations = [a[:]]
    
    while next_permutation(a):
        permutations.append(a[:])
        
    return permutations


