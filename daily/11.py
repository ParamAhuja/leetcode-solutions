"""
two pointer, greedy
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2 pointers
        left = 0
        right = len(height)-1

        area = 0
        while(left<right):
            h = min(height[left], height[right])
            w = (right - left)
            area = max(area, h * w)

            # greedy update
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return area

