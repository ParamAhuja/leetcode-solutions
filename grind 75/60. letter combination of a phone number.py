"""
string, recursion, backtracking, searching
"""

class Solution:
    def words(self, curr_word, level):
        if len(self.digits) == level:
            self.ans.append(curr_word)
            return
        digit = int(self.digits[level])
        level+=1
        for i in self.choices[digit]:
            self.words(curr_word+i, level)
        level-=1

    def letterCombinations(self, digits: str) -> List[str]:
        self.ans = []
        self.digits=digits
        self.choices = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        self.words("", 0)
        return self.ans
