class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def combo(curr_combo, num_opening = 0, num_closing = 0):
            if len(curr_combo) == 2*n:
                ans.append(curr_combo)
                return
            if num_opening <n:
                combo(curr_combo + "(", num_opening+1, num_closing)
            if num_closing<num_opening:
                combo(curr_combo + ")", num_opening, num_closing+1)
        combo("")
        return ans