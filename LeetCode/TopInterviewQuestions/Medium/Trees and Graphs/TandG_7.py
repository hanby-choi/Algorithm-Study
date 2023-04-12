# Number of Islands
class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        cnt = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def dfs(x, y, grid, visited):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, grid, visited)
            return
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = True
                    cnt += 1
                    dfs(i, j, grid, visited)
                    
        return cnt
    def numIslands2(self, grid):
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def dfs(x, y, grid):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    dfs(nx, ny, grid)
            return
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    cnt += 1
                    dfs(i, j, grid)
                    
        return cnt