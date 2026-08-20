"""Cinema Seat Allocation
hashmap, greedy, bit manipulation

problem is memory, we NEED a hashmap but a list/set... gives MLE, hence use bits

"""
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        hashmap = {}
        for i in reservedSeats:
            if i[0] not in hashmap:
                hashmap[i[0]] = 0
            hashmap[i[0]] += 10**(10-i[1])

        ans = 2*n
        for i in hashmap:
            flag = 0
            filled = hashmap[i]
            if (filled%(10**5)) // 10 != 0:
                ans-=1
                flag+=1
            if (filled%(10**9)) //(10**5) != 0:
                ans-=1
                flag+=1
            if flag == 2 and (filled%(10**7))//1000 == 0:
                flag+=1
                ans+=1
            
        return ans
            
        