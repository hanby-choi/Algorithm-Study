class Solution(object):
    def exist(self, board, word):
        w = len(word)
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        self.found = False
        def backtracking(x, y, idx):
            if idx == (w-1) and board[x][y] == word[idx]:
                self.found = True
                return
            if board[x][y] == word[idx]:
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        backtracking(nx, ny, idx+1)
                        visited[nx][ny] = False
            return

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    backtracking(i, j, 0)
                    if self.found:
                        return True
                    visited[i][j] = False
        return self.found