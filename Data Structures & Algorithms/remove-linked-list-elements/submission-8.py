# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        prev = ListNode()
        prev.next = head

        def helper(node,val):
            if node is None or node.next is None:
                return 
            else:
                while node.next and node.next.val == val:
                    node.next = node.next.next
                helper(node.next, val)

        
        helper(prev,val)

        return prev.next