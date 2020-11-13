import random
import copy
import sys
import itertools

def print_grid(l):
    rows = [ ''.join(row) + '\n' for row in l ]
    grid = ''.join(rows)
    print(grid)

def get_neighbors(r, c, n_rows, n_cols):
    neighbors = []
    for (dr, dc) in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        if 0 <= r + dr < n_rows and 0 <= c + dc < n_cols:
            neighbors.append((r + dr, c + dc))
    return neighbors

def generate_DFS_tree(r0, c0, visited, n_rows, n_cols):
    visited.add((r0, c0))
    tree = set()
    neighbors = get_neighbors(r0, c0, n_rows, n_cols)
    random.shuffle(neighbors)
    for (r, c) in neighbors:
        if (r, c) not in visited:
            tree.add(((r0, c0), (r, c)))
            tree |= generate_DFS_tree(r, c, visited, n_rows, n_cols)
    return tree

def generate_maze_tree(n_rows, n_cols):
    limit = max(sys.getrecursionlimit(), n_rows * n_cols)
    sys.setrecursionlimit(limit)
    visited = set()
    tree = generate_DFS_tree(0, 0, visited, n_rows, n_cols)
    return tree

def edge_to_canvas_coords(edge):
    ((r0, c0), (r1, c1)) = edge
    r = 1 + r0 + r1
    c = 1 + c0 + c1
    return (r, c)

def full_maze_set(n_rows, n_cols):
    R, C = 2 * n_rows + 1, 2 * n_cols + 1
    maze_set = set()
    for r in range(n_rows):
        maze_set |= { (2 * r, c) for c in range(C) }
        maze_set |= { (2 * r + 1, c) for c in range(C) if c % 2 == 0}
    maze_set |= { (2 * n_rows, c) for c in range(C) }
    return maze_set

def remove_wall(maze_set, edge):
    r, c = edge_to_canvas_coords(edge)
    maze_set.remove((r, c))

def generate_maze_set(n_rows, n_cols):
    tree = generate_maze_tree(n_rows, n_cols)
    maze_set = full_maze_set(n_rows, n_cols)
    for edge in tree:
        remove_wall(maze_set, edge)
    return maze_set

def generate_maze_grid(R, C, maze_set):
    grid = [ [' ' for c in range(C) ] for r in range(R) ]
    for block in maze_set:
        r, c = block
        grid[r][c] = '#'
    return grid

def print_maze(n_rows, n_cols):
    tree = generate_maze_tree(n_rows, n_cols)
    maze_set = generate_maze_set(n_rows, n_cols, tree)
    grid = generate_maze_grid(2 * n_rows + 1, 2 * n_cols + 1, maze_set)
    print_grid(grid)
