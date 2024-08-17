class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

    # Create a frequency dictionary for characters in s
        char_count = {}

    # Count each character in s
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # Subtract the count for each character in t
        for char in t:
            if char in char_count:
                char_count[char] -= 1
            # If any character count goes below zero, it's not an anagram
                if char_count[char] < 0:
                    return False
            else:
            # If t contains a character not in s, it's not an anagram
                return False

    # If all character counts are zero, s and t are anagrams
        return True
