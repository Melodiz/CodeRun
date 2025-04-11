# Solution for https://coderun.yandex.ru/problem/symbols-set-min-susbstr/

def solution(s, c):
    min_length = float('inf')
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Create a set from the current substring
            substring_set = set(s[i:j + 1])
            # Check if the substring set equals the required set
            if substring_set == c:
                min_length = min(min_length, j - i + 1)
    return min_length if min_length != float('inf') else 0
        

if __name__ == "__main__":
    s = input()
    c = set(input())
    print(solution(s, c))