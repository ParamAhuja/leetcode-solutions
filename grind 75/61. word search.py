"""
graph traversal, graph dfs
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(root, word, visited):
            i = root[0]
            j = root[1]
            val = board[i][j]
            if val!=word[0]:
                return False
            if len(word) == 1:
                return True
            visited.append(root)
            neighbours = [[i+1, j], [i, j-1], [i-1, j], [i, j+1]]
            for neighbour in neighbours:
                x = neighbour[0]
                y = neighbour[1]
                if x>=0 and x<m and y>=0 and y<n and ([x,y] not in visited):
                    if dfs([x,y], word[1:], visited):
                        return True
            visited.remove([i,j])
            return False
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs([i,j], word, []):
                        return True
        return False


"""
optim:

1. use set for visited not list!

2.
#Check frequency in word to search

#Check if we have enough letters in the board:

3. 
#Check if its easier to search reverse 
#(if first letter occurs more often, then itll start more DFS)

"""