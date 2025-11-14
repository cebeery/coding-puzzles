"""
Given a 0-indexed n x n integer matrix grid,
return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal
if they contain the same elements in the same order (i.e., an equal array).

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
-----------
Results
Runtime: 19 ms - beats 79.39%
Memory: 21.85 MB - beats 83.35%
"""
from collections import defaultdict

import tester


def solution(grid: list[list[int]]) -> int:
    rows = defaultdict(int)
    for row in grid:
        rows[tuple(row)] += 1

    cols = defaultdict(int)
    for i in range(len(grid)):
        col = [row[i] for row in grid]
        cols[tuple(col)] += 1

    ct = 0
    for row, freq in rows.items():
        ct += freq * cols[row]
    return ct


tester.test([[[3,2,1],[1,7,6],[2,7,7]]], 1, solution)
tester.test([[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]], 3, solution)
