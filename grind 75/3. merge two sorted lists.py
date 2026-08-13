"""auxillary linked list used
# todo - without aux
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        ans = ListNode()
        temp = ans
        while(p1!=None and p2!=None):
            if p1.val > p2.val:
                temp.next = p2
                p2 = p2.next
            else:
                temp.next = p1
                p1 = p1.next
            temp = temp.next
        if p2!=None:
            temp.next = p2
        elif p1!=None:
            temp.next = p1
        return ans.next