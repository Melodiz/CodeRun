def count_active_os(M, n, installations):
    active_partitions = []

    for a, b in installations:
        # Remove overlapping partitions
        active_partitions = [part for part in active_partitions if part[1] < a or part[0] > b]
        # Add the new partition
        active_partitions.append((a, b))

    return len(active_partitions)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    M = int(data[0])
    n = int(data[1])
    installations = [(int(data[i]), int(data[i+1])) for i in range(2, len(data), 2)]
    
    result = count_active_os(M, n, installations)
    print(result)

if __name__ == "__main__":
    main()