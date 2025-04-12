# Solution for https://coderun.yandex.ru/problem/nearest-bus-stop/

def find_nearest_stop(stops, query):
    left = 0
    right = len(stops) - 1
    
    if query <= stops[0]:
        return 0
    
    if query >= stops[-1]:
        return len(stops) -1
    
    while left <= right:
        mid = left + (right - left) // 2
        if stops[mid] == query:
            while mid > 0 and stops[mid-1] == query:
                mid -= 1
            return mid 
        elif stops[mid] < query:
            left = mid + 1
        else:
            right = mid - 1
    
    
    left_dist = query - stops[right] if right >= 0 else float('inf')
    right_dist = stops[left] - query if left < len(stops) else float('inf')
    
    if left_dist < right_dist:
        return right
    elif right_dist < left_dist:
        return left  
    else:
        return right

def solution():
    n, k = map(int, input().split())
    stops = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    
    for query in queries:
        nearest = find_nearest_stop(stops, query)
        print(nearest+1) # converting to 1-based index

if __name__ == "__main__":
    solution()