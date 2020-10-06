class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # faster
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums
    
        # in place
        #for i in range(len(nums), 0, -1):
        #    nums[i-1] = sum(nums[:i])
        #return nums
    