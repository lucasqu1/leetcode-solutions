Lots of questions, but some are a bit trivial, so I won't write them:

1D DP:
- Climb stairs
The way I understood this one is that if we were to explicitly enumerate the solutions for getting to stair i - 1, and stair i - 2, they would be sequences.
We can get to stair i by extending a sequence for solution i - 1 by adding a step of 1, or we can extend a sequence for getting to solution i - 2 by adding a step of 2.
This is why dp[i] = dp[i - 1] + dp[i - 2].

Array:
- Combine 2 arrays in place. Advance pointers forward and handle logic for when 1 array is emptied first.

Course Schedule I or II:
- Both trivial implementations of Kahn's

Valid Tree:
- Need to check for the ccs = 1 condition as well as ensuring that none of the unions fail.

Word Ladder:
- It's a simple graph BFS.
- The optimization works by generating the neighbors on the fly instead of calculating an adjacency list.
- O(26*N^2 L)

Pacific Atlantic Ocean Flow
- BFS around the edges instead of from each cell. We want to find all cells reachable from the atlantic and the pacific.

Walls and Gates:
- BFS from each gate to each cell. 
