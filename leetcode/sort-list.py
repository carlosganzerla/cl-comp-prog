# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def toList(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

def swap(e1, e2):
    temp = e1.val
    e1.val = e2.val
    e2.val = temp

def partition(head, last):
    first_high = head
    first_high_prev = head
    iterator = head
    while iterator != last:
        if last.val > iterator.val:
            swap(iterator, first_high)
            first_high_prev = first_high
            first_high = first_high.next

        iterator = iterator.next
    swap(first_high, last)
    first_high_next = last if first_high == last else first_high.next
    return (head, first_high_prev), (first_high_next, last)

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def loop(low, high):
            if low != high:
                left, right = partition(low, high)
                loop(*left)
                loop(*right)
        if not head:
            return None
        last = head
        while last.next:
            last = last.next
        loop(head, last)
        return head
