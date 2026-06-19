class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell=0,1
        mprof=0
        while sell!=len(prices):
            if prices[buy]<prices[sell]:
                prof=prices[sell]-prices[buy]
                mprof=max(mprof,prof)
            else:
                buy=sell
            sell+=1
        return mprof            
