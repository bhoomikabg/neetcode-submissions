class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li=[0,0]
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    li[0]=i
                    li[1]=j
                    break
        return li            