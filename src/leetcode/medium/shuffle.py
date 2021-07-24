from typing import List


# https://leetcode.com/problems/shuffle-the-array/
# 1470. Shuffle the Array

def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    for i in range(0, n):
        res.append(nums[i])
        res.append(nums[i + n])
    return res
