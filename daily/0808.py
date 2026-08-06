class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans=[[rStart,cStart]]
        x=1
        print(ans)
        print(len(ans))
        print(rows)
        print(cols)
        print(rows*cols)
        while ((len(ans))<(rows*cols)):
            cStart+=x
            if 0<=cStart<cols and 0<=rStart<rows:
                ans+=[[rStart,cStart]]
            rStart+=x
            if 0<=rStart<rows and 0<=cStart<cols:
                ans+=[[rStart,cStart]]
            x+=1
            if x==4:
                break
            cStart-=x
            if 0<=rStart<rows and 0<=cStart<cols:
                ans+=[[rStart,cStart]]
            rStart-=x
            if 0<=rStart<rows and 0<=cStart<cols:
                ans+=[[rStart,cStart]]
            x+=1

        print(ans)
        print(len(ans))
        print(rows)
        print(cols)
        print(rows*cols)
        return ans