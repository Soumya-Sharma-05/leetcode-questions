class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
    # Negative numbers are not palindromes
        if x < 0:
            return False
    
    # Create a reversed number
        original = x
        reversed_num = 0
    
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
    
    # Check if the original number is equal to the reversed number
        return original == reversed_num
