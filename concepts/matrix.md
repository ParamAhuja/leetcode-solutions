## 1. Fundamentals & Traversals

Mastering indexing, boundaries, and standard iteration patterns.

* **2D Array Representation & Storage**
* Row-major vs. Column-major memory layout
* Dynamic 2D vector/array allocation and indexing rules


* **Standard Traversals**
* Row-wise & Column-wise iteration
* Diagonal Traversals (Main diagonal, Anti-diagonal, arbitrary diagonals)
* Spiral Matrix Traversal (Iterative boundary shrinkage)
* Zig-Zag / Wave Traversal



---

## 2. In-Place Transformations & Geometry

Manipulating matrix elements without allocating significant extra space ($O(1)$ auxiliary space).

* **Matrix Transposition**
* In-place swapping for square matrices ($N \times N$)


* **Rotations & Reflections**
* Rotate image by $90^\circ$ clockwise/counter-clockwise (Transpose + Reverse)
* Horizontal and Vertical flipping


* **Set Matrix Zeroes Pattern**
* Using first row and first column as state markers to achieve $O(1)$ space complexity



---

## 3. Search Operations

Leveraging structural properties (like sorted rows/columns) to optimize searches.

* **Searching in Matrix**
* Unsorted Matrix ($O(M \times N)$ linear scan)
* Fully Sorted Matrix (Binary Search treating 2D array as 1D array)
* Row-wise & Column-wise Sorted Matrix (Staircase Search algorithm starting from top-right or bottom-left corner)



---

## 4. Matrix Mathematics & Games

Arithmetic and game logic on grid formats.

* **Matrix Multiplication**
* Standard $O(N^3)$ multiplication logic
* Strassen's Algorithm concept (Divide & Conquer)


* **Game of Life & State Simulation**
* In-place state transitions using bit manipulation or temporary markers
* In-place boundary padding



---

## 5. Grid Graph Algorithms (BFS & DFS)

Treating a 2D matrix as an implicit graph where each cell $(i, j)$ is a node with up to 4 or 8 edges.

* **Grid Connected Components**
* Flood Fill Algorithm
* Number of Islands (DFS / BFS)
* Max Area of Island


* **Shortest Path in Grids**
* BFS on unweighted grids (Shortest Path in Binary Matrix, Rotting Oranges)
* Multi-Source BFS


* **Cycle Detection & Union-Find on Grid**
* Mapping 2D coordinates `(r, c)` to 1D ID `r * cols + c` for Disjoint Set Union (DSU)



---

## 6. Dynamic Programming on Grids

Solving optimization problems by defining 2D subproblems $DP[i][j]$.

* **Path Counting & Optimization**
* Unique Paths (Standard grid movement down/right)
* Minimum Path Sum
* Dungeon Game / Cherry Pickup (2-pass DP)


* **Submatrices & Geometry DP**
* Maximal Square / Maximal Rectangle
* Count Square Submatrices with All Ones
* 2D Prefix Sums (Range Sum Query 2D)



---

## 7. Advanced Matrix Patterns

Specialized topics for high-level technical interviews.

* **Monotonic Stack on Matrices**
* Maximal Rectangle using Largest Rectangle in Histogram as a sub-problem


* **Binary Lifting / Divide and Conquer on Grids**
* Toeplitz Matrix verification
* K-th Smallest Element in a Sorted Matrix (Binary search on value space or Min-Heap)