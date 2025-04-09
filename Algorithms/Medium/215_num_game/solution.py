# Solution for https://coderun.yandex.ru/problem/num-game/

def solution():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    dp = [0] * (n + 1)
    
    dp[n] = 0
    
    for i in range(n - 1, -1, -1):
        dp[i] = float('-inf')
        
        current_sum = 0
        for j in range(1, min(m + 1, n - i + 1)):
            current_sum += numbers[i + j - 1]
            dp[i] = max(dp[i], current_sum - dp[i + j])
    
    return 1 if dp[0] > 0 else 0

if __name__ == "__main__":
    print(solution())