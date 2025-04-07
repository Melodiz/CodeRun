def find_best_trip(temperatures):
    if not temperatures:
        return 0, 0, 0
    
    n = len(temperatures)
    max_increase = 0
    best_start = 0
    best_end = 0
    
    # For each possible end day
    min_temp_idx = 0
    
    for end in range(1, n):
        # Update the minimum temperature index if needed
        if temperatures[end - 1] < temperatures[min_temp_idx]:
            min_temp_idx = end - 1
        
        # Calculate increase from current minimum to current end
        increase = temperatures[end] - temperatures[min_temp_idx]
        
        # If we found a better increase
        if increase > max_increase:
            max_increase = increase
            best_start = min_temp_idx
            best_end = end
        # If we found the same increase
        elif increase == max_increase:
            current_duration = best_end - best_start
            new_duration = end - min_temp_idx
            
            # Choose the shorter trip
            if new_duration < current_duration:
                best_start = min_temp_idx
                best_end = end
            # If same duration, choose the one with earlier end date
            elif new_duration == current_duration and end < best_end:
                best_start = min_temp_idx
                best_end = end
    
    return max_increase, best_start, best_end

def main():
    mums = list(map(int, input().split()))
    max_increase, start_day, end_day = find_best_trip(mums)
    print(max_increase, start_day, end_day)


if __name__ == "__main__":
    main()
