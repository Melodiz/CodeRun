# Solution for https://coderun.yandex.ru/problem/sum-of-cubes/

def solution(N):
    # Initialize the list of cubes up to the cube root of N
    max_k = int(round(N ** (1/3))) + 2  # Adding buffer to avoid missing due to floating errors
    cubes = []
    for k in range(1, max_k + 1):
        cube = k ** 3
        if cube <= N:
            cubes.append(cube)
        else:
            break
    
    # Initialize DP array
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  # Base case: 0 cubes needed for 0
    
    for i in range(1, N + 1):
        for cube in cubes:
            if cube <= i:
                if dp[i - cube] + 1 < dp[i]:
                    dp[i] = dp[i - cube] + 1
    return dp[N]

if __name__ == "__main__":
    N = int(input())
    print(solution(N)) 