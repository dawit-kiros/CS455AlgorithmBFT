from collections import deque

def hasPath(maze, start, destination):
    rows = len(maze)
    cols = len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    
    queue = deque([start])
    visited = set(start)
    
    while queue:
        current_row, current_col = queue.popleft()
        
        if [current_row, current_col] == destination:
            return True
        
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            
            # Move in the current direction until you hit a wall or go out of bounds
            while 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0:
                new_row += dr
                new_col += dc
            
            # Adjust back to valid cell
            new_row -= dr
            new_col -= dc
            
            if (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
                
    return False

# Test data
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

start = [0, 4]
destination = [4, 4]

print(hasPath(maze, start, destination))  # Output: True
