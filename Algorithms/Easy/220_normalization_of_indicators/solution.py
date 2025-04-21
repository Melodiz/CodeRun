# Solution for https://coderun.yandex.ru/problem/normalization-of-indicators/

def find_closest_value(indicators, target):
    left = 0
    right = len(indicators) - 1
    
    if right == 0 or target <= indicators[0]:
        return 0
    
    if target >= indicators[right]:
        return right
    
    while left <= right:
        mid = (left + right) // 2
        if indicators[mid] == target:
            return mid
        elif indicators[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if left < len(indicators) and right >= 0:
        if abs(indicators[left] - target) < abs(indicators[right] - target):
            return left
        else:
            return right
    elif left < len(indicators):
        return left
    else:
        return right

def solution():
    n = int(input())
    indicators = list(map(int, input().split()))
    indicators.sort()
    m = int(input())
    for _ in range(m):
        target = int(input())
        print(indicators[find_closest_value(indicators, target)])

if __name__ == "__main__":
    solution()