from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        current = dummy

        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If there are remaining nodes in either list, append them
        current.next = list1 if list1 else list2

        # Return the merged list, which starts at dummy.next
        return dummy.next

# Test the function


def print_list(node: Optional[ListNode]):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


s = Solution()
result = s.mergeTwoLists(
    ListNode(1, ListNode(2, ListNode(4))),
    ListNode(1, ListNode(3, ListNode(4)))
)

print_list(result)
