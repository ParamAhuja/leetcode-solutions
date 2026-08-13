# Master Theorem Notes

The Master Theorem provides a fast mathematical recipe to determine the Big-O time complexity of divide-and-conquer recursive algorithms. It solves recurrence relations that take the generic form:

$$T(n) = aT\left(\frac{n}{b}\right) + f(n)$$

* $a \ge 1$: Number of recursive subproblems.
* $b > 1$: Factor by which the problem size is divided.
* $f(n)$: Work done outside recursive calls (splitting or merging).

---

## 1. Core Term: Critical Exponent

Extract $a$, $b$, and $f(n)$, then calculate the critical value:

$$\text{Critical Value} = n^{\log_b a}$$

This critical value represents the total computational work generated purely by the leaves of the recursion tree.

---

## 2. Summary of Cases

Compare the non-recursive work $f(n)$ to the leaf work $n^{\log_b a}$:

| Case | Condition | Intuition / Meaning | Result $T(n)$ |
| --- | --- | --- | --- |
| **Case 1** | $f(n) = O\left(n^{\log_b a - \epsilon}\right)$ for $\epsilon > 0$ | **Recursive Leaves Dominate.** Branches grow polynomially faster than non-recursive work. | $\Theta\left(n^{\log_b a}\right)$ |
| **Case 2** | $f(n) = \Theta\left(n^{\log_b a} \log^k n\right)$ for $k \ge 0$ | **Work is Evenly Balanced.** Work at each level of the tree is asymptotically equal. | $\Theta\left(n^{\log_b a} \log^{k+1} n\right)$ <br>

<br>*(When $k=0$, it is $\Theta(n^{\log_b a} \log n)$)* |
| **Case 3** | $f(n) = \Omega\left(n^{\log_b a + \epsilon}\right)$ for $\epsilon > 0$ <br>

<br>**AND** $a f(n/b) \le c f(n)$ for $c < 1$ | **Non-Recursive Work Dominates.** Merging/dividing work at the root dominates execution. | $\Theta(f(n))$ |

---

## 3. Worked Examples

### Summary Comparison Table

| Example Algorithm / Recurrence | $a, b, f(n)$ | Critical Value $n^{\log_b a}$ | Matching Case | Time Complexity $T(n)$ |
| --- | --- | --- | --- | --- |
| **Merge Sort** <br>

<br> $T(n) = 2T(n/2) + n$ | $a=2, b=2, f(n)=n$ | $n^{\log_2 2} = n^1 = n$ | **Case 2** ($k=0$) | $\Theta(n \log n)$ |
| **Binary Search** <br>

<br> $T(n) = T(n/2) + O(1)$ | $a=1, b=2, f(n)=O(1)$ | $n^{\log_2 1} = n^0 = 1$ | **Case 2** ($k=0$) | $\Theta(\log n)$ |
| **Strassen's Matrix Mult.** <br>

<br> $T(n) = 7T(n/2) + O(n^2)$ | $a=7, b=2, f(n)=O(n^2)$ | $n^{\log_2 7} \approx n^{2.81}$ | **Case 1** | $\Theta\left(n^{\log_2 7}\right) \approx \Theta(n^{2.81})$ |

### Step-by-Step Breakdown (Merge Sort)

1. **Identify terms:** $a = 2$, $b = 2$, $f(n) = n$.
2. **Compute critical value:** $n^{\log_2 2} = n^1 = n$.
3. **Compare:** $f(n) = n$ and $n^{\log_b a} = n$ are identical.
4. **Select case:** Case 2 with $k = 0$.
5. **Final Result:** $T(n) = \Theta(n \log n)$.

---

## 4. Strict Limitations

The Master Theorem **cannot** be applied directly if:

1. $a$ is not a constant (e.g., $T(n) = n T(n/2)$).
2. $b \le 1$ or changes dynamically.
3. $f(n)$ is non-polynomial (e.g., $T(n) = 2T(n/2) + 2^n$).
4. The gap between $f(n)$ and $n^{\log_b a}$ is not polynomial (e.g., $T(n) = 2T(n/2) + n \log n$).