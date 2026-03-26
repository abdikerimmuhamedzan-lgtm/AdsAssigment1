def fill_spiral(grid, top, left, bottom, right, num):
    if top > bottom or left > right:
        return
    for i in range(left, right + 1):
        grid[top][i] = num
        num += 1
    for i in range(top + 1, bottom + 1):
        grid[i][right] = num
        num += 1
    if top < bottom:
        for i in range(right - 1, left - 1, -1):
            grid[bottom][i] = num
            num += 1
    if left < right:
        for i in range(bottom - 1, top, -1):
            grid[i][left] = num
            num += 1
    fill_spiral(grid, top + 1, left + 1, bottom - 1, right - 1, num)


def print_grid(grid, row, n):
    if row == n:
        return
    print(' '.join(map(str, grid[row])))
    print_grid(grid, row + 1, n)


n = int(input())
grid = [[0] * n for _ in range(n)]
fill_spiral(grid, 0, 0, n - 1, n - 1, 1)
print_grid(grid, 0, n)