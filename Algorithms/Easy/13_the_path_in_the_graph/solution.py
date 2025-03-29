from collections import deque


def bfs_shortest_path(adj_matrix, start, end):
    n = len(adj_matrix)
    visited = [False] * n
    distance = [-1] * n
    parent = [-1] * n
    queue = deque([start])

    visited[start] = True
    distance[start] = 0

    while queue:
        current = queue.popleft()

        for neighbor in range(n):
            if adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)

                if neighbor == end:
                    path = []
                    while neighbor != -1:
                        path.append(neighbor + 1)
                        neighbor = parent[neighbor]
                    path.reverse()
                    return distance[end], path

    return -1, []


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    n = int(data[index])
    index += 1

    adj_matrix = []
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        adj_matrix.append(row)
        index += n

    start = int(data[index]) - 1
    end = int(data[index + 1]) - 1
    if start == end:
        print(0)
    else:
        distance, path = bfs_shortest_path(adj_matrix, start, end)
        if distance == -1:
            print(-1)
        else:
            print(distance)
            print(" ".join(map(str, path)))


if __name__ == "__main__":
    main()