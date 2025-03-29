import sys
sys.setrecursionlimit(100_000)
def read_file(file_path='ML/Easy/587_cat-search/input.txt'):
    data = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            data.append(list(map(int, line.strip().split())))
    return data


def mark_all_islands(matrix):
    if not matrix or not matrix[0]:
        return matrix, 0

    def dfs(matrix, i, j, island_id):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != 1:
            return
        matrix[i][j] = island_id
        dfs(matrix, i + 1, j, island_id)
        dfs(matrix, i - 1, j, island_id)
        dfs(matrix, i, j + 1, island_id)
        dfs(matrix, i, j - 1, island_id)

    island_id = 2  # Start marking islands from 2 since 1 is already used in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                dfs(matrix, i, j, island_id)
                island_id += 1
    return matrix, island_id - 2


def main():
    matrix = read_file('input.txt')
    marked_matrix, num_islands = mark_all_islands(matrix)
    print(num_islands)
    for line in marked_matrix:
        print(' '.join(map(str, line)))
    return


if __name__ == '__main__':
    main()
