class Solution(object):
    def kthDistinct(self, arr, k):
    
        count = {}
        for string in arr:
            if string in count:
                count[string] += 1
            else:
                count[string] = 1
    
    # Step 2: Collect distinct strings
        distinct_strings = []
        for string in arr:
            if count[string] == 1:
                distinct_strings.append(string)
    
    # Step 3: Return the k-th distinct string or an empty string
        if k <= len(distinct_strings):
            return distinct_strings[k-1]
        else:
            return ""
    
