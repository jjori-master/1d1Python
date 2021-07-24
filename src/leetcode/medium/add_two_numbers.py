# noinspection PyShadowingBuiltins
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/add-two-numbers/
def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    list_n1 = []
    list_n2 = []

    while l1 or l2:
        n1 = 0 if not l1 else l1.val
        n2 = 0 if not l2 else l2.val

        list_n1.insert(0, str(n1))
        list_n2.insert(0, str(n2))

        l1 = None if not l1 else l1.next
        l2 = None if not l2 else l2.next

    sum_value = str(int(''.join(list_n1)) + int(''.join(list_n2)))

    return_node = None

    for n in [int(x) for x in str(sum_value)]:
        return_node = ListNode(val=int(n), next=return_node)

    return return_node
