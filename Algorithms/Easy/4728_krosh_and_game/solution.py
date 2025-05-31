# Solution for https://coderun.yandex.ru/problem/krosh-and-game
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    MAX_N = 100000
    dp = [False] * (MAX_N + 1)

    # Precompute perfect squares up to MAX_N
    perfect_squares = []
    i = 1
    while i * i <= MAX_N:
        perfect_squares.append(i * i)
        i += 1

    # dp[0] is False (base case)
    # dp[i] is True if there exists a move to a state j where dp[j] is False
    # dp[i] is False if all moves lead to a state j where dp[j] is True
    for i in range(1, MAX_N + 1):
        can_win_from_i = False
        for square in perfect_squares:
            if i - square >= 0:
                if not dp[i - square]:
                    can_win_from_i = True
                    break
        dp[i] = can_win_from_i

    q = int(input())
    for _ in range(q):
        n = int(input())
        print("1" if dp[n] else "0")


if __name__ == "__main__":
    main()
