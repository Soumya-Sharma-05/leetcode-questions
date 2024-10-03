class Solution(object):
    def isValid(self, s):
        stack = []
        # Dictionary to map closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                # Pop the top of the stack if there is one, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                # If the bracket doesn't match, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push open bracket to stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched properly
        return not stack
