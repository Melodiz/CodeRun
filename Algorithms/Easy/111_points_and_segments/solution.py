def count_segments(n, segments, m, points):
    events = []
    for a, b in segments:
        events.append((min(a, b), 'L'))
        events.append((max(a, b), 'R'))
    
    for i in range(m):
        events.append((points[i], 'P', i))
    
    events.sort()
    
    counts = [0] * m
    active_segments = 0
    
    for event in events:
        if event[1] == 'L':
            active_segments += 1
        elif event[1] == 'R':
            active_segments -= 1
        else:
            counts[event[2]] = active_segments
    
    return counts

def main():
    # Example input
    n, m = map(int, input().split())
    segments = [list(map(int, input().split())) for _ in range(n)]
    points = list(map(int, input().split()))
    
    # Get the counts of segments each point belongs to
    result = count_segments(n, segments, m, points)
    
    # Print the result
    print(*result)

if __name__ == "__main__":
    main()