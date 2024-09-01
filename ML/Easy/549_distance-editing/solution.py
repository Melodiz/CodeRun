def levenshtein_distance_modified(str1, str2, insert_cost, delete_cost, substitute_cost):        
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i * delete_cost

    for j in range(n + 1):
        dp[0][j] = j * insert_cost

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = substitute_cost

            dp[i][j] = min(dp[i - 1][j] + delete_cost, dp[i][j - 1] + insert_cost, dp[i - 1][j - 1] + cost)

    return dp[-1][-1]


def main():
    input() # ignore the first line
    str1 = input()
    str2 = input()
    insert_cost, delete_cost, substitute_cost = map(int, input().split())
    print(levenshtein_distance_modified(str1, str2, insert_cost, delete_cost, substitute_cost))


if __name__ == "__main__":
    main()
