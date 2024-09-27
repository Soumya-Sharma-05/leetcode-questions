class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Trim leading whitespaces
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check if the next character is '+' or '-'
        sign = 1
        if i < n and s[i] in ['+', '-']:
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Read digits and form the number
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        # Step 4: Apply sign to the number
        result *= sign
        
        # Step 5: Handle overflow and underflow
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
