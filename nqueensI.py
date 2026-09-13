class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Already am aware of this solution. 
        # Implemented it yesterday, but let's see if I can still conceptually walk through it.

        colSet = set()
        posDiag = set()
        negDiag = set()

        rows = [("." * i) + "Q" + ("." * (n - 1 - i)) for i in range(n)]

        res = []

        def rec(row, solution):
            if row == n:
                res.append(solution[:])
                return
            
            for col in range(n):
                pos = row + col
                neg = row - col
                if col in colSet or pos in posDiag or neg in negDiag:
                    continue
                
                solution.append(rows[col])
                colSet.add(col)
                posDiag.add(pos)
                negDiag.add(neg)
                rec(row + 1, solution)

                solution.pop()
                colSet.remove(col)
                posDiag.remove(pos)
                negDiag.remove(neg)

        rec(0, [])

        return res






        