class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # rec 2 in rec 1:
        vertices1 = [(rec2[0], rec2[1]),(rec2[2], rec2[3]), (rec2[0], rec2[3]), (rec2[2], rec2[1]) ]
        for i, j in vertices1:
            # print("checking vertex: ", (i, j))
            if (i<rec1[2] and i>rec1[0]) and (j<rec1[3] and j>rec1[1]):
                return True
        # rec 1 in rec 2:
        vertices2 = [(rec1[0], rec1[1]),(rec1[2], rec1[3]), (rec1[0], rec1[3]), (rec1[2], rec1[1]) ]
        for i, j in vertices2:
            # print("checking vertex: ", (i, j))
            if (i<rec2[2] and i>rec2[0]) and (j<rec2[3] and j>rec2[1]):
                return True
        # edge case:
        if rec1[0]>=rec2[0] and rec1[2]<=rec2[2] and rec1[1]<=rec2[1] and rec1[3]>=rec2[3]:
            return True
        if rec2[0]>=rec1[0] and rec2[2]<=rec1[2] and rec2[1]<=rec1[1] and rec2[3]>=rec1[3]:
            return True
        
        return False

# class Solution:
#     def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
#         return rec1[0] < rec2[2] and rec1[1] < rec2[3] and rec1[2] > rec2[0] and rec1[3] > rec2[1]
