# Solution for https://coderun.yandex.ru/problem/traffic-lanes
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    m, n = map(int, input().split())

    dp = [0] * (m + 1)
    for j in range(1, m + 1):
        dp[j] = 1

    for _lane_idx in range(2, n + 1):
        new_dp = [0] * (m + 1)
        
        S = [0] * (m + 1)
        for j in range(1, m + 1):
            S[j] = S[j-1] + dp[j]
        
        for j in range(1, m + 1):
            term1_sum_up_to_j = S[j]
            term2_sum_up_to_j_minus_1 = S[j-1] # S[0] is 0
            new_dp[j] = term1_sum_up_to_j + term2_sum_up_to_j_minus_1
        dp = new_dp

    print(dp[m])

if __name__ == "__main__":
    main()
