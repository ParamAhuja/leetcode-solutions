# 1. Complete Concept of Recursion
when a problem can be broken in sub problems which could be independent, like Divide n Conquer, or dependent subpoblems like DP.

It uses a stack to keep strack of function calls. - hence the calls can be imagined as dfs of a tree.


## The Two Pillars

1. **Base Case**: The "exit condition" that stops the recursion. Without it, the function calls itself infinitely until the call stack is exhausted.
2. **Recursive Case**: The logic where the function calls itself with a modified (usually smaller or simpler) version of the input.

## The Call Stack Behavior

When a function calls itself, the current execution is "paused," and a new **stack frame** is pushed onto the **Call Stack**. This frame stores the *local variables* and the return address. Once the base case is hit, the stack begins to "unwind," returning values back through the chain of paused functions.

### Note: the local variables can be returned or a global keyword can be used if updates are needed.
### Note: for mutable types, since call by reference is used, they are updated in place. but also make sure to use copy where needed in each call.

Every recursive function must have a proper base case to function correctly and avoid a `RecursionError` (Stack Overflow) which happens at 1000 calls in python in default. sys.setrecursionlimit() can be used to ovveride the limit
---

# Recursion patterns: -
## 2. Accumulator (Easier) vs. Top-Down Approaches

### Top-Down (Divide and Conquer)

This is the "classic" way to think about recursion. You define the solution for $n$ based on the solution for $n-1$. The calculation happens **after** the recursive call returns (during the unwinding phase).

* **Logic**: $f(n) = n + f(n-1)$
* **Example (Factorial)**: `return n * factorial(n-1)`

### Accumulator (Iterative-like Recursion)

This approach passes the "running total" or state as an extra argument (the **accumulator**) into the next call. This is often considered "easier" because it mimics how a `for` loop works. The calculation happens **before** the next recursive call.

* **Logic**: $f(n, \text{acc}) = f(n-1, \text{acc} + n)$
* **Example**:
```python
def sum_acc(n, acc=0):
    if n == 0:
        return acc # Base case returns the accumulated result
    return sum_acc(n - 1, acc + n)

```

---

## 3. Head Recursion vs. Tail Recursion

The distinction lies in **when** the function performs its primary logic relative to the recursive call.

### Head Recursion (Bottom-up).

The recursive call is made at the **beginning** of the function. The function's "work" is done **after** the recursive call returns. Hence, the tree generates first, then only the task is carried out when backtracking. 

Note: Used when bottom up(leaf to root) type task is needed, meaning the subtask will be done first.

* **Effect**: It processes data in the reverse order of the calls (Bottom-up).
* **Code Pattern**:
```python
def head_rec(n):
    if n == 0: return
    head_rec(n - 1) # Call first
    print(n)        # Work second (Prints 1, 2, 3...)

```



### Tail Recursion (Top-down).

The recursive call is the **last** operation in the function. No work is left to do after the call returns. 

Note: Used when root to leaf type task is needed, meaning the task keeps becoming smaller and smaller, first for n then n-1, etc.

* **Effect**: It processes data in the same order as the calls (Top-down).
* **Optimization**: Some languages (not standard CPython) can optimize tail recursion into a loop to save stack space (Tail Call Optimization).
* **Code Pattern**:
```python
def tail_rec(n):
    if n == 0: return
    print(n)        # Work first (Prints 3, 2, 1...)
    tail_rec(n - 1) # Call last

```


---

## 4. Recursion procedural vs functional

This highlights the difference between **returning a value** and **executing a side effect**.

### Recursion for a Task (Functional)

The goal is to compute and **return** a value. The result of one call is needed to calculate the result of the previous call.

* **Key Feature**: Uses the `return` keyword with the recursive call.
* **Example**: Calculating the sum of a list or a factorial.
```python
def task_sum(n):
    if n == 1: return 1
    return n + task_sum(n - 1) # Task: Computing a sum

```



### Recursion for Print (Procedural)

The goal is to perform an action (like printing or modifying a global variable) during each step of the recursion.

* **Key Feature**: Often returns `None` (implicit). The "result" is the output on the screen.
* **Example**: Traversing a folder structure or printing a sequence.
```python
def print_rec(n):
    if n == 0: return
    print(n)        # Side effect: Printing
    print_rec(n - 1)

```


### Comparison Summary

| Feature | Head Recursion | Tail Recursion |
| --- | --- | --- |
| **Logic Timing** | After the call (unwinding). | Before the call (winding). |
| **Stack Usage** | High (must wait for return). | High (in Python), but logically simple. |
| **Common Style** | Top-down / Task-based. | Accumulator / Iterative-style. |


## complexity of recursion:- 
Time Complexity: (total number of executions/operations across all recursive calls)

Space Complexity: (the maximum depth of the call stack required during execution).



### Time Complexity

The time complexity of a recursive function is generally calculated using the following rule of thumb:

\(\text{Total\ Time\ Complexity}=\text{Total\ Number\ of\ Recursive\ Calls}\times \text{Time\ Complexity\ Per\ Call}\)

To solve complex recursive algorithms mathematically, use the three primary methods to solve recurrence relations:

**The Master Method**: A mathematical formula providing instant bounds for divide-and-conquer recurrences in the form T(n) = aT(n/b) + f(n). see master_theorem.md
**The Recursion Tree Method**: A visual map charting out every breakdown of the input size to sum the work done across each tree level.
**The Substitution Method**: Making an educated guess of the complexity bound and confirming its validity using mathematical induction.


## Space complexity

Every time a function calls itself, runtime memory reserves space on the internal call stack to save local variables and execution paths. This introduces a memory overhead absent in iterative solutions.

\(\text{Total\ Space\ Complexity}=\text{Maximum\ Depth\ of\ the\ Recursion\ Tree}\times \text{Space\ Allocated\ Per\ Call}\)

Even if your code creates no arrays or lists, a recursion that drills down n levels deep still occupies O(n) space purely due to stack allocation.

*For example*:- for a problem that gets broken into two subproblems of n/2 each, max depth would be (logn)
*For example*:- for a problem that gets broken into a subproblems of n-1 , max depth would be (n)


## Common Complexity Examples


| Algorithm | Recurrence Relation | Time Complexity | Space Complexity | Why? |
| --- | --- | --- | --- | --- |
| **Linear Search / Factorial** | $T(n) = T(n-1) + O(1)$ | $O(n)$ | $O(n)$ | Linear reduction of input size; builds a single-branch call stack. |
| **Binary Search** | $T(n) = T(n/2) + O(1)$ | $O(\log n)$ | $O(\log n)$ | Divides problem size by 2 at each step but only explores one path. |
| **Merge Sort** | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ | $O(n)$ | Splits into two branches ($\log n$ depth) and executes $n$ work to merge. |
| **Fibonacci (Naive)** | $T(n) = T(n-1) + T(n-2)$ | $O(2^n)$ | $O(n)$ | Exponentially explodes into a massive tree, but depth only scales linearly. |