class Solution(object):
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []
        
        result = []
        
        for i in range(0, len(original), n):
            result.append(original[i:i+n])
        
        return result
