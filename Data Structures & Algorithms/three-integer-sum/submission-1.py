class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        use two pointers inside the first outer loop
        for i in range(N) -> set up index j, k = i+1, len(nums)- 1
        if nums[j] + nums[k] < -nums[i] -> increase index j
        eif nums[j]+ nums[k] > -nums[i] -> decrease index k?
        else: return the triplet [nums[i], nums[j]. nums[k]]
        optimal solution should be O(n^2)
        '''
        res= set()
        nums.sort()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k: 
                if nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return [list(x) for x in res]