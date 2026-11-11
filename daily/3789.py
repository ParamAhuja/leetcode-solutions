class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # case 1: costboth >= cost1+cost2 -> need1*cost1+need2*cost2
        if cost1+cost2<=costBoth:
            return (need1*cost1 + need2*cost2)
        
        # case 2: costboth < cost1+cost2 ->
        #   1. min(need1, need2) obv will be costboth
        #   2. after that, abs(need2-need1) ->
        #       if cost 2 is less now, take that fully
        #       else, take costboth fully
        if need1 <= need2:
            ans = need1*costBoth
            if cost2<=costBoth:
                ans += (need2-need1) * cost2
            else:
                ans += (need2-need1) * costBoth
        else:
            ans = need2*costBoth
            if cost1<=costBoth:
                ans += (need1-need2) * cost1
            else:
                ans += (need1-need2) * costBoth
        return ans

# M2:
# class Solution:
#     def minimumCost(self,cost1:int,cost2:int,costBoth:int,need1:int,need2:int)->int:
#         together=min(need1,need2)
#         return (together*min(costBoth,cost1+cost2)+
#                 max(0,need1-need2)*min(cost1,costBoth)+
#                 max(0,need2-need1)*min(cost2,costBoth))
