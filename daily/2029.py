""" # revise
stone game ix

greedy, deterministic game, zero sum game, minimax, hashmap, game theory


1. the final outcome is dependent on who picks multiple of 3, so convert all numbers to mod 3 - i.e, 0, 1, 2 as a hashmap in an array
2. the goal for alice is to force bob to make the sum a multiple of 3. if you choose 1, other must choose 1 (2 would make a sum of 3). otherwise bob wins if the array runs out OR is you make a multiple of 3.
3. the role of zero is as a passer, it does not change sum but passes turns. it can not be picked in the start by alice.
4. the logic:
 A. if no. of zeros are even: 
 -- Rule: If both cnt1 >= 1 and cnt2 >= 1, Alice always wins.
 -- Why: Alice can look at the counts of Type 1 and Type 2 stones:
 -- If cnt1 <= cnt2, Alice starts by picking Type 1.
 -- If cnt1 > cnt2, Alice starts by picking Type 2.
 B. if no. of zeros are odd: 
 -- Rule: Alice wins only if |count1 - count2| > 2.
 -- Why: Because Bob can flip parity once using the odd Type 0 stones, Alice needs a significant imbalance between cnt1 and cnt2 (a difference greater than 2) so that Bob still runs out of valid moves even after using his turn-flip trick.
O(n)
"""


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        counts = [0,0,0] # frequency of 0 1, 2 after %3
        for i in stones:
            counts[i%3]+=1
        
        if counts[0] % 2 == 0:
            return counts[1] >= 1 and counts[2] >= 1
        else:
            return abs(counts[1] - counts[2]) > 2