def main():
    n, m = map(int, input().split())  # Read n and m from input
    events = []
    
    for _ in range(m):
        start, end = map(int, input().split())  # Read each pair of b1 and b2
        events.append((start, 0))  # Add start event
        events.append((end, 1))  # Add end event
    
    events.append((n + 1, 0))  # Add a dummy start event at n+1
    events.append((n + 1, 1))  # Add a dummy end event at n+1
    
    events.sort()  # Sort events by point value
    
    prev = 0  # Initialize previous point
    result = 0  # Initialize sum of uncovered segments
    balance = 0  # Initialize count of active segments
    
    for point, event_type in events:
        if balance == 0:  # If no active segments
            result += point - prev - 1  # Add the length of the uncovered segment
        if event_type == 1:  # If it's an end event
            prev = point  # Update previous point
            balance -= 1  # Decrease active segments count
        else:  # If it's a start event
            balance += 1  # Increase active segments count
    
    print(result)  # Print the result

if __name__ == "__main__":
    main()