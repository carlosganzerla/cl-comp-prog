# Definition for singly-linked list.
from typing import List, Optional
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class NodeIter:

    """Iterator that counts upward forever."""

    def __init__(self, head):
        self.head = head
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current:
            val = self.current.val
            self.current = self.current.next
            return val

        raise StopIteration()



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        iterator = None
        for val in heapq.merge(*map(NodeIter, filter(lambda x: x, lists))):
            e = ListNode(val)
            if not head:
                head = e
            else:
                iterator.next = e

            iterator = e

        return head






