def count_cancer_cells(grid, r, c):
    # Define directions for neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def is_isolated(x, y):
        # Check all four possible directions for neighboring cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == '#':
                return False
        return True
    
    count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '#' and is_isolated(i, j):
                count += 1
    
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    index = 0
    results = []
    
    while index < len(data):
        r, c = map(int, data[index].strip().split())
        if r == 0 and c == 0:
            break
        
        grid = [data[index + 1 + i].strip() for i in range(r)]
        index += r + 1
        
        result = count_cancer_cells(grid, r, c)
        results.append(result)
    
    for i, result in enumerate(results):
        print(result)

if __name__ == "__main__":
    main()
