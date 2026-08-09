class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = {}
        for string in strs:
            tmp = [0] * 26
            for char in string:
                tmp[ord(char) - ord("a")] += 1
            tmp = tuple(tmp)
            if tmp not in cnt:
                cnt[tmp] = []
            cnt[tmp].append(string)
        return [value for value in cnt.values()]