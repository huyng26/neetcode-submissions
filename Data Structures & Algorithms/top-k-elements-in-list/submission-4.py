class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # sort dicts based on values
        count = list(sorted(count.keys(), key= lambda item: count[item], reverse=True))
        return count[:k]