# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
from typing import List


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
