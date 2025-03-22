from collections import deque

def generate_new_code(num):
    variations = set()
    num_str = str(num)
    
    if num_str[0] != '9':
        variations.add(str(int(num_str[0]) + 1) + num_str[1:])
    
    if num_str[-1] != '1':
        variations.add(num_str[:-1] + str(int(num_str[-1]) - 1))
    
    variations.add(num_str[-1] + num_str[:-1])
    
    variations.add(num_str[1:] + num_str[0])
    
    return variations

def bfs(start, end):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()
        
        if current == end:
            return path
        
        for next_num in generate_new_code(current):
            if next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, path + [next_num]))
    
    return None  # If no path is found

def main():
    start, end = input().strip(), input().strip()
    path = bfs(start, end)
    
    for num in path:
        print(num)

if __name__ == "__main__":
    main()