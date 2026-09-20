class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def undo(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != "S":
                return
            
            board[i][j] = "NO"

            undo(i + 1, j)
            undo(i, j + 1)
            undo(i - 1, j)
            undo(i, j - 1)

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != "O":
                return False
            
            board[i][j] = "S"
            print("modified " + str(i) + " " + str(j))

            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            touches_border = False

            if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                touches_border = True

            for move in moves:
                ai, aj = move
                neighbor = dfs(i + ai, j + aj)
                touches_border = touches_border or neighbor

            return touches_border

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j):
                    undo(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "NO":
                    board[i][j] = "O"
                elif board[i][j] == "S":
                    board[i][j] = "X"

            # An even more efficient solution exists, where I can just mark Os around the borders as unsafe, 
            # and then any O that is not marked as unsafe just becomes an X. so basically i should only process the borders
