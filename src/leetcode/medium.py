# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
from typing import List


# noinspection PyShadowingBuiltins
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def min_partitions(n: str) -> int:
    return int(max(n))


# https://leetcode.com/problems/shuffle-the-array/
# 1470. Shuffle the Array

def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    for i in range(0, n):
        res.append(nums[i])
        res.append(nums[i + n])
    return res


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
