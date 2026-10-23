
class Solution:
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in pairs:
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0

