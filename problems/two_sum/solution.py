class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_length = len(nums)
        memo = {}
        for i in range(nums_length):
            complement = target - nums[i]
            if complement in memo.keys():
                return (i, memo[complement])
            memo[nums[i]] = i
        
        # slow AF
        #nums_length = len(nums)
        #for i in range(nums_length):
        #    for j in range(i+1, nums_length):
        #        if nums[i] + nums[j] == target:
        #            return (i, j)