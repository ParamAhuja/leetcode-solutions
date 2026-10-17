Standard Segment Tree (Point Update + Range Sum)

```python
class SegmentTree:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        # Allocate 4 * n space for implicit heap-indexed tree
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, node=1, l=0, r=self.n - 1)

    def _build(self, arr: list[int], node: int, l: int, r: int) -> None:
        if l == r:
            self.tree[node] = arr[l]
            return
        
        mid = (l + r) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        self._build(arr, left_child, l, mid)
        self._build(arr, right_child, mid + 1, r)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, idx: int, val: int) -> None:
        """Sets arr[idx] = val in O(log n) time."""
        self._update(node=1, l=0, r=self.n - 1, idx=idx, val=val)

    def _update(self, node: int, l: int, r: int, idx: int, val: int) -> None:
        if l == r:
            self.tree[node] = val
            return

        mid = (l + r) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        if idx <= mid:
            self._update(left_child, l, mid, idx, val)
        else:
            self._update(right_child, mid + 1, r, idx, val)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, ql: int, qr: int) -> int:
        """Returns sum of elements in arr[ql..qr] in O(log n) time."""
        return self._query(node=1, l=0, r=self.n - 1, ql=ql, qr=qr)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        # Case 1: Complete disjoint (no overlap)
        if qr < l or ql > r:
            return 0

        # Case 2: Complete overlap
        if ql <= l and r <= qr:
            return self.tree[node]

        # Case 3: Partial overlap
        mid = (l + r) // 2
        left_sum = self._query(2 * node, l, mid, ql, qr)
        right_sum = self._query(2 * node + 1, mid + 1, r, ql, qr)
        return left_sum + right_sum


# --- Verification with our example array ---
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)

    # Query range [1, 4] -> 3 + 5 + 7 + 9 = 24
    print("Query [1, 4]:", st.query(1, 4))  # Expected: 24

    # Point update: change arr[2] from 5 to 10
    st.update(idx=2, val=10)

    # Query range [1, 4] again -> 3 + 10 + 7 + 9 = 29
    print("Query [1, 4] after updating arr[2] = 10:", st.query(1, 4))  # Expected: 29
```