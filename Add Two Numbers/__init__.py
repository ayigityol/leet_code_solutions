# Leetcode question 2. Add Two Numbers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    pass


class Solution:
    overflow = 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_node = None

        if l1 is None and l2 is not None:
            value = l2.val + Solution.overflow
            Solution.overflow = int(value / 10)
            value = value % 10
            new_node = ListNode(value)
            new_node.next = self.addTwoNumbers(None, l2.next)

        elif l2 is None and l1 is not None:
            value = l1.val + Solution.overflow
            Solution.overflow = int(value / 10)
            value = value % 10
            new_node = ListNode(value)
            new_node.next = self.addTwoNumbers(l1.next, None)

        elif l1 is not None and l2 is not None:
            value = l1.val + l2.val + Solution.overflow
            Solution.overflow = int(value / 10)
            value = value % 10
            new_node = ListNode(value)
            new_node.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            if Solution.overflow == 0:
                return None
            else:
                new_node = ListNode(Solution.overflow)
                Solution.overflow = 0
                return new_node
        return new_node

import sys

if __name__ == "__main__":
    # Test Block
    l1 = ListNode(9)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(7)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    s = Solution()
    l3 = s.addTwoNumbers(l1, l2)
    node = l3
    while node is not None:
        sys.stdout.write(str(node.val))
        node = node.next
        if node is not None:
            sys.stdout.write(" -> ")

