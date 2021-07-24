# https://leetcode.com/problems/combination-sum/
# combination sum
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def recursion_combination_sum(inner_target: int) -> List[List[int]]:
        combinations = []

        for candidate in candidates:

            if inner_target == candidate:
                combinations.append([candidate])
                continue

            division_result = inner_target - candidate

            if division_result < 0:
                continue

            res = recursion_combination_sum(division_result)

            for r in res:
                r = sorted([candidate] + r)

                # 중복 확인
                if next((c for c in combinations if c == r), None):
                    continue

                combinations.append(r)

        return combinations

    return sorted(recursion_combination_sum(target))
