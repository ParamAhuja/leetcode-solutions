Let q(n) denote the number of ways to place n queens on an n× n chessboard.
The above backtracking algorithm tells us that, for example, q(8) = 92. When
n increases, the search quickly becomes slow, because the number of solutions
increases exponentially. For example, calculating q(16) = 14772512 using the
above algorithm already takes about a minute on a modern computer1


## Python Implementation

```python
def solve_n_queens(n):
    solutions = []
    
    # State tracking
    cols = set()         # Columns where queens are placed
    pos_diag = set()     # Positive diagonals (row + col)
    neg_diag = set()     # Negative diagonals (row - col)
    
    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        # Base case: All queens placed
        if row == n:
            board_copy = ["".join(r) for r in board]
            solutions.append(board_copy)
            return

        for col in range(n):
            # Check if current position is under attack
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            # Place queen
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            board[row][col] = "Q"

            # Recurse to next row
            backtrack(row + 1)

            # Backtrack (remove queen)
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            board[row][col] = "."

    backtrack(0)
    return solutions


n = 4
results = solve_n_queens(n)

print(f"Found {len(results)} solutions for N = {n}:\n")
for idx, solution in enumerate(results, 1):
    print(f"Solution {idx}:")
    for row in solution:
        print(row)
    print()

```


## How It Works

### 1. Diagonal Math Trick

Checking if a queen threatens another across diagonals in $\mathcal{O}(1)$ time is the core optimization here:

* **Positive Diagonal ($/$)**: Every cell on the same bottom-left to top-right diagonal shares the same sum of `row + col`.
* **Negative Diagonal ($\backslash$)**: Every cell on the same top-left to bottom-right diagonal shares the same difference of `row - col`.

### 2. Backtracking Logic

* **Row-by-Row Placement:** Since each row must contain exactly one queen, we process row by row (`row = 0, 1, ..., n-1`). This automatically avoids row collisions.
* **Pruning Invalid Paths:** Before placing a queen at `(row, col)`, we check if `col`, `row + col`, or `row - col` exist in our sets. If yes, that path is pruned early.
* **Backtrack Step:** After exploring `row + 1`, we remove the queen and reset the state sets to test the remaining columns in the current row.


## Complexity Breakdown

| Metric | Complexity | Explanation |
| --- | --- | --- |
| **Time Complexity** | $\mathcal{O}(N!)$ | For row 0, there are $N$ options; for row 1, at most $N-2$; and so on. |
| **Auxiliary Space** | $\mathcal{O}(N)$ | The recursion stack goes $N$ levels deep, and tracking sets hold at most $N$ elements. |
| **Total Space** | $\mathcal{O}(N \cdot S)$ | Memory to store all $S$ valid board arrangements, where $S$ is the total number of solutions. |


# PRUNING: common optimization in backtracking

We can often optimize backtracking by pruning the search tree. The idea is to
add ”intelligence” to the algorithm so that it will notice as soon as possible if a
partial solution cannot be extended to a complete solution. Such optimizations
can have a tremendous effect on the efficiency of the search


# Meet in the middle
Meet in the middle is a technique where the search space is divided into two parts of about equal size. A separate search is performed for both of the parts, and finally the results of the searches are combined.
The technique can be used if there is an efficient way to combine the results of the searches. In such a situation, the two searches may require less time than one large search. Typically, we can turn a factor of (n.2^n) into a factor of (n . 2^(n/2)) using the meet in the middle technique.


As an example, consider a problem where we are given a list of n numbers
and a number x, and we want to find out if it is possible to choose some numbers from the list so that their sum is x. For example, given the list [2,4,5,9] and x = 15, we can choose the numbers [2,4,9] to get 2+4+9 = 15. However, if x = 10 for the same list, it is not possible to form the sum.


A simple algorithm to the problem is to go through all subsets of the elements and check if the sum of any of the subsets is x. The running time of such an algorithm is O(2n), because there are 2^n subsets. However, using the meet in the middle technique, we can achieve a more efficient O(2n/2) time algorithm. Note that O(2n) and O(2n/2) are different complexities.


The idea is to divide the list into two lists A and B such that both lists contain about half of the numbers. The first search generates all subsets of A and stores their sums to a list SA. Correspondingly, the second search creates a list SB from B. After this, it suffices to check if it is possible to choose one element from SA and another element from SB such that their sum is x. This is possible exactly when there is a way to form the sum x using the numbers of the original list.


For example, suppose that the list is [2,4,5,9] and x = 15. First, we divide the list into A = [2,4] and B = [5,9]. After this, we create lists SA = [0,2,4,6] and SB = [0,5,9,14]. In this case, the sum x = 15 is possible to form, because SA contains the sum 6, SB contains the sum 9, and 6+9 = 15. This corresponds to the solution [2,4,9].


We can implement the algorithm so that its time complexity is O(2n/2). First,we generate the sorted lists SA and SB, which can be done in O(2n/2) time using a merge-like technique. After this, since the lists are sorted, we can check in O(2n/2) time if the sum x can be created from SA and SB.
Note that we use the sorted property of sa and sb to use 2 pointer, since length of sa and sb is 2^(n/2), time complexity if O(2^(n/2))
hence, total is O(2^n/2 + 2^n/2) => O(2.2^(n/2)) => O(2^(n/2))
whereas using loops to check each pair would have been O(2^(n/2) ^2)
hence, total would be O(2^n)