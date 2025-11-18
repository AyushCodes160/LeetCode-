from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        ans = 0

        while q:
            row, col, time = q.popleft()
            for dr, dc in direction:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    q.append((new_row, new_col, time + 1))
                    ans = max(ans, time + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return ans
