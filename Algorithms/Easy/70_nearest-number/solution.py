def find_closest_number(data, n, goal):
    closest_number = None
    min_diff = float('inf')

    for num in data:
        diff = abs(num - goal)
        if diff < min_diff:
            min_diff = diff
            closest_number = num

    return closest_number

def main():
    n = int(input())
    data = list(map(int, input().split()))
    goal = int(input())
    print(find_closest_number(data, n, goal))
    return


if __name__ == "__main__":
    main()
