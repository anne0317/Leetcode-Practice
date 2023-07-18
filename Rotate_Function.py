class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sum=0
        F=0
        n=len(nums)
        for i in range(n):
            sum+=nums[i]
            F+=i*nums[i]
        max_val=F
        for i in range(n-1,0,-1):
            F+=sum - n * nums[i]
            max_val=max(F,max_val)
        return max_val
