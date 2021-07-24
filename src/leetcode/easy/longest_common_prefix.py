from typing import List


# https://leetcode.com/problems/longest-common-prefix/
# Longest Common Prefix

def longest_common_prefix(strings: List[str]) -> str:
    prefix_target_str = min(strings)

    for i in range(len(prefix_target_str), 0, -1):
        prefix = prefix_target_str[0:i]

        if len([s for s in strings if s.startswith(prefix)]) == len(strings):
            return prefix

    return ''
