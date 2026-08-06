# class Solution:
#     def countSeniors(self, details: List[str]) -> int:
#         count=0
#         for i in details:
#             if int(i[11:13])>60:
#                 count+=1
#         return count

# import numpy as np
# class Solution:
#     def countSeniors(self, details: List[str]) -> int:
#         arr_details= np.array(details)
#         arr_age =arr_details[:][11:13]
# import numpy as np
# class Solution:
#     def countSeniors(self, details: List[str]) -> int:
#         age=[int(x[11:13]) for x in details]
#         arr_age=np.array(age)
#         arr_above60 = arr_age>60
#         count=len(arr_above60[arr_above60==True])
#         return count
