# Huffman coding
is a greedy algorithm that constructs an optimal (variable length) code for compressing a given string. The algorithm builds a binary tree based on the frequencies of the characters in the string, and each character’s codeword can be read by following a path from the root to the corresponding node. A move to the left corresponds to bit 0, and a move to the right corresponds to bit 1. 

Initially, each character of the string is represented by a node whose weight is the number of times the character occurs in the string. Then at each step two nodes with minimum weights are combined by creating a new node whose weight is the sum of the weights of the original nodes. The process continues until all nodes have been combined.

*NOTE:*
We require that no codeword is a prefix of another codeword. For example, it is not allowed that a code would contain both codewords 10 and 1011. The reason for this is that we want to be able to generate the original string from the compressed string. If a codeword could be a prefix of another codeword, this would not always be possible. For example, the following codes are not valid: 110 and 11.


**The Algorithm (Step-by-Step)**
- Count Frequencies: Calculate how often each character appears in the data.

- Initialize Min-Heap: Create a leaf node for each unique character and insert them into a priority queue (min-heap) sorted by frequency.

- Build the Tree: While there is more than one node in the queue:

    - Extract the two nodes with the lowest frequencies.

    - Create a new internal node with a frequency equal to the sum of the two nodes.

    - Make the first extracted node its left child (assign bit 0) and the second its right child (assign bit 1).

    - Insert this new node back into the min-heap.

- Finalize: The remaining node is the root of the Huffman Tree.

**Time Complexity: O(n.log n):** Extracting and inserting into a min-heap takes O(log n) time, and this is done for n nodes.

**Space Complexity: O(n)** to store the tree and the priority queue.

## code:
```python
import heapq
from collections import defaultdict

class node:
    def __init__(self, weight=0, value=None, l=None, r=None):
        self.weight = weight
        self.value = value
        self.l = l
        self.r = r
        
    def __lt__(self, other):
        # Needed for heapq to tie-break when two nodes have the exact same weight
        return self.weight < other.weight

class huffman:
    def __init__(self, string):
        # count weights
        hashmap = defaultdict(int)
        for i in string:
            hashmap[i] += 1
            
        # now heapify
        self.heap = []
        for i in hashmap:
            weight, name = hashmap[i], i
            nodeObj = node(weight, name)
            heapq.heappush(self.heap, (weight, nodeObj))
            
        # now make a tree
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)[1]
            node2 = heapq.heappop(self.heap)[1]
            
            # Create merged parent node
            nodeObj = node(node1.weight + node2.weight, node1.value + node2.value, node1, node2) 
            
            # Push the actual nodeObj into the heap, not just its string value
            heapq.heappush(self.heap, (nodeObj.weight, nodeObj))
            
        # Extract the final node object from the tuple, which represents the root
        self.head = heapq.heappop(self.heap)[1]
  
    def huffman_coding(self):
        coding = {}
        # Keep track of the node and the code built so far as a tuple
        stack = [(self.head, "")] 
        
        while stack:
            curr_node, code = stack.pop()
            
            # If it's a leaf node (no children), assign the accumulated code
            if curr_node.l is None and curr_node.r is None:
                coding[curr_node.value] = code
                
            if curr_node.l is not None:
                stack.append((curr_node.l, code + "0"))
            if curr_node.r is not None:
                stack.append((curr_node.r, code + "1"))
                
        return coding

string = "AABACDACA"
encoder = huffman(string)
coding = encoder.huffman_coding()

print("Codes Map:", coding)
print("Encoded Output:", end=" ")
for i in string:
    print(coding[i], end="")

# Output:
# Codes Map: {'A': '1', 'D': '011', 'B': '010', 'C': '00'}
# Encoded Output: 110101000111001
```