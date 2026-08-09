"""
- create a array to store the frequency of both words(size=26)
- 
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = 26 * [0]
        count_t = 26 * [0]
        for char in s: 
            count_s[ord(char) - ord("a")] += 1
        for char in t: 
            count_t[ord(char) - ord("a")] += 1
        return True if count_s == count_t else False