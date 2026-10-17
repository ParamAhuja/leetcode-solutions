## What is Bit Masking?

**Bit masking** is a technique used to manipulate, query, or set specific bits within an integer using **bitwise operators**.

An integer in a computer is stored as a sequence of bits (0s and 1s). A **"bit mask"** is simply another binary number used to "mask out" or target specific bits of that integer while leaving others alone.

---

## The Core Bitwise Operators

To understand bit masking, you need to know four fundamental operators:

* **AND (`&`)**: Returns `1` only if **both** bits are `1`. Used to **check/extract** if a bit is set.
* **OR (`|`)**: Returns `1` if **at least one** bit is `1`. Used to **turn a bit ON** (set to 1).
* **XOR (`^`)**: Returns `1` if the bits are **different**. Used to **toggle** a bit (flip 0 to 1, or 1 to 0).
* **Left Shift (`<<`)**: Shifts bits to the left, effectively multiplying by powers of 2. Used to **create masks** (e.g., `1 << i` creates a mask with the $i$-th bit turned on).

---

## Common Operations & Examples

Imagine a byte of data where we count bits from right to left, starting at index 0 (e.g., binary `00001010`).

### 1. Check if the $i$-th bit is ON (Get Bit)

To see if a specific bit is `1` or `0`, use the **AND** operator with a mask where only that bit is `1`.

* **Mask:** `1 << i`
* **Formula:** `number & (1 << i)`
* **Example:** Check if the 3rd bit of `10` (binary `1010`) is set.
* Mask for index 3: `1 << 3` $\rightarrow$ `1000`
* `1010 & 1000` $\rightarrow$ `1000` (non-zero, meaning the bit is **ON**).



### 2. Turn the $i$-th bit ON (Set Bit)

To force a specific bit to `1` without changing the others, use the **OR** operator.

* **Mask:** `1 << i`
* **Formula:** `number | (1 << i)`
* **Example:** Turn on the 2nd bit of `8` (binary `1000`).
* Mask for index 2: `1 << 2` $\rightarrow$ `0100`
* `1000 | 0100` $\rightarrow$ `1100` (which is `12`).



### 3. Turn the $i$-th bit OFF (Clear Bit)

To force a specific bit to `0`, use **AND** with the **inverse** (`~`) of the mask.

* **Mask:** `~(1 << i)`
* **Formula:** `number & ~(1 << i)`
* **Example:** Turn off the 3rd bit of `10` (binary `1010`).
* Mask: `~(1 << 3)` $\rightarrow$ `~1000` $\rightarrow$ `0111`
* `1010 & 0111` $\rightarrow$ `0010` (which is `2`).



### 4. Toggle the $i$-th bit (Flip Bit)

To flip a bit from `0` to `1` or `1` to `0`, use the **XOR** operator.

* **Mask:** `1 << i`
* **Formula:** `number ^ (1 << i)`

---

## Why Use Bit Masking?

1. **Extreme Efficiency:** Computers process bits natively at the hardware level. Bitwise operations execute in a single CPU cycle, making them blazing fast.
2. **Memory Optimization:** Instead of storing an array of booleans (`[True, False, True, False]`), you can represent an entire set of up to 32 or 64 flags inside a single integer.
3. **Dynamic Programming & Backtracking:** In problems like the Traveling Salesperson or generating all subsets, bit masks represent "which elements have been visited or included" compactly, making state memoization easy (often used in LeetCode bitmask DP problems).
