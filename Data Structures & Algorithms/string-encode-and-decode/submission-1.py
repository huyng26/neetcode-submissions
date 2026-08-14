class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#": #traverse until find limiter
                j += 1
            length = int(s[i: j]) #extract the length of the word
            i = j+1
            j = i + length
            res.append(s[i: j]) #extract the word based on the length
            i = j
        return res

            