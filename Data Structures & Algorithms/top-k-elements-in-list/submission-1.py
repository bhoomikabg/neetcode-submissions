from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        c=Counter(nums)
        c=sorted(c.items(),key=lambda x: x[1], reverse=True)
        return [num for num,count in c[:k]]
        