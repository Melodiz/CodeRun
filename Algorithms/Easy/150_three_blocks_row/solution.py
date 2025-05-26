# Solution for https://coderun.yandex.ru/problem/three-blocks-row/

def count_sequences(n):
    # dp[i][j] represents the number of valid sequences of length i
    # ending with j consecutive ones (j can be 0, 1, or 2)
    dp = [[0, 0, 0] for _ in range(n + 1)]
    
    # Base case: empty sequence
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        # If we add a 0, we reset the consecutive ones count
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        
        # If we add a 1 after 0 consecutive ones
        dp[i][1] = dp[i-1][0]
        
        # If we add a 1 after 1 consecutive one
        dp[i][2] = dp[i-1][1]
    
    # Sum all possibilities for sequences of length n
    return dp[n][0] + dp[n][1] + dp[n][2]

if __name__ == "__main__":
    print(count_sequences(int(input())))