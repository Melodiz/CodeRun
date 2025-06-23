# Solution for https://coderun.yandex.ru/problem/roulette
# Other solutions: https://github.com/Melodiz/CodeRun

def solve(k, x, y, u, v, a, b):
    petya_win_count = y - x + 1
    vasya_win_count = v - u + 1
    intersection_start = max(x, u)
    intersection_end = min(y, v)
    
    both_win_count = 0
    if intersection_start <= intersection_end:
        both_win_count = intersection_end - intersection_start + 1

    total_outcomes = 37
    prob_petya_only = (petya_win_count - both_win_count) / total_outcomes
    prob_vasya_only = (vasya_win_count - both_win_count) / total_outcomes
    prob_both = both_win_count / total_outcomes
    prob_neither = 1.0 - (prob_petya_only + prob_vasya_only + prob_both)

    dp_prev = [[0.0 for _ in range(k + 1)] for _ in range(k + 1)]
    dp_prev[0][0] = 1.0

    for round_num in range(1, k + 1):
        dp_curr = [[0.0 for _ in range(k + 1)] for _ in range(k + 1)]
        for p_chips in range(round_num):
            for v_chips in range(round_num):
                
                if dp_prev[p_chips][v_chips] == 0:
                    continue

                current_prob = dp_prev[p_chips][v_chips]

                if p_chips + 1 <= k:
                    dp_curr[p_chips + 1][v_chips] += current_prob * prob_petya_only

                if v_chips + 1 <= k:
                    dp_curr[p_chips][v_chips + 1] += current_prob * prob_vasya_only

                if p_chips + 1 <= k and v_chips + 1 <= k:
                    dp_curr[p_chips + 1][v_chips + 1] += current_prob * prob_both

                dp_curr[p_chips][v_chips] += current_prob * prob_neither
        
        dp_prev = dp_curr

    return dp_prev[a][b]

def main():
    t = int(input())
    for _ in range(t):
        k, x, y, a, b, v1, v2 = map(int, input().split())
        print(solve(k, x, y, a, b, v1, v2))

if __name__ == "__main__":
    main()
