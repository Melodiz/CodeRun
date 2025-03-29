def main():
    n = int(input())  # Read n from input
    events = []
    
    for _ in range(n):
        line = list(map(int, input().split()))  
        start = 60 * line[0] + line[1]
        end = 60 * line[2] + line[3]
        if start < end:
            events.append((start, 0))  # Add start event
            events.append((end, 1))  # Add end event
        elif start > end:
            events.append((start, 0))  # Add start event
            events.append((24 * 60, 1))  # Add end event (wrap around midnight)
            events.append((0, 0))  # Add end event (wrap around midnight)
            events.append((end, 1))  # Add end event (wrap around midnight)
        else:  # start == end
            events.append((0, 0))  # Add start event
            events.append((24 * 60, 1))  # Add end event (wrap around midnight)
    
    events.sort()  # Sort events by point value
    
    prev = 0  # Initialize previous point
    result = 0  # Initialize sum of covered segments
    balance = 0  # Initialize count of active segments
    
    for point, event_type in events:
        if balance == n:  # If all n segments are active
            result += point - prev  # Add the length of the covered segment
        if event_type == 1:  # If it's an end event
            balance -= 1  # Decrease active segments count
        else:  # If it's a start event
            balance += 1  # Increase active segments count
        prev = point  # Update previous point
    
    print(result)  # Print the result

if __name__ == "__main__":
    main()