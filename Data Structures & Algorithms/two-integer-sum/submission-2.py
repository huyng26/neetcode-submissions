class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        res = []
        for idx, num in enumerate(nums):
            if target - num in mp:
                res = [mp[target-num], idx]
            mp[num] = idx
        return res