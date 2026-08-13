# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
linked list
method 1: simply add all nodes to arr and access middle

method 2: 2 pointer, slow and fast method
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # method 1:
        # arr = [head]
        # count = 0
        # while (head.next!=None):
        #     head = head.next
        #     arr.append(head)
        #     count+=1
        
        # return arr[ceil(count/2)]


        slow = head
        fast = head
        count = 1
        while (fast.next):
            fast = fast.next
            count+=1
            if count%2==0:
                slow = slow.next

        return slow