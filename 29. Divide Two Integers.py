class Solution(object):
    def divide(self, dividend, divisor):
        # Constants for the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle special case of overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # Overflow case
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Use absolute values for calculation
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        
        # Subtract divisor from dividend using bit shifts for efficiency
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        
        # Apply the sign to the result
        if negative:
            quotient = -quotient
        
        # Clamp the result to the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))
