# https://leetcode.com/problems/valid-parentheses/
def valid_parentheses(s: str) -> bool:
    open_stack = []

    for p in s:
        if p in '([{':
            open_stack.append(p)
            continue

        if len(open_stack) == 0:
            return False

        if {')': '(', ']': '[', '}': '{'}[p] != open_stack.pop():
            return False

    return True if len(open_stack) == 0 else False
