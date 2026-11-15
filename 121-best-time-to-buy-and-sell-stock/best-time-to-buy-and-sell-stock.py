class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price= float('inf')
        max_prof=0
        for i in prices:
            if i<min_price:
                min_price=i
            elif i-min_price>max_prof:
                max_prof=i-min_price
        return max_prof