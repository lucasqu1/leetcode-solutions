Lots of questions, but some are a bit trivial, so I won't write them:

1D DP:
- Climb stairs
The way I understood this one is that if we were to explicitly enumerate the solutions for getting to stair i - 1, and stair i - 2, they would be sequences.
We can get to stair i by extending a sequence for solution i - 1 by adding a step of 1, or we can extend a sequence for getting to solution i - 2 by adding a step of 2.
This is why dp[i] = dp[i - 1] + dp[i - 2].

Array:
- Combine 2 arrays in place. Advance pointers forward and handle logic for when 1 array is emptied first.
