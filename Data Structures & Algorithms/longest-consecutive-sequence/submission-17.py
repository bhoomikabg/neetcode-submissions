class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr,maxx=1,1
        if len(nums)==0:
            return 0        
        nums=sorted(set(nums))
        for i in range(0,len(nums)-1):
            if nums[i+1]==nums[i]+1:
                curr+=1
                maxx=max(curr,maxx)
            else:
                curr=1
        return maxx            