def calculate_elevation_gain(x, y, prefix_sums):
    return sum(prefix_sums[x:y+1])

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    trails = [list(map(int, input().split())) for _ in range(M)]

    # Precompute elevation between consecutive points
    elevation_gains = [0] * N
    desent_gains = [0] * N
    for i in range(N):
        num = points[i][1] - points[i-1][1]
        if num > 0:
            elevation_gains[i] = num
        else:
            desent_gains[i] = abs(num)

    for x, y in trails:
        if x == y: print(0)
        elif x > y: print(calculate_elevation_gain(y-1, x-1, elevation_gains))
        else: print(calculate_elevation_gain(x-1, y-1, desent_gains))

if __name__ == "__main__":
    main()
