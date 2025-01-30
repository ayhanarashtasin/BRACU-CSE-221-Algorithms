#Taking input____________________________________________________________________________
import queue
with open("output1a.txt","w") as out_f:
  with open("input1a.txt","r") as inp_f:
    read = inp_f.read().split("\n")
#Taking Input Ends Here__________________________________________________________________
    
#Main Code Starts Frome Here_____________________________________________________________
    from collections import deque
    def max_diamonds(grid, R, H):
        max_d = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for i in range(R):
            for j in range(H):
                if grid[i][j] != '#':
                    visited = [[False for _ in range(H)] for _ in range(R)]
                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True
                    diamonds = 0
                
                    while queue:
                        x, y = queue.popleft()
                        if grid[x][y] == 'D':
                            diamonds += 1
                    
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < R and 0 <= ny < H:
                                if grid[nx][ny] != '#' and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))
                    max_d = max(max_d, diamonds)
        return max_d
#Main Code Ends Here_____________________________________________________________________
      
#Drive Code Which I Made_________________________________________________________________


#Driver Code Ends Here____________________________________________________________________
