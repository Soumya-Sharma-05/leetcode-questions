class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        def common_prefix_length(str1, str2):
        # Find the length of the common prefix between two strings
            i = 0
            while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
                i += 1
            return i

        max_prefix_length = 0
        
        # Convert all elements of both arrays to strings
        arr1_str = list(map(str, arr1))
        arr2_str = list(map(str, arr2))
        
        # Check every pair from arr1 and arr2
        for str1 in arr1_str:
            for str2 in arr2_str:
                max_prefix_length = max(max_prefix_length, common_prefix_length(str1, str2))
        
        return max_prefix_length
