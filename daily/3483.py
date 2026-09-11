"""
# revise
M1: permutations
"""

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        ans = 0
        # generate perms
        perms = set()
        chosen = [0]*n
        def permute(curr_num = 0):
            if curr_num>99:
                if curr_num%2==0:
                    perms.add(curr_num)
                return

            for i in range(n):
                if chosen[i] != 0:
                    continue
                curr_num = curr_num*10+digits[i]
                chosen[i]=1
                permute(curr_num)
                chosen[i]=0
                curr_num//=10

        permute()
        return len(perms)



"""
M2: choose one digit at a time
math
"""
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        l=[]
        mp=[0]*10
        for d in digits:
            mp[d] +=1

        for i in range(1,10):
            if mp[i]==0:
                continue
            else:
                mp[i] -= 1
            for j in range(0,10):
                if mp[j]==0:
                    continue
                else:
                    mp[j] -=1
                for k in range(0,10,2):
                    if mp[k]>0:
                        l.append(i*100+j*10+k)

                mp[j] +=1
            mp[i] +=1

        return len(l)


"""
M3: optimal
math
"""

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from collections import defaultdict

        freq = defaultdict(int)
       
        uniq_even = set()
        count = 0
        for d in digits:
            if d%2 == 0:
                uniq_even.add(d)
            freq[d]+=1

        for e in uniq_even:
            freq[e]-=1

            keys = [k for k in freq if freq[k]>0]
            for i in range(len(keys)):
                for j in range(i+1,len(keys)):
                    a,b = keys[i], keys[j]
                    ## a,b,e 
                    if a!=0:
                        count+=1
                    if b!=0:
                        count+=1
                    
            for num in keys:
                if freq[num] >=2 and num!=0 :
                    ## num num e
                    count+=1
            freq[e]+=1
        
        return count
