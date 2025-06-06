# Solution for https://coderun.yandex.ru/problem/metro-loop
# Other solutions: https://github.com/Melodiz/CodeRun

def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def solve_metro_loop():
    import sys
    
    # Read all events
    events = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        pid = int(parts[0])
        action = parts[1]
        station = int(parts[2])
        time = parts[3]
        events.append((pid, action, station, time_to_minutes(time)))
    
    # Sort events by time
    events.sort(key=lambda x: x[3])
    
    # Track passengers in train
    passengers_in_train = set()
    
    start_time = time_to_minutes("05:00")  # 5:00
    end_time = time_to_minutes("23:30")    # 23:30
    
    # Create timeline with all events
    timeline = []
    current_time = start_time
    
    for pid, action, station, event_time in events:
        # Add segment before this event
        if event_time > current_time:
            timeline.append((current_time, event_time, len(passengers_in_train)))
            current_time = event_time
        
        # Process the event
        if action == 'in':
            passengers_in_train.add(pid)
        else:  # action == 'out'
            passengers_in_train.discard(pid)
    
    # Add final segment
    if current_time < end_time:
        timeline.append((current_time, end_time, len(passengers_in_train)))
    
    # Calculate weighted average
    total_weighted_time = 0
    total_journey_time = end_time - start_time
    
    for start, end, passenger_count in timeline:
        duration = end - start
        total_weighted_time += duration * passenger_count
    
    average = total_weighted_time / total_journey_time
    print(f"{average:.12f}")

if __name__ == "__main__":
    solve_metro_loop()
