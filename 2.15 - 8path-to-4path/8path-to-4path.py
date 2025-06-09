def convert_8path_to_4path(grid):
    from collections import deque

    rows, cols = len(grid), len(grid[0])
    directions_8 = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    # retorna todos os vizinhos ativos (1) em 8 direções
    def get_neighbors(x, y):
        return [(x+dx, y+dy) for dx, dy in directions_8
                if 0 <= x+dx < rows and 0 <= y+dy < cols and grid[x+dx][y+dy] == 1]

    endpoints = [(x, y) for x in range(rows) for y in range(cols)
                 if grid[x][y] == 1 and len(get_neighbors(x, y)) == 1]

    if len(endpoints) != 2:
        raise ValueError("Path must have 2 endpoints")

    # BFS para reconstruir o caminho
    path = []
    visited = set()
    q = deque([endpoints[0]])
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path.append((x, y))
        for nx, ny in get_neighbors(x, y):
            if (nx, ny) not in visited:
                q.append((nx, ny))
                break

    new_path = [path[0]]

    # conversão de diagonais
    for i in range(1, len(path)):
        x0, y0 = new_path[-1]
        x1, y1 = path[i]
        dx, dy = x1 - x0, y1 - y0

        if abs(dx) == 1 and abs(dy) == 1:
            new_path.append((x0 + dx, y0))
            new_path.append((x0 + dx, y0 + dy))
        else:
            new_path.append((x1, y1))

    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for x, y in new_path:
        new_grid[x][y] = 1

    return new_grid

# -------------------------------

print("Digite a matriz linha por linha (apenas 0s e 1s separados por espaço).")
print("Digite uma linha vazia para finalizar.\n")

grid = []
while True:
    line = input()
    if not line.strip():
        break
    row = list(map(int, line.strip().split()))
    grid.append(row)

try:
    converted = convert_8path_to_4path(grid)
    print("\nMatriz com 4-conectividade:")
    for row in converted:
        print(' '.join(str(c) for c in row))
except Exception as e:
    print("Erro:", e)
