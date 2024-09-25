class Solution(object):
    def reverse(self, x):
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
    
        # Handle the sign of the integer
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        reversed_num = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow/underflow before updating the reversed_num
            if reversed_num > (MAX_INT - digit) // 10:
                return 0  # Overflow condition
            
            reversed_num = reversed_num * 10 + digit
        
        return sign * reversed_num
