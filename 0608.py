# class Solution:
#     def minimumPushes(self, word: str) -> int:
#         for i in word:
#             print(ord(i))

word="bbbcdefghaaaikj"
class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        count=0
        for i in word:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d={k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
        x=0
        for i in d:
            if x<8:
                count+=d[i]
            elif x<16:
                count+=2*d[i]
            elif x<24:
                count+=3*d[i]
            else:
                count+=4*d[i]
            x+=1
        return count
x= Solution()
ans=x.minimumPushes(word)
print(ans)