class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        strings = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        res = []

        def rec(curr, index):
            if index == len(digits):
                res.append("".join(curr))
                return
            
            for c in strings[int(digits[index])]:
                curr.append(c)
                rec(curr, index + 1)
                curr.pop()

        rec([], 0)

        return res

        # very simple backtracking solution.
        # add a digit, recurse, undo to allow backtracking.
