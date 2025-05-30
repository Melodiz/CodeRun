# Solution for https://coderun.yandex.ru/problem/traffic-lanes
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    m, n = map(int, input().split())

    # dp[j] will store dp[current_lane_idx][j]
    # which is the number of ways to assign directions for current_lane_idx lanes
    # such that current_lane_idx covers up to direction j (max_dir[current_lane_idx]=j)
    # and all directions 1...j are covered.

    # Initialize for lane 1: dp[1][j] = 1 for j=1..m
    # Lane 1 must cover [1, j]. There's only 1 way to do this for each j.
    dp = [0] * (m + 1)
    for j in range(1, m + 1):
        dp[j] = 1

    # Iterate for lanes from 2 to n
    for _lane_idx in range(2, n + 1):
        new_dp = [0] * (m + 1)
        
        # S[j] = sum(dp[prev_lane][x] for x from 1 to j)
        S = [0] * (m + 1)
        for j in range(1, m + 1):
            S[j] = S[j-1] + dp[j]
        
        # Calculate new_dp for the current lane
        # dp[current_lane][j] = S[prev_lane][j] + S[prev_lane][j-1]
        for j in range(1, m + 1):
            term1_sum_up_to_j = S[j]
            term2_sum_up_to_j_minus_1 = S[j-1] # S[0] is 0
            new_dp[j] = term1_sum_up_to_j + term2_sum_up_to_j_minus_1
        dp = new_dp

    # The final answer is dp[n][m], which is stored in dp[m] after the loops
    print(dp[m])

if __name__ == "__main__":
    main()
