class Solution:
# easy: check if strings can be made equal by operations 1
    def hash(self, i, h):
        if i in h:
            h[i]+=1
        else:
            h[i] = 1
    def de_hash(self, i, h):
        if i in h:
            if h[i]>1:
                h[i]-=1
                return 1
            else:
                return h.pop(i)
        else:
            return False
    def canBeEqual(self, s1: str, s2: str) -> bool:
        h_e = {}
        h_o = {}
        for i in range(len(s1)):
            if i%2==0:
                self.hash(s1[i], h_e)
            else:
                self.hash(s1[i], h_o)
        # print(h_o)
        # print(h_e)
        for i in range(len(s2)):
            if i%2==0:
                a = self.de_hash(s2[i], h_e)
            else:
                a = self.de_hash(s2[i], h_o)
            if not a:
                return False
        # print("ho:", h_o)
        # print("he:", h_e)
        if len(h_o)>0 or len(h_e)>0:
            return False
        return True

# for length 4 always:
        # even_s1 = sorted([s1[0], s1[2]])
        # even_s2 = sorted([s2[0], s2[2]])
        
        # odd_s1 = sorted([s1[1], s1[3]])
        # odd_s2 = sorted([s2[1], s2[3]])
        
        # return even_s1 == even_s2 and odd_s1 == odd_s2
