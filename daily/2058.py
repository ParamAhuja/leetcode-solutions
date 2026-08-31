"""
linked list, greedy
Find the Minimum and Maximum Number of Nodes Between Critical Points
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDist = math.inf
        prevCritical = None
        firstCritical = None
        i = 0
        while(head.next.next!=None):
            prev = head
            head = head.next
            forw = head.next
            i+=1
            # always has a prev and next
            if (prev.val < head.val and head.val > forw.val) or (prev.val > head.val and head.val < forw.val):
                # print("critical at index: ", i)
                if prevCritical!=None:
                    dist = i - prevCritical
                    minDist = min(minDist, dist)
                else:
                    firstCritical = i
                prevCritical = i
            

        ans = [-1, -1]
        if minDist!=math.inf:
            ans[0] = minDist
        if firstCritical!=prevCritical and prevCritical!=None and firstCritical!=None:
            maxDist = prevCritical - firstCritical
            ans[1]=maxDist
        return ans