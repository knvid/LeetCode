class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
    
        return -1