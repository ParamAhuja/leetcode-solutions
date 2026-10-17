
## 5. Lazy Propagation: Range Updates in $O(\log n)$

Updating a whole range $[qL, qR]$ naively via point updates costs $O(K \log n)$, which degrades to $O(n \log n)$ when updating large ranges.

**Lazy propagation** delays updates until a subsegment must actually be queried or split:

1. Maintain a parallel array `lazy[]` initialized to 0.
2. When an update completely covers node $[L, R]$, update `tree[node]` immediately, mark `lazy[node]`, and return without recursing deeper.
3. Whenever visiting any node later, if it has a pending lazy tag, **push** that tag down to its two children before doing any split.

### Range Sum Value Adjustment Formula

When adding $\Delta$ to each element in $[L, R]$:


$$\Delta_{\text{total}} = (R - L + 1) \times \Delta$$

$$\text{tree}[\text{node}] \mathrel{+}= (R - L + 1) \times \Delta$$

### Full Lazy Implementation (Range Add + Range Sum)

```python

class LazySegmentTree:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, node=1, l=0, r=self.n - 1)

    def _build(self, arr: list[int], node: int, l: int, r: int) -> None:
        if l == r:
            self.tree[node] = arr[l]
            return
        
        mid = (l + r) // 2
        self._build(arr, 2 * node, l, mid)
        self._build(arr, 2 * node + 1, mid + 1, r)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _push(self, node: int, l: int, r: int) -> None:
        """Pushes pending deferred updates down to immediate children."""
        if self.lazy[node] == 0:
            return

        mid = (l + r) // 2
        left = 2 * node
        right = 2 * node + 1
        pending = self.lazy[node]

        # Apply to left child segment: length is (mid - l + 1)
        self.lazy[left] += pending
        self.tree[left] += (mid - l + 1) * pending

        # Apply to right child segment: length is (r - mid)
        self.lazy[right] += pending
        self.tree[right] += (r - mid) * pending

        # Clear parent's lazy tag
        self.lazy[node] = 0

    def update_range(self, ql: int, qr: int, delta: int) -> None:
        """Adds delta to all elements in range [ql..qr] in O(log n) time."""
        self._update_range(node=1, l=0, r=self.n - 1, ql=ql, qr=qr, delta=delta)

    def _update_range(self, node: int, l: int, r: int, ql: int, qr: int, delta: int) -> None:
        # Full overlap: update this node and mark lazy tag for children
        if ql <= l and r <= qr:
            self.tree[node] += (r - l + 1) * delta
            self.lazy[node] += delta
            return

        # Partial overlap: flush lazy state before recursing down
        self._push(node, l, r)
        mid = (l + r) // 2

        if ql <= mid:
            self._update_range(2 * node, l, mid, ql, qr, delta)
        if qr > mid:
            self._update_range(2 * node + 1, mid + 1, r, ql, qr, delta)

        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query_range(self, ql: int, qr: int) -> int:
        """Returns sum in range [ql..qr] in O(log n) time."""
        return self._query_range(node=1, l=0, r=self.n - 1, ql=ql, qr=qr)

    def _query_range(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if qr < l or ql > r:
            return 0

        if ql <= l and r <= qr:
            return self.tree[node]

        # Partial overlap: flush lazy state before reading children
        self._push(node, l, r)
        mid = (l + r) // 2

        return (
            self._query_range(2 * node, l, mid, ql, qr) +
            self._query_range(2 * node + 1, mid + 1, r, ql, qr)
        )


# --- Verification ---
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    lazy_st = LazySegmentTree(arr)

    # Add +5 to every index from 1 to 3:
    # Array effectively becomes: [1, 3+5, 5+5, 7+5, 9, 11] = [1, 8, 10, 12, 9, 11]
    lazy_st.update_range(ql=1, qr=3, delta=5)

    # Query range [0, 2] -> 1 + 8 + 10 = 19
    print("Query [0, 2]:", lazy_st.query_range(0, 2))  # Expected: 19

    # Query range [2, 5] -> 10 + 12 + 9 + 11 = 42
    print("Query [2, 5]:", lazy_st.query_range(2, 5))  # Expected: 42
```