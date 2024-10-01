class Solution(object):
    def canArrange(self, arr, k):
        remainder_count = [0] * k  # Create a list to store the frequency of remainders
    
        # Count the remainders
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        # Check if we can pair the elements
        for i in range(k):
            if i == 0:
                # All numbers with remainder 0 should form pairs with each other
                if remainder_count[0] % 2 != 0:
                    return False
            elif i == k - i:
                # For cases like remainder k/2, the number of such remainders must be even
                if remainder_count[i] % 2 != 0:
                    return False
            else:
                # Check if remainder i can be paired with remainder k-i
                if remainder_count[i] != remainder_count[k - i]:
                    return False
        
        return True
