# binary search

uses the sorted property of a collection to "search"

## when to use:
used in sorted structures with some monotonic (strictly increasing or decreasing) pattern with large constraints

## conditions: 
- sorted
- 0(1) access time using index

## complexity:
O(logN)

## overflow case:
- overflow of integer could be there when `mid = (low+high)//2` is done on big integers
- `low+ (high-low)//2` is used because we want to avoid.

## EXTRA:
- Some problems can be solved by binary searching on the answer and verifying feasibility using greedy or dynamic programming.
- Examples:
 -- Minimize maximum subarray sum (Greedy)
 -- Aggressive Cows (check with greedy)
 -- Allocate books problem
 -- Longest segment with some property (use prefix sums + BS)
 -- source: https://codeforces.com/blog/entry/144848

- NOTE: a temp variable can be taken in this for problems such as:
-- upper bound, lower bound
-- floor, ceil

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) -1
        low = 0

        while low<=high:
            mid = low+(high-low)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
        
        return -1
```
## BOUNDS:

```python
## LOWER BOUND: first index >= x

low = 0
high = len(nums)-1
ans = len(nums) # return n if x is larger than all elements in array
while(high>=low):
    mid = low+ (high-low)//2
    if nums[mid]>=target: # update answer if a number greater or equal to x is found
        ans = mid
        high = mid-1
    else:
        low=mid+1
return ans



## UPPER BOUND: first index > x

low = 0
high = len(nums)-1
ans = len(nums) # return n if x is larger than all elements in array or IS the largest element in array
while(high>=low):
    mid = low+ (high-low)//2
    if nums[mid]>target: # only difference than lower bound is the operator used
        ans = mid
        high = mid-1
    else:
        low=mid+1
return ans



## FLOOR: largest number smaller than equal to x
low = 0
high = len(nums)-1
ans = -1 # return -1 if x is smaller than all elements in the array.
while(high>=low):
    mid = low+ (high-low)//2
    if nums[mid]<=target:
        ans = mid
        low=mid+1
    else:
        high = mid-1
return ans

## CEIL: smallest number greater than or equal to x

## SAME AS LOWER BOUND:

low = 0
high = len(nums)-1
ans = -1 # return n if x is larger than all elements in the array.
while(high>=low):
    mid = low+ (high-low)//2
    if nums[mid]>=target: # make it > if equals not to be considered
        ans = mid
        high = mid-1
    else:
        low=mid+1
return ans

```