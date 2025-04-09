# Solution for https://coderun.yandex.ru/problem/max-num-split/

def find_max_distinct_split(s):
    # Brute force approach to find all possible splits
    def backtrack(start, path, used):
        if start == len(s):
            return path
        
        best_path = []
        
        for end in range(start + 1, len(s) + 1):
            num = s[start:end]
            
            # Skip numbers with leading zeros
            if num[0] == '0' and len(num) > 1:
                continue
            
            # Skip if this number is already used
            if num in used:
                continue
            
            # Try this number
            new_path = path + [num]
            new_used = used | {num}
            
            # Recursively find the best path
            result = backtrack(end, new_path, new_used)
            
            # Update best path if this one has more parts
            if len(result) > len(best_path):
                best_path = result
        
        return best_path
    
    return backtrack(0, [], set())

def solution(n):
    result = find_max_distinct_split(n)
    return "-".join(result)

if __name__ == "__main__":
    print(solution(input()))